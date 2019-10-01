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


def Crear_Diccionario_de_Localidades(Diccionario,ListaDeNombres):
    DiccionarioLocalidades = dict()
    for Nombre in ListaDeNombres:
        DiccionarioLocalidades[Diccionario[Nombre][0]] += [(Nombre,[Diccionario[Nombre][1]],[Diccionario[Nombre][2]],[Diccionario[Nombre][3]])]
    return DiccionarioLocalidades

def Crear_ListaDeDato(ListaDePersonas, Dato):
    ListaDeDato = []
    if Dato == "Nombre":
        for [Nombre,Apellido, Localidad, Edad, Sexo, Sexualidad] in ListaDePersonas:
            ListaDeDato += [Nombre + " " + Apellido]
        return ListaDeDato
    elif Dato == "Localidad":
        for [Nombre, Apellido,Localidad, Edad, Sexo, Sexualidad] in ListaDePersonas:
            if Localidad not in ListaLocalidades:
                ListaDeDato += [Localidad]
        return ListaDeDato
    
def SepararPor (Lista, Dato):
    if Dato == "Edad":
        NuevaLista = []
        Lista15 = []
        Lista17 = []
        Lista18 = []
        for Persona in Lista:
            if int(Persona[1]) < 15:
                Lista15 += [Persona]
            elif int(Persona[1]) < 18:
                Lista17 += [Persona]
            else:
                Lista18 += [Persona]
        return NuevaLista = [Lista15] + [Lista17] + [Lista18]
    
    elif Dato == "Sexo":
        NuevaLista = []
        HombresHetero = []
        MujerHetero = []
        HombreHomo= []
        MujerHomo = []
        HombreBi = []
        MujerBi = []
        
        for Persona in Lista:
            if Persona[2] == "M" and Persona[3] == "F":
                HombresHetero += [Persona]
            elif Persona[2] == "F" and Persona[3] == "M":
                MujerHetero += [Persona]
            elif Persona[2] == "M" and Persona[3] == "M":
                HombresHomo += [Persona]
            elif Persona[2] == "F" and Persona[3] == "F":
                MujerHomo += [Persona]
            elif Persona[2] == "M" and Persona[3] == "A":
                HombresBi += [Persona]
            else:
                MujerBi += [Persona]

        return NuevaLista = [HombresHetero] + [MujerHetero] + [HombreHomo] + [MujerHomo] + [HombreBi] + [MujerBi]
    
def Descartados (Diccionario,ListaDeNombres, Tipo):
    ListaDeTipo = []
    if Tipo == "Menores":
        for Nombre in ListaDeNombres:      
            if int(Diccionario[Nombre][1]) <= 10:
                ListaDeTipo += [Nombre]
        return ListaDeTipo
    elif Tipo == "Asexuales":
        for nombres in ListaDeNombres:
            if Diccionario[nombres][3]== "N":
                ListaDeTipo += [nombres]
        return ListaDeTipo

#def Matching(Diccionario,Lista):
    #Rosario": [(blasito, 17, M, F),(castre,14, m, f)]
    # Tener en cuenta el caso de una localidad con una unica persona en ella
    
    """"for Localidad in Lista:
    Diccionario[Localidad] = SepararPorEdades(Diccionario[Localidad])
    """


def Match (): #FUNCION PRINCIPAL
    f = open("testeo.txt","r",encoding="latin1") #Archivo de entrada
    Lista_de_Personas = list(map(NormalizarString,(map(lambda x: x.split(","),f.readlines()))))
    f.close()
    Diccionario_de_Personas = Crear_DiccionarioDePersonas(Lista_de_Personas)
    Lista_De_Nombres = Crear_ListaDeDato(Lista_de_Personas,"Nombre")
    Menores_de_edad = Descartados(Diccionario_de_Personas,Lista_De_Nombres,"Menores")
    Asexuales = Descartados(Diccionario_de_Personas,Lista_De_Nombres,"Asexuales")
    Candidatos = QuitarPersonas(Lista_De_Nombres,Menores_de_edad+Asexuales)
    #Parejas = Matching(Crear_Diccionario_de_Localidades(Diccionario,Candidatos),Crear_ListaDeDato(Lista_de_Personas))
    """ArchivoNoparejas = open("solterones.txt","a")
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser menores de 10 años")
    ArchivoNoparejas.writelines(Menores_de_edad)
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser asexuales")
    ArchivoNoparejas.writelines(Asexuales)"""
    

Match()
