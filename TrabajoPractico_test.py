from TrabajoPractico import *

""" El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de una lista de listas, que cada elemento sea un string
    El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de una lista de quintuplas de strings """
def test_Pasar_a_Tupla ():
    EjemplosFile = open("Pasar_a_TuplasEjemplo.txt","r")
    ResultadosFile = open("Pasar_a_TuplasResultado.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    Resultados.close()
    listaejemplo1 = eval(LineasEjemplo[0])
    listaejemplo2 = eval(LineasEjemplo[1])
    listaejemplo3 = eval(LineasEjemplo[2])
    listaresultado1 = eval(LineasResultados[0])
    listaresultado2 = eval(LineasResultados[1])
    listaresultado3 = eval(LineasResultados[2])
    assert Pasar_a_Tupla(listaejemplo1) == listaresultado1
    assert Pasar_a_Tupla(listaejemplo2) == listaresultado2
    assert Pasar_a_Tupla(listaejemplo3) == listaresultado3
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de una lista de quintuplas de strings
   El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de diccionario donde cada key es una localidad y su valor
   asociado es una lista de cuatruplas"""
def test_Crear_Diccionario_de_Localidades ():
    EjemplosFile = open("Crear_Diccionario_de_LocalidadesEjemplos.txt","r")
    ResultadosFile = open("Crear_Diccionario_de_LocalidadesResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    Resultados.close()
    ListaTuplaEjemplo1 = eval(LineasEjemplo[0])
    ListaTuplaEjemplo2 = eval(LineasEjemplo[1])
    DiccionarioResultado1 = eval(LineasResultados[0])
    DiccionarioResultado2 = eval(LineasResultados[1])
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo1) == DiccionarioResultado1
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo2) == DiccionarioResultado2
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de lista de cuatruplas
   El archivo de resultados tiene un resultado por linea, dependiendo del segundo argumento que puede ser "Edad" o "Genero" el resultado debe estar
   """
def test_SepararPor ():
    EjemplosFile = open("SepararPorEjemplos.txt","r")
    ResultadosFile = open("SepararPorResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    Resultados.close()
    ListaEdadesEjemplo1 = eval(LineasEjemplo[0])
    ListaEdadesEjemplo2 = eval(LineasEjemplo[1])
    ListaGeneroInteresEjemplo1 = eval(LineasEjemplo[2])
    ListaGeneroInteresEjemplo2 = eval(LineasEjemplo[3])
    ListaDeEdadesEsperada1 = eval(LineasResultados[0])
    ListaDeEdadesEsperada2 = eval(LineasResultados[1])
    ListaGeneroInteresEsperada1 = eval(LineasResultados[2])
    ListaGeneroInteresEsperada2 = eval(LineasResultados[3])
    assert SepararPor(ListaEdadesEjemplo1,"Edad") == ListaDeEdadesEsperada1
    assert SepararPor(ListaEdadesEjemplo2,"Edad") == ListaDeEdadesEsperada2
    assert SepararPor(ListaGeneroInteresEjemplo1,"Genero") == ListaGeneroInteresEsperada1
    assert SepararPor(ListaGeneroInteresEjemplo2,"Genero") == ListaGeneroInteresEsperada2

def test_Descartados ():
    EjemplosFile = open("Pasar_a_TuplasEjemplo.txt","r")
    ResultadosFile = open("Pasar_a_TuplasResultado.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    Resultados.close()
    ListaPersonasEjemplo1 = eval(LineasEjemplo[0])
    ListaPersonasEjemplo2 = eval(LineasEjemplo[1])
    ListaDescartadosEsperada1 = eval(LineasResultados[0])
    ListaDescartadosEsperada2 = eval(LineasResultados[1])
    assert Descartados(ListaPersonasEjemplo1,"Menores") == ListaDescartadosEsperada1
    assert Descartados(ListaPersonasEjemplo2,"Menores") == []
    assert Descartados(ListaPersonasEjemplo1,"Asexuales") == ListaDescartadosEsperada2
    assert Descartados(ListaPersonasEjemplo2,"Asexuales") == []

def test_Matching ():
    EjemplosFile = open("MatchingEjemplos.txt","r")
    ResultadosFile = open("MatchingResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    Resultados.close()
    DiccionarioEjemplo1 = eval(LineasEjemplo[0])
    DiccionarioEjemplo2 = eval(LineasEjemplo[1])
    ListaResultado1 = eval(LineasResultado[0])
    ListaResultado2 = eval(LineasResultado[1])

    assert Matching(DiccionarioEjemplo1) == ListaResultado1
    assert Matching(DiccionarioEjemplo2) == ListaResultado2
