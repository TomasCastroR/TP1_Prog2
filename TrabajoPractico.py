#   Esta funcion quita los espacios y los enter de los datos (strings) individuales de cada persona.
#   Devuelve la lista con los strings sin los espacios necesarios
def Pasar_a_Tupla(Lista):
    NuevaLista = []
    for [Nombre,Apellido,Localidad,Edad,Genero,Interes] in Lista:
        NuevaLista += [(Nombre.strip()+" "+Apellido.strip(),Localidad.strip(),Edad.strip(),Genero.strip(),Interes.strip())]
    return NuevaLista
""" Tomas un diccionario y una lista que sus elementos son keys del diccionario, elimina esos elementos del diccionario.
    Devuelve el diccionario sin esos elementos"""
def EliminarDeLaLista(ListaPrincipal,Lista_a_sacar):
    for Persona in Lista_a_sacar:
            ListaPrincipal.remove(Persona)

"""Toma un diccionario existentex crea otro diccionario donde las keys son Localidades y sus valores una lista de tuplas de la forma 
    (Nombre, Edad, Genero, Interes)"""
def Crear_Diccionario_de_Localidades(ListaDePersonas):
    DiccionarioLocalidades = dict()
    for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:
        if Localidad in DiccionarioLocalidades.keys():
            DiccionarioLocalidades[Localidad] += [(NombreYApellido,Edad,Genero,Interes)]
        else:
            DiccionarioLocalidades[Localidad] = [(NombreYApellido,Edad,Genero,Interes)]
    return DiccionarioLocalidades
"""Toma un diccionario, un archivo, una lista de nombre que son keys del diccionario y una razon de escritura.
    Escribe sobre el archivo todos los datos de las persona de la lista"""
def EscribirNoPareja (Archivo_a_Escribir,ListaDePersonas,Razon):
    if Razon == "Menores":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif Razon == "Asexuales":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser asexuales\n")
    elif Razon == "Solteros":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja en su localidad\n")
    elif Razon == "Unicos":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja por ser las unicas en su localidad\n")
    for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:
        Archivo_a_Escribir.write("{0}, {1}, {2}, {3}, {4}\n".format(NombreYApellido,Edad,Genero,Interes,Localidad))

"""Recibe el archivo a escribir, dos personas que seran la pareja y su localidad.
    Escribe sobre el archivo la siguiente linea:"""
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
def Descartados (ListaDePersonas,Condicion):
    ListaDeTipo = []
    if Condicion == "Menores":
        for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:      
            if int(Edad) <= 10:
                ListaDeTipo += [(NombreYApellido,Localidad,Edad,Genero,Interes)]
        return ListaDeTipo
    elif Condicion == "Asexuales":
        for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:
            if Interes == "N":
                ListaDeTipo += [(NombreYApellido,Localidad,Edad,Genero,Interes)]
        return ListaDeTipo
"""Recibe un Archivo, dos listas de Genero e Interes y la localidad donde se encuentra.
    Empareja los primeros elementos de cada lista escribiendolos sobre el archivo y luego
    los elimina de las respectivas listas"""
def MatchearHeterosexuales (Archivo,lista1,lista2,localidad):
    while lista1!=[] and lista2!=[]:
        EscribirParejas(Archivo,lista1[0],lista2[0],localidad)
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
"""Recibe un archivo, una lista de Genero e Interes y la localidad donde se encuentra.
    Empareja el primer elemento con el siguiente escribiendolos sobre el archivo y luego
    los elimina de la lista"""
def MatchearHomosexuales (Archivo,lista, localidad):
    while lista != [] and len(lista)!= 1:
        EscribirParejas (Archivo,lista[0],lista[1],localidad)
        lista.remove(lista[0])
        lista.remove(lista[0])
"""Recibe un diccionario de Localidades. Luego, por cada Localidad, separa por edades en 3 listas y a cada
    grupo etario en 6 listas de Genero e Interes. Despues, forma las parejas.
    Al mismo tiempo, forma una lista de dos listas donde la primera contiene todos los nombres de las personas
    que estan solas en su localidad y la otra, los nombres de las personas que no pudieron formar pareja.
    Retorna esa lista"""
def Matching(Diccionario):
    PersonasUnicas = []
    PersonasSolteras = []
    ParejasFile = open("SalidaParejas.txt","w")
    for Localidad in Diccionario.keys():
        if len(Diccionario[Localidad]) == 1:
            Persona = Diccionario[Localidad][0]
            PersonasUnicas += [(Persona[0],Localidad,Persona[1],Persona[2],Persona[3])]
        else:
            ListaPorEdades = SepararPor(Diccionario[Localidad],"Edad")
            ListaPorEdades_Y_Sexo = []
            for Edad in ListaPorEdades:
                ListaPorEdades_Y_Sexo += [SepararPor(Edad,"Genero")]
            for listaEdad in ListaPorEdades_Y_Sexo:
                MatchearHeterosexuales(ParejasFile,listaEdad[0],listaEdad[1],Localidad) #Primero se matchea hombres hetero con mujeres hetero
                MatchearHomosexuales(ParejasFile,listaEdad[2],Localidad)#Match de hombres homosexuales
                MatchearHomosexuales(ParejasFile,listaEdad[3],Localidad)#Match de mujeres homosexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[0],listaEdad[5],Localidad)#Match de los hombres hetero que no pudieron formar pareja con mujeres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[1],listaEdad[4],Localidad)#Match de las mujeres hetero que no pudieron formar pareja con hombres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[2],listaEdad[4],Localidad)#Match de los hombres homosexuales que no pudieron formar pareja con hombres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[3],listaEdad[5],Localidad)#Match de los mujeres homosexuales que no pudieron formar pareja con mujeres bisexuales
                BisexualesRestantes = listaEdad[4]+listaEdad[5] #Bisexuales que todavia no formaron pareja
                MatchearHomosexuales(ParejasFile,BisexualesRestantes,Localidad)#Match personas bisexuales
                for Persona in listaEdad[0] + listaEdad[1] + listaEdad[2] + listaEdad[3] + BisexualesRestantes:
                    PersonasSolteras += [(Persona[0],Localidad,Persona[1],Persona[2],Persona[3])]
                   
    ParejasFile.close()
    return [PersonasUnicas]+ [PersonasSolteras]
                
#FUNCION PRINCIPAL
def Match ():
    EntradaFile = open("ejemplo2.txt","r",encoding="latin1") #Archivo de entrada
    Lista_de_Personas = Pasar_a_Tupla(list(map(lambda x: x.split(","),EntradaFile.readlines())))
    EntradaFile.close()
    NoParejasFile = open("SalidaNoParejas.txt","w")
    Menores_de_Edad = Descartados(Lista_de_Personas,"Menores")
    EscribirNoPareja(NoParejasFile,Menores_de_Edad,"Menores")
    EliminarDeLaLista(Lista_de_Personas,Menores_de_Edad)
    Asexuales = Descartados(Lista_de_Personas,"Asexuales")
    EscribirNoPareja(NoParejasFile,Asexuales,"Asexuales")
    EliminarDeLaLista(Lista_de_Personas,Asexuales)
    DiccionarioPorLocalidades = Crear_Diccionario_de_Localidades(Lista_de_Personas)
    NoParejas = Matching(DiccionarioPorLocalidades)
    EscribirNoPareja(NoParejasFile,NoParejas[0],"Unicos")
    EscribirNoPareja(NoParejasFile,NoParejas[1],"Solteros")
    NoParejasFile.close()

Match()
