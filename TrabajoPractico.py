def NormalizarString(Lista):
    NuevaLista = []
    for x in Lista:
        x = x.strip()
        NuevaLista += [x]
    return NuevaLista

def QuitarPersonas(Lista_de_nombres,Lista_a_sacar):
    Candidatos = []
    for persona in Lista_de_nombres:
        if persona not in Lista_a_sacar:
            Candidatos += [persona]
    return Candidatos

def Crear_DiccionarioDePersonas (lista):
    Listadedict= dict()
    for [Nombre,Apellido,Localidad,Edad,Sexo,Sexualidad] in lista:
        Listadedict[Nombre + " " + Apellido]= (Localidad, Edad, Sexo, Sexualidad)
    return Listadedict

def Crear_ListaDeNombres  (listadelistas):
    listadenombres=[]
    for [Nombre,Apellido, Localidad, Edad, Sexo, Sexualidad] in listadelistas:
        listadenombres += [Nombre + " " + Apellido]
    return listadenombres


def Crear_Diccionario_de_Localidades(Diccionario,ListaDeNombres):
    DiccionarioLocalidades = dict()
    for Nombre in ListaDeNombres:
        DiccionarioLocalidades[Diccionario[Nombre][0]] += [(Nombre,[Diccionario[Nombre][1]],[Diccionario[Nombre][2]],[Diccionario[Nombre][3]])]
    return DiccionarioLocalidades

def Crear_ListaDeLocalidades (ListaDePersonas):
    ListaLocalidades = []
    for [Nombre, Apellido,Localidad, Edad, Sexo, Sexualidad] in ListaDePersonas:
        if Localidad not in ListaLocalidades:
            ListaLocalidades += [Localidad]
    return ListaLocalidades

def PersonasAsexuales (diccionario,listanombres):
    Asexuales = []
    for nombres in listanombres:
        if diccionario[nombres][3]== "N":
            Asexuales += [nombres]
    return Asexuales

def Menores_de_Edad(Dictionario,ListaDeNombres):
    ListaMenores = []
    for Nombre in ListaDeNombres:      
        if int(Dictionario[Nombre][1]) < 10:
            ListaMenores += [Nombre]
    return ListaMenores

def Matching(Diccionario,Lista_de_Nombres):
    Menores_de_edad = Menores_de_Edad(Diccionario,Lista_de_Nombres)
    Asexuales = PersonasAsexuales(Diccionario,Lista_de_Nombres)
    Candidatos = QuitarPersonas(Lista_de_Nombres,Menores_de_edad+Asexuales)
    """ArchivoNoparejas = open("solterones.txt","a")
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser menores de 10 años")
    ArchivoNoparejas.writelines(Menores_de_edad)
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser asexuales")
    ArchivoNoparejas.writelines(Asexuales)"""


def Match (): #FUNCION PRINCIPAL
    f = open("testeo.txt","r") #Archivo de entrada
    Lista_de_Personas = list(map(NormalizarString,(map(lambda x: x.split(","),f.readlines()))))
    f.close()
    Diccionario_de_Personas = Crear_DiccionarioDePersonas(Lista_de_Personas)
    Lista_De_Nombres = Crear_ListaDeNombres(Lista_de_Personas)
    Lista_de_Parejas = Matching(Diccionario_de_Personas,Lista_De_Nombres)
    #print(Diccionario_de_Personas)
    #print(Lista_De_Nombres)

Match()
