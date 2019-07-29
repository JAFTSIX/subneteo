import sub




def vlan(numero,rango):
  
  comando=' vlan $numero \n name vlan$numero \n ex \n inter range fa0/$rango \n switchport mode access \n switchport access vlan $numero \n ex'; 
  comando=comando.replace('$numero',numero)
  comando=comando.replace('$rango',rango)
  return comando


def switch(alrou,alsw,vlans,ides):
  
  print('ena \nconf  term')
  for lanes in vlans:
      print(vlan(lanes['num'],lanes['rango']))
  alf='int $alrouter \nswitchport mode access \nsw mod tru \nexit'.replace('$alrouter',alrou)
  print(alf)
 
  if sub.red and ides:
        print('')
        print('********************** esto en el router, joven')
        print('')
        router_A_vlan(alsw,ides,sub.red,vlans)
  else:
        print("subnetea algo, y te daré los comandos del router")
        

   



def router_A_vlan(alsw,ides,red,vlans ):
  print(" ena \n conf term \n int $alsw \n no ip ad \n no shu \n ex".replace('$alsw',alsw))
  
  
  tuplas=list()
  ides_cpy=ides
  for lan  in  vlans:
    for idi in ides_cpy:
       tuplas.append( (lan,idi,devolver_red(idi,red)) )
       ides_cpy.remove(idi)

  for lan,idi,red in tuplas: 
     print("int $alsw.$nom_vlan".replace('$alsw',alsw).replace('$nom_vlan',lan['num'])) 
     print("en d $nom_vlan".replace('$nom_vlan',lan['num']))
     print("ip ad $red $mascara".replace('$red',red['primera']).replace('$mascara',red['mascara']))
     print("ex")
  
  

	
def devolver_red(ide,redes):
  
  for red in redes:
    if red['id'] ==  int(ide):
       return  red



#P1==[({'num': '10', 'rango': '3-10'}, {'num': '20', 'rango': '12-30'}), ('1', '2')]
#[
 # ({'num': '10', 'rango': '3-10'}, '1', {'id': 1, 'red': '190.123.2.0', 'primera': '190.123.2.0', 'ultima': '190.123.2.0', 'broad': '190.123.2.0', 'mascara': '255.255.248.0'})]