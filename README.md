# subneteo

*leelo en RAW o no se entenderá*

programa de comandos para subnetear y trabajar el cisco packet tracer más fácil

la misión de este programa es subnetear redes de tipo b y c.

para subnetear con comandos es así:

su b ip:140.20.0.0 LNS 6000,4000,2000,1000

traducción

(subnetea   una red tipo b    con esta ip    y todas estas lanes       )

  su        b                 ip:140.20.0.0 LNS 6000,4000,2000,1000
  

si quieres algo tecnico, tengo la expresion regular con la que trabaja 

  ^\s*SU\s+(B|C)\s*IP:\s*([0-9]{,3}(.)){3}[0-9]{,3}\s*(LNS)\s*([0-9]*(,))*[0-9]*$  
  
si corres esto: su b ip:140.20.0.0 LNS 6000,4000 

eso daría el siguiente resultado

{'id': 1, 'red': '140.20.0.0', 'primera': '140.20.0.1', 'ultima': '140.20.31.254',
'broad': '140.20.31.255', 'mascara': '255.255.224.0', 'wil': '0.0.31.255'}


{'id': 2, 'red': '140.20.32.0', 'primera': '140.20.32.1', 'ultima': '140.20.47.254',
'broad': '140.20.47.255', 'mascara': '255.255.240.0', 'wil': '0.0.15.255'}

 


ahora, hay funciones extra para trabajar en packet tracer más rápido (creeme te ahorrarán el tiempo)

FUNCIONES PARA PACKET TRACER #1 hacer vlans


para crear vlans con comandos es así:

VL FA0/1_GB0/2 !N:10 R:3-10 !N:20 R:12-30       

traducción

(crea una vlan  que va de el puerto del switch al puerto del router      

VL              FA0/1_GB0/2           

   nombre de la vlan:10 ,  rango:los puertos del 3 al 10 )
   
!  N:10                    R:3-10 

si se quiere que nos de los códigos ocupa el router, primero hay que subnetear,

y el comando cambia solo al final asi

nombre de la vlan:10 ,  rango:los puertos del 3 al 10  con la ip subneteada que tiene el id de 2)

!N:20                    R:12-30                       ID:2     





