from TrabajoPractico import *


def test_Pasar_a_Tupla ():
    listaejemplo1=[['JOSE', ' DELGADO', ' SANTA ANA', '  52', ' M', ' A\n'], ['CARMEN', ' CORRALES', ' GOICOECHEA', '  32', ' F', ' M\n']]
    listaejemplo2=[['RAFAEL', ' AGUERO', ' CENTRAL', '  72', ' M', ' F\n'], ['MARTA', ' VILLALTA', ' GOICOECHEA', '  71', ' F', ' F\n']]
    listaejemplo3=[['MANUEL', ' DELGADO', ' PURISCAL', '  66', ' M', ' N\n'], ['MARIA', ' SALAS', ' ATENAS', '  42', ' F', ' N\n'], ['ISABEL', ' VEGA', ' GOICOECHEA', '  73', ' F', ' N']]
    listaresultado1=[('JOSE DELGADO', 'SANTA ANA', '52', 'M', 'A'), ('CARMEN CORRALES', 'GOICOECHEA', '32', 'F', 'M')]
    listaresultado2=[('RAFAEL AGUERO', 'CENTRAL', '72', 'M', 'F'), ('MARTA VILLALTA', 'GOICOECHEA', '71', 'F', 'F')]
    listaresultado3=[('MANUEL DELGADO', 'PURISCAL', '66', 'M', 'N'), ('MARIA SALAS', 'ATENAS', '42', 'F', 'N'), ('ISABEL VEGA', 'GOICOECHEA', '73', 'F', 'N')]
    assert Pasar_a_Tupla(listaejemplo1) == listaresultado1
    assert Pasar_a_Tupla(listaejemplo2) == listaresultado2
    assert Pasar_a_Tupla(listaejemplo3) == listaresultado3

def test_Crear_Diccionario_de_Localidades ():
    ListaTuplaEjemplo1 = [('JOSE DELGADO', 'SANTA ANA', '52', 'M', 'A'), ('CARMEN CORRALES', 'GOICOECHEA', '32', 'F', 'M'),('RAFAEL AGUERO', 'CENTRAL', '72', 'M', 'F'), ('MARTA VILLALTA', 'GOICOECHEA', '71', 'F', 'F')]
    ListaTuplaEjemplo2 = [('JOSE DELGADO', 'SANTA ANA', '52', 'M', 'A'), ('CARMEN CORRALES', 'SANTA ANA', '32', 'F', 'M'),('RAFAEL AGUERO', 'SANTA ANA', '72', 'M', 'F')]
    DiccionarioResultado1 = {"SANTA ANA":[("JOSE DELGADO","52","M","A")],"GOICOECHEA":[("CARMEN CORRALES","32","F","M"),("MARTA VILLALTA","71","F","F")],"CENTRAL":[("RAFAEL AGUERO","72","M","F")]}
    DiccionarioResultado2 = {"SANTA ANA":[("JOSE DELGADO","52","M","A"),("CARMEN CORRALES","32","F","M"),("RAFAEL AGUERO","72","M","F")]}
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo1) == DiccionarioResultado1
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo2) == DiccionarioResultado2

def test_SepararPor ():
    ListaEdadesEjemplo1 = [('JOSE DELGADO', '13', 'M', 'A'), ('CARMEN CORRALES','17', 'F', 'M'),('RAFAEL AGUERO','72', 'M', 'F')]
    ListaEdadesEjemplo2 = [('JOSE DELGADO', '13', 'M', 'A'), ('CARMEN CORRALES','14', 'F', 'M'),('RAFAEL AGUERO','12', 'M', 'F')]
    ListaGeneroInteresEjemplo1 = [('JOSE DELGADO', '13', 'M', 'F'), ('CARMEN CORRALES','14', 'F', 'M'),('RAFAEL AGUERO','12', 'M', 'M'),('MANUEL DELGADO', '66', 'M', 'A'), ('MARIA SALAS', '42', 'F', 'F'), ('ISABEL VEGA',  '73', 'F', 'A')]
    ListaGeneroInteresEjemplo2 = [('JOSE DELGADO', '13', 'M', 'M'), ('CARMEN CORRALES','14', 'F', 'A'),('RAFAEL AGUERO','12', 'M', 'M'),('MANUEL DELGADO', '66', 'M', 'A'), ('MARIA SALAS', '42', 'F', 'F'), ('ISABEL VEGA',  '73', 'F', 'A')]
    ListaDeEdadesEsperada1 = [[('JOSE DELGADO', '13', 'M', 'A')],[('CARMEN CORRALES','17', 'F', 'M')],[('RAFAEL AGUERO','72', 'M', 'F')]]
    ListaDeEdadesEsperada2 = [[('JOSE DELGADO', '13', 'M', 'A'),('CARMEN CORRALES','14', 'F', 'M'),('RAFAEL AGUERO','12', 'M', 'F')],[],[]]
    ListaGeneroInteresEsperada1 = [[('JOSE DELGADO', '13', 'M', 'F')],[('CARMEN CORRALES','14', 'F', 'M')],[('RAFAEL AGUERO','12', 'M', 'M')],[('MARIA SALAS', '42', 'F', 'F')],[('MANUEL DELGADO', '66', 'M', 'A')],[('ISABEL VEGA', '73', 'F', 'A')]]
    ListaGeneroInteresEsperada2 = [[],[],[('JOSE DELGADO', '13', 'M', 'M'),('RAFAEL AGUERO','12', 'M', 'M')],[('MARIA SALAS', '42', 'F', 'F')],[('MANUEL DELGADO', '66', 'M', 'A')],[('CARMEN CORRALES','14', 'F', 'A'),('ISABEL VEGA', '73', 'F', 'A')]]
    assert SepararPor(ListaEdadesEjemplo1,"Edad") == ListaDeEdadesEsperada1
    assert SepararPor(ListaEdadesEjemplo2,"Edad") == ListaDeEdadesEsperada2
    assert SepararPor(ListaGeneroInteresEjemplo1,"Genero") == ListaGeneroInteresEsperada1
    assert SepararPor(ListaGeneroInteresEjemplo2,"Genero") == ListaGeneroInteresEsperada2

def test_Descartados ():
    ListaPersonasEjemplo1 = [('JOSE DELGADO', 'SANTA ANA', '9', 'M', 'N'), ('CARMEN CORRALES', 'GOICOECHEA', '32', 'F', 'M'),('RAFAEL AGUERO', 'CENTRAL', '10', 'M', 'F'), ('MARTA VILLALTA', 'GOICOECHEA', '71', 'F', 'N')]
    ListaPersonasEjemplo2 = [('JOSE DELGADO', 'SANTA ANA', '52', 'M', 'A'), ('CARMEN CORRALES', 'GOICOECHEA', '32', 'F', 'M')]
    ListaDescartadosEsperada1 = [('JOSE DELGADO', 'SANTA ANA', '9', 'M', 'N'),('RAFAEL AGUERO', 'CENTRAL', '10', 'M', 'F')]
    ListaDescartadosEsperada2 = []
    ListaDescartadosEsperada3 = [('JOSE DELGADO', 'SANTA ANA', '9', 'M', 'N'),('MARTA VILLALTA', 'GOICOECHEA', '71', 'F', 'N')]
    assert Descartados(ListaPersonasEjemplo1,"Menores") == ListaDescartadosEsperada1
    assert Descartados(ListaPersonasEjemplo2,"Menores") == ListaDescartadosEsperada2
    assert Descartados(ListaPersonasEjemplo1,"Asexuales") == ListaDescartadosEsperada3
    assert Descartados(ListaPersonasEjemplo2,"Asexuales") == ListaDescartadosEsperada2

def test_Matching ():