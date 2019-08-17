import re


red=list() 

#METODO SOLO SIRVE CON CLASES TIPO B
def principal(ip,tipo,lanes): 
   
  lanes=lanes.split(',')
  resumen=list()
  for host in lanes:resumen.append(saltos(host,tipo))
  mision=salto(ip,resumen,tipo) 
  
  print('                                   ') 
  for res in mision:
    red.append(res)
    print(res)
    print('                                   ') 
    print('                                   ') 
  


#su c ip: 173.10.0.0 lns 50,25,10,6

def saltos(host,tipo):
  potencia=0

  
  
  if tipo=='B': 
    #255.255.0.0 
    while not ((2**potencia)-2 > int(host)):
      potencia=potencia+1
    mask=sacaMascara(str(16+(16-potencia)))
    salto=(2**potencia)//256   
  elif tipo=='C': 
    #255.255.255.0
    while not ((2**potencia) > int(host)):
      potencia=potencia+1
    mask=sacaMascara(str(24+(8-potencia)))
    salto=(2**potencia) 

  return {'salto' :salto,'mascara': mask}



def sacaMascara(MASCARA):
    
    new_Mask = '1A.2A.3A.4A'
    mask = int(MASCARA)
    # añado todos los 255
    

    letras = ['1A', '2A', '3A', '4A']
    bucle = 0 
    for R in letras:

        if (mask-8) == 0:
            break
        if (mask-8) < 0:
            break

        mask = mask-8
        new_Mask = new_Mask.replace(R, '255')

        bucle = bucle+1

    unos = 0
    i = 0
    for num in [7, 6, 5, 4, 3, 2, 1, 0]:
        i = i+1
        unos = unos+(2**num)
        if i == mask:
            break

    new_Mask = new_Mask.replace(letras[bucle], str(unos))
    # voy a verificar si hay un 0
    for rev in letras:
        for parte in new_Mask.split('.'):
            if parte == rev:
                new_Mask = new_Mask.replace(rev, '0')
    return new_Mask
     

def salto(ip,resumen,tipo):
  tipo=tipo.replace(' ','')
  ip=limpiar(ip,tipo)
  mision=list()
  
  if tipo=='B':
    i=0
    igu=0
    print(ip)
    for elemento in resumen:   
        red=ip.replace('.a.b','.'+str(igu)+'.0')   
        a=int(elemento['salto'])
        igu=igu
        primera=ip.replace('.a.b','.'+str(igu)+'.1')
        
        igu=igu+a-1
        ultima=ip.replace('.a.b','.'+str(igu)+'.254')
        igu=igu+1
        broad=ip.replace('.a.b','.'+str(igu-1)+'.255')
        i=i+1   
        mision.append({'id':i,'red':red,'primera':primera,'ultima':ultima,'broad':broad,'mascara':elemento['mascara'] ,'wil':wilcard(elemento['mascara'])})
  elif tipo=='C':           
    igu=0
    i=0
    for elemento in resumen:   
          red=ip.replace('.b','.'+str(igu))   
          a=int(elemento['salto'])
          primera=ip.replace('.b','.'+str(igu+1))
          igu=igu+a-2
          ultima=ip.replace('.b','.'+str(igu))
          igu=igu+1
          broad=ip.replace('.b','.'+str(igu))
          igu=igu+1
          i=i+1
          mision.append({'id':i,'red':red,'primera':primera,'ultima':ultima,'broad':broad,'mascara':elemento['mascara'],'wil':wilcard(elemento['mascara'])})
  return mision
  

def limpiar(ip,t):
  if t=='B':
    ip=ip.replace('.0.0','.a.b')   
  if t=='C':
    ip=re.findall('[0-9]+\.[0-9]+\.[0-9]+\.',ip)[0]+'b'
  return ip

def wilcard(mascara):
  picadillo=mascara.split('.')
  lista=list()
  for seg in picadillo:
      lista.append(str(255-int(seg)))
  return '.'.join(lista)


 