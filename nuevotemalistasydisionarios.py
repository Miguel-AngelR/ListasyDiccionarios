# -*- coding: utf-8 -*-
"""NuevoTemaListasyDisionarios.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vp9_XRDaPsrF_Xd4rltatswShJL6No00

# Listas y Diccionarios - TIpos de Datos Complejos

##Datos Simples

.Cadena - Strings

.Enteros - int

.Decimales - float

.Booleano - True OR(o) false  

## Datos Complejos
Nos permiten almacenar multiples valores a la vez.

Listas - Arrays

Es una coleccion ordenada de elementos, los cuales puede modificar, agregar y eliminar.

Manzanas, Peras, Leche, Carne, Pollo -> "
 0     ,   1   ,    2  ,   3  ,    4"


 Diccionarios - Objetos

¿Que son los diccionarios?

Es una coleccion de datos desordenada, almacenada con claver - valor.

Ejemplo:

clave ---------- valor

Paula:----3014567898

Pedro:----3105678998

Carlos:---3155874569
"""

#Lista

frutas=["Madre", "Padre", "Hijo", "Tio", "Animalitos"]
print(frutas[0]) # Acceder un elemento de la lista

frutas[2]="Miguel angel" # Modificar un elemento de la lista
print(frutas[2])

frutas[4]="Caninos y felinos" # Modificar un elemento de la lista
print(frutas[4])



frutas.append("Hija") #append() me permite agregar un elemento a lista, en la ultima posicion


frutas.pop() #Elimina el ultimo elemento de la lista

frutas.remove("Miguel angel") # Elimina un elemtno de la lista

print(*frutas) # Muestra toda la lista de fruta, " * " quita los simbolos de la lista

print(len(frutas)) # Longitud de la lista

# Diccionario

contactos= {

            "Pedro El escamoso" :  "310-856-7898",
            "Maria" : "315-756-8954",
            "Carlos ivan duque" : "315-523-4574"
}

print("El contacto de maria es:", contactos["Maria"]) # llamos un elemento por medio de su clave
print("El contacto de Pedro es:", contactos["Pedro El escamoso"])
print("El contacto de Carlos es:", contactos["Carlos ivan duque"])

contactos["Camilita"]="310-567-7458" # Agregando un nuevo contacto al diccionario
print(contactos)

contactos["Maria"]="555-555-555" # modificar
del contactos["Carlos ivan duque"] #Eliminar un contacto

print(contactos)

"""## Ejercicio 1: Lista de tareas

1. Crea una lista de tareas con al menos 5 elementos.
2. Modificar una de las tareas
3. Elimina la ultima tarea de la lista
4. Agrega una nueva tarea

## Dicionario de productos

1. Crea un diccionario que almacene nombre de productos y sus precios.
2. Modificar el precio de uno de los productos.
3. Agrega un nuevo productos al diccionario.
4. Elimina un prodcuto del diccionario



"""

#Lista de tareas

Tareas=[
    "Matematicas",
    "Castellano",
    "Naturales",
    "Historia",
    "Filosofia"
    ]
Tareas[2]="Lenguaje" # Modificar un elemento de la lista
print(frutas[2])
Tareas.pop()
Tareas.append("Educacion fisica")
print(Tareas)

#Diccionario de productos

DULCES= {

            "Bombom" :  "600",
            "Papas Margarita" : "3,000",
            "Torta" : "5,000",
            "Bomyur" : "7,000"
}

DULCES["Bomyur"]="8,000"
DULCES["Paletas"]="2,000"
del DULCES["Torta"]
print(*DULCES.keys(), *DULCES.values()) # keys - clave = te muestre todas las clases, values() - muestr solo los valores
print(DULCES)

contactos = {
    "Miguel Angel" : {
        "Telefono" : ["315-456-8925",3107568974],
        "Correo" : ["miguelangel@gmail.com","angel@gmail.com", "Miangel@gmail.com" ],
        "Direccion" : {
            "Calle" : "3A",
            "Barrio" : "Principe",
            "Ciudad" : "Tulua"
        }
    }, # TAREA AGREGAR OTROS DOS CONTACTOS AL CODIGO
    "Sofia" : {
        "Telefono" : ["318-434-5645",3147548575],
        "Correo" : "sofiacob@gmail.com",
        "Direccion" : {
            "Carrera" : "3A",
            "Barrio" : "Albernia",
            "Ciudad" : "Tulua"
        }
    },
     "Estefania" : {
        "Telefono" : ["317-242-2574",3132573814],
        "Correo" : "Estefany@gmail.com",
        "Direccion" : {
            "Calle" : "22",
            "Barrio" : "san pedro claver",
            "Ciudad" : "Tulua"
        }
    },
}


contactos["Anna"]={
     "Telefono" : ["313-777-8812", 312345678],
     "Correo" : "Anna@gamil.com",
     "Direccion" : {
         "calle" : "2B",
         "Barrio" : "farfan",
         "Ciudad": "Pueblo nuevo"
     }
}

contactos["Tatiana"]={
     "Telefono" : ["323-777-8812", "315375878", "234567832"],
     "Correo" : "tatianaRP@gamil.com",
     "Direccion" : {
         "calle" : "2B",
         "Barrio" : "albernia",
         "Ciudad": "tulua"
     }
  }
contactos["Pedro"]={
     "Telefono" : ["323-777-8812", "315375878", "234567832"],
     "Correo" : "tatianaRP@gamil.com",
     "Direccion" : {
         "calle" : "2B",
         "Barrio" : "albernia",
         "Ciudad": "tulua"
     }
  }

print(*contactos)
print("El telefono de Miguel Angel es:", contactos["Miguel Angel"]["Telefono"])
print("El segundo telefono de tatiana es:", contactos["Tatiana"]["Telefono"][1])
print("La direccion  de Miguel angel es:", contactos["Miguel Angel"]["Direccion"])
print("La ciudad de Migue angel es:", contactos["Miguel Angel"]["Direccion"]["Ciudad"])

CiudadMiguel = contactos["Miguel Angel"]["Direccion"]["Ciudad"] #Puedo guardarlo en una variable
print("La ciudad donde esta ubicado Miguel angel es:", CiudadMiguel)

CorreoMiguel = contactos ["Miguel Angel"]["Correo"]
print("El correo de Miguel angel es:", CorreoMiguel)

TelefonoTatiana = contactos["Tatiana"]["Telefono"] #Guarde los telefonos de tatiana en una variable
print("los telefonos de tatiana son:", TelefonoTatiana)

# For variable/contador = 0 in limite (<11) "IN = En(vaya) "

for Telefono in TelefonoTatiana: # Telefono[0], Telefono[1], Telefono[2]
 print(Telefono)

for i, Telefono in enumerate(TelefonoTatiana, start=1): # Enumerate es una funcion que agrega Un
                                                        # Contador/indice a cada elemento, start le indicamos desde que
                                                        # numero va empezar a contar
  print(f"Telefono ({i}) es:", Telefono)

for i, Correo in enumerate(CorreoMiguel, start=1):
   print(f"Los correo son ({i}) es:",Correo)


contactos["Miguel Angel"]["Cumpleaños"]="19 de Junio"  # Agrega una clave o campo nuevo como andres
print("El compleaños de Miguel es",contactos["Miguel Angel"]["Cumpleaños"])

contactos["Miguel Angel"]["Fech nacimniento"]=[19,"Junio",2004] # Agregar fecha de nacimiento
print("La fecha de nacimiento de Miguel es", *contactos["Miguel Angel"]["Fech nacimniento"])

yearNacimiento = contactos["Miguel Angel"]["Fech nacimniento"][2]
print(yearNacimiento)

# Miguel es mayor o menor de edad ?

yearActual= 2024 - yearNacimiento;

if yearNacimiento - yearActual >=18:
  print(f"Miguel angel es mayor de edad que trabaje")
else:
  print(f"Miguel angel es menor de edad")


del contactos["Pedro"] # Eliminar un contacto
print(*contactos)

contactos["Miguel Angel"]["Correo"].remove("Miangel@gmail.com")
print(*contactos["Miguel Angel"]["Correo"])