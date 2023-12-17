import Run_RADMC3D_From_Python.py

################ Example run_simple_1 ################
## Corremos run_simple_1
nombre_directorio= "radmc3d-2.0"

nombre_ejemplo= "run_simple_1"

ruta_radmc= buscar_directorio(nombre_directorio, nombre_ejemplo) #Llamamos función para buscar directorio
print(os.getcwd()) #Printeamos actual directorio

run_simple_1(ruta_radmc) #Llamado a función que ejecuta run_simple_1

################ Example run_ppdisk_fargo3d_1 ################
## Corremos run_ppdisk_fargo3d_1
nombre_directorio= "radmc3d-2.0"

nombre_ejemplo= "run_ppdisk_fargo3d_1"

ruta_fargo= buscar_directorio(nombre_directorio, nombre_ejemplo) #Llamamos función para buscar directorio
print(os.getcwd()) #Printeamos actual directorio

modelo = "my_own_1_problem_setup.py" #Nombre del modelo que queramos correr
run_fargo(ruta_fargo,modelo) #Llamado a función que ejecuta el .py especificado
