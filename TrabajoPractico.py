#   Esta funcion quita los espacios y los enter de los datos (strings) individuales de cada persona.
#   Devuelve la lista con los strings sin los espacios necesarios
def NormalizarString(Lista):
    NuevaLista = []
    for x in Lista:
        x = x.strip()
        NuevaLista += [x]
    return NuevaLista
""" Tomas un diccionario y una lista que sus elementos son keys del diccionario, elimina esos elementos del diccionario.
    Devuelve el diccionario sin esos elementos"""
def EliminarDelDiccionario(Diccionario,Lista_a_sacar):
    for Persona in Lista_a_sacar:
        del Diccionario[Persona]
    return Diccionario
"""Toma una lista de lista de la forma [Nombre,Apellido,Localidad,Edad,Genero,Interes] y crea un diccionario
    donde las keys son Nombre y Apellido y los valores asociados son tuplas de la forma (Localidad, Edad, Genero, Interes)
    Retorna el diccionario"""
def Crear_DiccionarioDePersonas (lista):
    NuevoDiccionario = dict()
    for [Nombre,Apellido,Localidad,Edad,Genero,Interes] in lista:
        NuevoDiccionario[Nombre + " " + Apellido] = (Localidad, Edad, Genero, Interes)
    return NuevoDiccionario

"""Toma un diccionario existentex crea otro diccionario donde las keys son Localidades y sus valores una lista de tuplas de la forma 
    (Nombre, Edad, Genero, Interes)"""
def Crear_Diccionario_de_Localidades(Diccionario):
    DiccionarioLocalidades = dict()
    for Nombre in Diccionario.keys():
        if Diccionario[Nombre][0] in DiccionarioLocalidades.keys():
            DiccionarioLocalidades[Diccionario[Nombre][0]] += [(Nombre,Diccionario[Nombre][1],Diccionario[Nombre][2],Diccionario[Nombre][3])]
        else:
            DiccionarioLocalidades[Diccionario[Nombre][0]] = [(Nombre,Diccionario[Nombre][1],Diccionario[Nombre][2],Diccionario[Nombre][3])]
    return DiccionarioLocalidades
"""Toma un diccionario, un archivo, una lista de nombre que son keys del diccionario y una razon de escritura.
    Escribe sobre el archivo todos los datos de las persona de la lista"""
def EscribirNoPareja (Archivo_a_Escribir,Diccionario,ListaDeNombres,Razon):
    if Razon == "Menores":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif Razon == "Asexuales":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser asexuales\n")
    elif Razon == "Solos":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja en su localidad\n")
    elif Razon == "Unicos":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja por ser las unicas en su localidad\n")
    for Nombre in ListaDeNombres:
        Archivo_a_Escribir.write("{0}, {1}, {2}, {3}, {4}\n".format(Nombre,Diccionario[Nombre][1],Diccionario[Nombre][2],Diccionario[Nombre][3],Diccionario[Nombre][0]))

def EscribirParejas (Archivo,Persona1,Persona2,Localidad):
    Archivo.write("{0}, {1}, {2}, {3} -- {4}, {5}, {6}, {7} -- {8}\n".format(Persona1[0],Persona1[1],Persona1[2],Persona1[3], Persona2[0],Persona2[1],Persona2[2],Persona2[3],Localidad))


"""Recibe una lista de tupla y forma una lista de lista segun el Dato.
    Si el Dato es Edad, crea una lista de 3 listas donde cada una representa un grupo etario
    la primera de 11 a 14 años, la segunda de 15 a 17 años y la tercera de 18 años en adelante
    Si el Dato es Sexo, crea una lista de 6 listas donde cada representa a un genero y su interes
    La primera son Hombres Heterosexules, la segundd mujeres heteros sexuales
    la tercera hombres homosexuales, la cuarta mujeres homosexuales
    la quinta hombres bisexuales, la sexta mujeres bisexuales"""
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
        return [Lista15] + [Lista17] + [Lista18]
    
    elif Dato == "Genero":
        HombresHetero = []
        MujeresHetero = []
        HombresHomo= []
        MujeresHomo = []
        HombresBi = []
        MujeresBi = []
        for Persona in Lista:
            if Persona[2] == "M" and Persona[3] == "F":
                HombresHetero += [Persona]
            elif Persona[2] == "F" and Persona[3] == "M":
                MujeresHetero += [Persona]
            elif Persona[2] == "M" and Persona[3] == "M":
                HombresHomo += [Persona]
            elif Persona[2] == "F" and Persona[3] == "F":
                MujeresHomo += [Persona]
            elif Persona[2] == "M" and Persona[3] == "A":
                HombresBi += [Persona]
            else:
                MujeresBi += [Persona]
        return [HombresHetero] + [MujeresHetero] + [HombresHomo] + [MujeresHomo] + [HombresBi] + [MujeresBi]

"""Recibe un diccionario y una condicion de descarte, devuelve la lista de nombres de personas que cumplan con la condicion"""    
def Descartados (Diccionario,Condicion):
    ListaDeTipo = []
    if Condicion == "Menores":
        for Nombre in Diccionario.keys():      
            if int(Diccionario[Nombre][1]) <= 10:
                ListaDeTipo += [Nombre]
        return ListaDeTipo
    elif Condicion == "Asexuales":
        for nombres in Diccionario.keys():
            if Diccionario[nombres][3]== "N":
                ListaDeTipo += [nombres]
        return ListaDeTipo

def MatchearHeterosexuales (lista1,lista2,localidad):
    ParejasFile = open("SalidaParejas.txt","a")
    while lista1!=[] and lista2!=[]:
        EscribirParejas(ParejasFile,lista1[0],lista2[0],localidad)
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
    ParejasFile.close()

def MatchearHomosexuales (lista, localidad):
    ParejasFile = open("SalidaParejas.txt","a")
    while lista != [] and len(lista)!= 1:
        EscribirParejas (ParejasFile,lista[0],lista[1],localidad)
        lista.remove(lista[0])
        lista.remove(lista[0])
    ParejasFile.close()

def Matching(Diccionario):
    PersonasUnicas = []
    for Localidad in Diccionario.keys():
        if len(Diccionario[Localidad]) == 1:
            Persona = Diccionario[Localidad][0]
            PersonasUnicas += [Persona[0]]
        else:
            ListaPorEdades = SepararPor(Diccionario[Localidad],"Edad")
            ListaPorEdades_Y_Sexo = []
            for Edad in ListaPorEdades:
                ListaPorEdades_Y_Sexo += [SepararPor(Edad,"Genero")]
            for listaEdad in ListaPorEdades_Y_Sexo:
                MatchearHeterosexuales(listaEdad[0],listaEdad[1],Localidad)
                MatchearHomosexuales(listaEdad[2],Localidad)
                MatchearHomosexuales(listaEdad[3],Localidad)
    return PersonasUnicas

 #FUNCION PRINCIPAL
def Match ():
    f = open("ejemplo1.txt","r",encoding="latin1") #Archivo de entrada
    Lista_de_Personas = list(map(NormalizarString,(map(lambda x: x.split(","),f.readlines()))))
    f.close()
    Diccionario_de_Personas = Crear_DiccionarioDePersonas(Lista_de_Personas)
    Menores_de_Edad = Descartados(Diccionario_de_Personas,"Menores")
    Asexuales = Descartados(Diccionario_de_Personas,"Asexuales")
    NoParejasFile = open("SalidaNoParejas.txt","w")
    EscribirNoPareja(NoParejasFile,Diccionario_de_Personas,Menores_de_Edad,"Menores")
    EscribirNoPareja(NoParejasFile,Diccionario_de_Personas,Asexuales,"Asexuales")
    Diccionario_de_Personas = EliminarDelDiccionario(Diccionario_de_Personas,Menores_de_Edad+Asexuales)
    DiccionarioPorLocalidades = Crear_Diccionario_de_Localidades(Diccionario_de_Personas)
    Unicos = Matching(DiccionarioPorLocalidades)
    EscribirNoPareja(NoParejasFile,Diccionario_de_Personas,Unicos,"Unicos")
    NoParejasFile.close()
Match()
