from TrabajoPractico import *
def Pasar_a_Tupla_test ():
    listaejemplo1=[['JOSE', ' DELGADO', ' SANTA ANA', '  52', ' M', ' A\n'], ['CARMEN', ' CORRALES', ' GOICOECHEA', '  32', ' F', ' M\n']]
    listaejemplo2=[['RAFAEL', ' AGUERO', ' CENTRAL', '  72', ' M', ' F\n'], ['MARTA', ' VILLALTA', ' GOICOECHEA', '  71', ' F', ' F\n']]
    listaejemplo3=[['MANUEL', ' DELGADO', ' PURISCAL', '  66', ' M', ' N\n'], ['MARIA', ' SALAS', ' ATENAS', '  42', ' F', ' N\n'], ['ISABEL', ' VEGA', ' GOICOECHEA', '  73', ' F', ' N']]
    listaresultado1=[('JOSE DELGADO', 'SANTA ANA', '52', 'M', 'A'), ('CARMEN CORRALES', 'GOICOECHEA', '32', 'F', 'M')]
    listaresultado2=[('RAFAEL AGUERO', 'CENTRAL', '72', 'M', 'F'), ('MARTA VILLALTA', 'GOICOECHEA', '71', 'F', 'F')]
    listaresultado3=[('MANUEL DELGADO', 'PURISCAL', '66', 'M', 'N'), ('MARIA SALAS', 'ATENAS', '42', 'F', 'N'), ('ISABEL VEGA', 'GOICOECHEA', '73', 'F', 'N')]
    assert Pasar_a_Tupla(listaejemplo1) == listaresultado1
    assert Pasar_a_Tupla(listaejemplo2) == listaresultado2
    assert Pasar_a_Tupla(listaejemplo3) == listaresultado3
    