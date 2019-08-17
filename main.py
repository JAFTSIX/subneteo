
import re
import sub
import comandos
import enrutar

subneteo='^\s*SU\s+(B|C)\s*IP:\s*([0-9]{,3}(.)){3}[0-9]{,3}\s*(LNS)\s*([0-9]*(,))*[0-9]*$'
vlanear='^\s*VL\s+[A-Z]*[0-9]*\/[0-9]*_[A-Z]*[0-9]*\/[0-9]*\s+(\s*!\s*N:\s*[0-9]*\s*R:\s*[0-9]*-[0-9]*\s*ID:[0-9]+\s*)*$'
vlanear2='^\s*VL\s+[A-Z]*[0-9]*\/[0-9]*_[A-Z]*[0-9]*\/[0-9]*\s+(\s*!\s*N:\s*[0-9]+\s*R:\s*[0-9]+-[0-9]+\s*)+$'

insertar='^\s*IN\s+(B|C)\s+([0-9]+\.){3}([0-9]+)\-(([0-9]+\.){3}([0-9]+)|([0-9]{2}))'

ips='^\s*IPS'
translate='^\s*M\s+[0-9]+'

def interfaz():
    print('E.S.A EL SACA APUROS 2019, ? para ayuda')
    while True:
        comando=input('ORDEN>').upper()
            
        if re.search(subneteo,comando):
                
              extraccionSUB(comando)
        elif  re.search(vlanear,comando) or re.search(vlanear2,comando) :
                
              extraccionVLANS(comando)        
        elif re.search('^(EX|EXI|EXIT|EXT)\s*$',comando):
              break 
        elif  re.search(translate,comando):
              X=sub.sacaMascara(comando.replace('M','').replace(' ',''))  
              print(X)
              print(sub.wilcard(X))               
        elif re.search(insertar,comando):
              #insert(comando)      
              pass
        elif re.search(ips,comando):
              print(' ') 
              for res in sub.red:
                    print(res)
                    print(' ') 
                    print(' ') 
              
        elif '?'==comando:
              print('subneteo comando ejemplo: SU B ip: 190.123.2.0 LNS 1000,100,1223,100')    
              print('                   ')            
              print('vlan comando ejemplo: VL FA0/1 !N:10 R:3-10 !N:20 R:12-30')    
              print('vlan con router:VL FA0/1_GB0/2 !N:10 R:3-10 ID:1 !N:20 R:12-30 ID:2 ')    
              print('bits a mascara: m 32 (probablemente lo mas util) ')            
        else:
              pass    

#su b ip: 190.123.0.0 lns 1500,1400,1000
#su c ip: 190.123.50.0 lns 50,24,12,5
#saca los datos de las tuplas y los limpia      
def extraccionSUB(subneteo):
    tipo=re.findall('(\s*(B|C)\s*){1}',subneteo)[0][0]
    tipo=tipo.replace(' ','')        
    ip=re.findall('(IP:\s*([0-9]{,3}(.)){3}[0-9]{,3}){1}',subneteo)[0][0]
    ip=ip.replace('IP:','')
    ip=ip.replace(' ','')
    lanes=re.findall('(\s*(LNS)\s*([0-9]*(,))*[0-9]*$){1}',subneteo)[0][0]
    lanes=lanes.replace('LNS','')            
    lanes=lanes.replace(' ','') 
    #print('TIPO='+tipo,'IP='+ip,'LANES='+lanes)
    sub.principal(ip,tipo,lanes)
     
#VL FA0/1_GB0/2 !N:10 R:3-10 !N:20 R:12-30       
#VL FA0/1_GB0/2 !N:10 R:3-10 ID:1 !N:20 R:12-30 ID:2     
def extraccionVLANS(comando):   
  vlans=list()
  lanes=re.findall('!\s*N:\s*[0-9]*\s*R:\s*[0-9]*-[0-9]*\s*',comando)
  ides=re.findall('ID:[0-9]+',comando)
  for lan in lanes:
                
     rango=re.findall('[0-9]*-[0-9]*',lan)
     lan=lan.replace('R:'+rango[0],'')
     lan=lan.replace(' ','')
     num=lan.replace('!N:','') 
     lan=lan.replace(' ','')
     vlans.append({'num':num,'rango':rango[0]})
  lanes=re.findall('\s+[A-Z]*[0-9]*\/[0-9]*_[A-Z]*[0-9]*\/[0-9]*\s+',comando)  
  splet=lanes[0].split('_')  
  alrou=splet[0].replace(' ','')
  alsw=splet[1].replace(' ','') 
  for i in range(len(ides)):
      ides[i]=ides[i].replace('ID:','')    
  comandos.switch(alrou,alsw,vlans,ides)      

#in B 190.123.8.0-255.255.248.0
def insert(comando):
 tipo=re.findall('(B|C){1}',comando)[0][0]
 comando=comando.replace('C','').replace('B','').replace('IN','').replace(' ','')
 ip=comando.split('-')[0]
 mascara=comando.split('-')[1]  
 sub.insert_p2(tipo,ip,mascara)
  

 

#su b ip:140.20.0.0 LNS 6000,4000,2000,1000
#VL FA0/1_Gi0/1 !N:10 R:8-9 ID:2 
#VL FA0/1_Gi0/1 !N:10 R:10-17 ID:1  
interfaz()
