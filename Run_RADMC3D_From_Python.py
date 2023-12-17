#Importamos librerías
import os

###Funciones:

##Función que ubica el directorio que queremos encontrar, en este caso radmc3d-2.0
def buscar_directorio(nombre_directorio, nombre_ejemplo):
    '''
    Esta función ubica el path de radmc3d-2.0, y el de la carpeta examples, para luego cambiar a ese directorio.
   
    Argumentos de la función:
    nombre_directorio (string): Nombre del directorio que estamos buscando, en este caso radmc3d-2.0.
    nombre_ejemplo (string): Nombre del ejemplo que queremos trabajar.
   
    Output:
    El output de la función es la ruta en la que se encuentra actualmente según lo especificado en los argumentos.
    
    #Ejemplo de uso
    nombre_directorio= "radmc3d-2.0"

    nombre_ejemplo= "run_simple_1_binary"

    ruta_radmc= buscar_directorio(nombre_directorio, nombre_ejemplo) #Llamamos a la función dentro de una variable
    '''

    #Itera entre directorios hasta encontrar el nombre_directorio a encontrar, desde /home
    os.chdir("/home")
    for root, dirs, files in os.walk(str(os.getcwd())):
        if nombre_directorio in dirs:
            #En caso de encontrar el directorio crea la ruta hasta el, si no, sigue iterando hasta encontrarlo
            ruta = str(os.path.join(root, nombre_directorio))
            os.chdir(ruta)
            os.chdir("examples") #Entramos a examples
            rutafinal= os.chdir(nombre_ejemplo) #Path final de interés
            
            return print("Su ruta:", os.getcwd())
    return print("No se pudo encontrar el directorio")


##Función para ejecutar el ejemplo "run_simple_1"
def run_simple_1(ruta):
    '''
    Esta función ejecuta el ejemplo run_simple_1 de radmc3d. 
   
    Argumentos de la función:
    ruta (string): Nombre del path en donde se ubica run_simple_1.
   
    Output:
    El output de la función son los ploteos del ejemplo.
    
    #Ejemplo de uso
    nombre_directorio= "radmc3d-2.0"

    nombre_ejemplo= "run_simple_1_binary"

    ruta_radmc= buscar_directorio(nombre_directorio, nombre_ejemplo) #Llamamos a la función para buscar directorio
    dentro de una variable
    
    run_simple_1(ruta_radmc) #Llamamos a la función
    '''

    #Sigue los pasos para ejecutar el ejemplo de radmc3d 
    os.system('python3 problem_setup.py')
    
    os.system('radmc3d mctherm')
    
    os.system('ipython3 --matplotlib')
    
    %run problem_plotexamples.py

##Función para ejecutar el ejemplo "run_ppdisk_fargo3d_1"
def run_fargo(ruta, modelo):
    '''
    Esta función ejecuta el ejemplo run_ppdisk_fargo3d_1 de radmc3d. 
   
    Argumentos de la función:
    ruta (string): Nombre del path en donde se ubica run_ppdisk_fargo3d_1.
    modelo (string): Nombre del modelo que queramos correr.
   
    Output:
    El output de la función son los ploteos del ejemplo.
    
    #Ejemplo de uso
    nombre_directorio= "radmc3d-2.0"

    nombre_ejemplo= "run_ppdisk_fargo3d_1"

    ruta_fargo= buscar_directorio(nombre_directorio, nombre_ejemplo) #Llamamos a la función para buscar directorio

    modelo = "prueba_fargo_1.py" #Nombre del modelo que queramos correr
    
    run_fargo(ruta_fargo,modelo) #Llamamos a la función
    '''
    
    #Sigue los pasos para ejecutar el ejemplo de radmc3d 
    
    os.system(f"python3 {modelo}")
    
    os.system('radmc3d mctherm')
    
    os.system('ipython3 --matplotlib')
    
    %run plot_images.py
