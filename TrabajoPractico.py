def NormalizarString(Lista):
    NuevaLista = []
    for x in Lista:
        x = x.strip()
        NuevaLista += [x]
    return NuevaLista

def QuitarPersonas(Diccionario,Lista_a_sacar):
    for Persona in Lista_a_sacar:
        del Diccionario[Persona]
    return Diccionario

def Crear_DiccionarioDePersonas (lista):
    Listadedict= dict()
    for [Nombre,Apellido,Localidad,Edad,Sexo,Sexualidad] in lista:
        Listadedict[Nombre + " " + Apellido]= (Localidad, Edad, Sexo, Sexualidad)
    return Listadedict


def Crear_Diccionario_de_Localidades(Diccionario):
    DiccionarioLocalidades = dict()
    for Nombre in Diccionario.keys():
        DiccionarioLocalidades[Diccionario[Nombre][0]] += [(Nombre,[Diccionario[Nombre][1]],[Diccionario[Nombre][2]],[Diccionario[Nombre][3]])]
    return DiccionarioLocalidades

def Escribir (Diccionario,ListaDeNombres):
    Solterones = open("SalidasNoParejas.txt","w")
    for Nombre in ListaDeNombres:
        Solterones.write("{0}, {1}, {2}, {3}, {4} \n".format(Nombre,Diccionario[Nombre][1],Diccionario[Nombre][2],Diccionario[Nombre][3],Diccionario[Nombre][0]))
    Solterones.close()
   
def SepararPor (Lista, Dato):
    if Dato == "Edad":
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
        return [[Lista15] + [Lista17] + [Lista18]]
    
    elif Dato == "Sexo":
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

        return [[HombresHetero] + [MujerHetero] + [HombreHomo] + [MujerHomo] + [HombreBi] + [MujerBi]]
    
def Descartados (Diccionario,Tipo):
    ListaDeTipo = []
    if Tipo == "Menores":
        for Nombre in Diccionario.keys():      
            if int(Diccionario[Nombre][1]) <= 10:
                ListaDeTipo += [Nombre]
        return ListaDeTipo
    elif Tipo == "Asexuales":
        for nombres in Diccionario.keys():
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
    Menores_de_Edad = Descartados(Diccionario_de_Personas,"Menores")
    Asexuales = Descartados(Diccionario_de_Personas,"Asexuales")
    Escribir(Diccionario_de_Personas,Menores_de_Edad+Asexuales)
    """ArchivoNoparejas = open("SalidaNoParejas.txt","w")
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser menores de 10 años")
    ArchivoNoparejas.writelines(Menores_de_edad)
    ArchivoNoparejas.write("Estas personas no formaron parejas por ser asexuales")
    ArchivoNoparejas.writelines(Asexuales)"""
    #EliminarDelDiccionario(Menores_de_Edad+Asexuales)
    #DiccionarioPorLocalidades = Crear_Diccionario_de_Localidades(Diccionario_de_Personas)
    #Matching(DiccionarioPorLocalidades)

Match()
