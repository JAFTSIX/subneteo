# subneteo
programa de comandos para subnetear y pasar cisco mas facil

la misión de este programa es subnetear redes de tipo b y c.

para subnetear con comandos es así

su b ip:140.20.0.0 LNS 6000,4000,2000,1000
traducción
(subnetea   una red tipo b    con esta ip    y todas estas lanes       )
  su        b                 ip:140.20.0.0 LNS 6000,4000,2000,1000

eso daría el siguiente resultado

{'id': 1, 'red': '140.20.0.0', 'primera': '140.20.0.1', 'ultima': '140.20.31.254',
'broad': '140.20.31.255', 'mascara': '255.255.224.0', 'wil': '0.0.31.255'}


{'id': 2, 'red': '140.20.32.0', 'primera': '140.20.32.1', 'ultima': '140.20.47.254',
'broad': '140.20.47.255', 'mascara': '255.255.240.0', 'wil': '0.0.15.255'}


{'id': 3, 'red': '140.20.48.0', 'primera': '140.20.48.1', 'ultima': '140.20.55.254',
'broad': '140.20.55.255', 'mascara': '255.255.248.0', 'wil': '0.0.7.255'}


{'id': 4, 'red': '140.20.56.0', 'primera': '140.20.56.1', 'ultima': '140.20.59.254', 
'broad': '140.20.59.255', 'mascara': '255.255.252.0', 'wil': '0.0.3.255'}






