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
            DiccionarioLocalidades[Diccionario[Nombre][0]] += [(Nombre,[Diccionario[Nombre][1]],[Diccionario[Nombre][2]],[Diccionario[Nombre][3]])]
        else:
            DiccionarioLocalidades[Diccionario[Nombre][0]] = [(Nombre,[Diccionario[Nombre][1]],[Diccionario[Nombre][2]],[Diccionario[Nombre][3]])]
    return DiccionarioLocalidades
"""Toma un diccionario, una lista de nombre que son keys del diccionario y una razon de escritura.
    Escribe sobre el archivo SalidaNoPareja.txt todos los datos de las persona de la lista"""
def Escribir (Diccionario,ListaDeNombres,Razon):
    Solterones = open("SalidaNoParejas.txt","w+")
    if Razon == "Menores":
        Solterones.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif Razon == "Asexuales":
        Solterones.write("Estas personas no formaron parejas por ser asexuales\n")
    for Nombre in ListaDeNombres:
        Solterones.write("{0}, {1}, {2}, {3}, {4} \n".format(Nombre,Diccionario[Nombre][1],Diccionario[Nombre][2],Diccionario[Nombre][3],Diccionario[Nombre][0]))
    Solterones.close()
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
        return [[Lista15] + [Lista17] + [Lista18]]
    
    elif Dato == "Genero":
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

def machearhetero (lista1,lista2,localidad):
    while lista1!=[] and lista2!=[]:
        escribirpareja(lista1[0],lista2[0],localidad)
        lista1.remove(list1[0])
        lista2.remove(lista2[0])
    
def machearhomos (lista, localidad):
    while lista != [] and len(list)!= 1:
        escribirpareja (lista[0],lista[1],localidad)
        lista.remove(lista[0])
        lista.remove(lista[1])

def Matching(Diccionario):
    for localidades in Diccionario.keys:
        ListaPorEdades = SepararPor(Diccionario[Localidad],"Edad")
        ListaPorEdades_Y_Sexo = []
        for Edad in ListaPorEdades:
            ListaPorEdades_Y_Sexo += [SepararPor(Edad,"Sexo")]
        for listaEdad in ListaPorEdades_Y_Sexo:
            machearhetero(listaEdad[0],listaEdad[1],localidad)
            machearhomos(listaEdad[2])
            machearhomos(listaEdad[3])


    #Rosario": [(blasito, 17, M, F),(castre,14, m, f)]
    # Tener en cuenta el caso de una localidad con una unica persona en ella
    
    """"for Localidad in Lista:
    Diccionario[Localidad] = SepararPorEdades(Diccionario[Localidad])
    """

 #FUNCION PRINCIPAL
def Match ():
    f = open("testeo.txt","r",encoding="latin1") #Archivo de entrada
    Lista_de_Personas = list(map(NormalizarString,(map(lambda x: x.split(","),f.readlines()))))
    f.close()
    Diccionario_de_Personas = Crear_DiccionarioDePersonas(Lista_de_Personas)
    Menores_de_Edad = Descartados(Diccionario_de_Personas,"Menores")
    Asexuales = Descartados(Diccionario_de_Personas,"Asexuales")
    Escribir(Diccionario_de_Personas,Menores_de_Edad,"Menores")
    Escribir(Diccionario_de_Personas,Asexuales,"Asexuales")
    Diccionario_de_Personas = EliminarDelDiccionario(Diccionario_de_Personas,Menores_de_Edad+Asexuales)
    DiccionarioPorLocalidades = Crear_Diccionario_de_Localidades(Diccionario_de_Personas)
    #Matching(DiccionarioPorLocalidades)

Match()
