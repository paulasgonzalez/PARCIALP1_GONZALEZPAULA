from os import system
from random import randint
import json

def limpiar_pantalla():
    """funcion que limpia la pantalla
    """
    system("clear")
    
    
def menu()-> str:
    """muestra menu para elegir una opcion

    Returns:
        str: retorna un input para que el usuario ingrese la opcion elegida
    """
    print(" ***MENU DE OPCIONES*** ")
    print("A- Cargar archivo .CSV")
    print("B- Imprimir lista")
    print("C- Asignar estadisticas")
    print("D- Filtrar por mejores post")
    print("E- Filtrar por haters")
    print("F- Informar promedio de followers")
    print("G- Ordenar los datos por nombre de user ascendente")
    print("H- Mostrar mas popular")
    print("I- Salir")
    
    return input('Ingrese opcion: ').upper()


def pausar()-> str:
    input('Aprete una tecla para continuar...')

   
def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def leer_csv(nombre_archivo:str)->list:
    """lee y carga un archivo csv en formato de lista de diccionarios

    Args:
        nombre_archivo (str): recibe el nombre del archivo en formato csv a leer

    Returns:
        list: retorna una lista de diccionarios
    """
    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
    
        
        for linea in archivo.readlines():
            usuario = {}
            linea = linea.strip("\n").split(",")
            
            id, user, likes, dislikes, followers = linea
            
            usuario["id"] = int(id)
            usuario["user"] = user
            usuario["likes"] = int(likes)
            usuario["dislikes"] = int(dislikes)
            usuario["followers"] = int(followers)
                        
            lista.append(usuario)
            
    return lista


def cargar_csv():
    
    archivo = input("Ingrese el nombre del archivo que desea cargar: ")
    datos = leer_csv(archivo)
    return datos


def mostrar_users(users:list)->None:
    """muestra en formato tabla una lista

    Args:
        users (list): recibe una lista
    """
    print('                     ***LISTA USERS***                             ')
    print('ID          USER             LIKES            DISLIKES       FOLLOWERS')
    print('------------------------------------------------------------------------------')
    for i in range(len(users)):
        mostrar_un_user(users[i])
    print()


def mostrar_un_user(un_user:dict):
    """muestra a un usuario

    Args:
        un_user (dict): recibe un diccionario
    """
    print(f"{un_user['id']}        {un_user['user']:>10}   {un_user['likes']:>10}     {un_user['dislikes']:>10}    {un_user['followers']:>10}")


def mapear_lista(procesadora, lista:list)-> list:
    """mapea una lista

    Args:
        procesadora (_type_): funcion anonima que realizara una accion por cada elemento de la lista
        lista (list): lista recibida por parametros

    Returns:
        list: retorna una nueva lista
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno


def cargar_enteros_random(diccionario:dict, clave:str, min:int, max:int)->dict:
    """carga numeros enteros de manera aleatoria

    Args:
        diccionario (dict): recibe un diccionario
        clave (str): recibe una clave, que sera a la que se le asignara un numero random como valor
        min (int): valor minimo para cargar
        max (int): valor maximo para cargar

    Returns:
        dict: retorna el diccionario con los valores random agregados a la clave
    """
    for _ in diccionario:
        diccionario[clave] = randint(min, max)
    return diccionario


def filtrar_lista(filtradora, lista:list)->list:
    """filtra una lista

    Args:
        filtradora (_type_): funcion anonima que filtrara la lista retornando un booleano
        lista (list): lista recibida para filtrar

    Returns:
        list: retorna una nueva lista filtrada
    """
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def guardar_csv(nombre_archivo_nuevo:str, lista:list):
    """funcion que guarda una lista en formato csv

    Args:
        nombre_archivo_nuevo (str): nombre nuevo del archivo a guardar
        lista (list): lista que deseo guardar en formato csv
    """
    with open(get_path_actual(nombre_archivo_nuevo), "w", encoding="utf-8") as archivo:
        keys = list(lista[0].keys())
        
        encabezado = ",".join(keys) + "\n"
        archivo.write(encabezado)
        
        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
                
            linea = ",".join(l) + "\n"
            archivo.write(linea)
            
            
def promedio_followers(diccionario:dict)->float:
    """funcion que realiza un promedio de followers

    Args:
        diccionario (dict): diccionario

    Returns:
        float: retorna un valor flotante como promedio
    """
    acumulador_followers = 0
    contador_users = 0
    for usuario in diccionario:
        acumulador_followers += usuario['followers']
        contador_users += 1
    
    return acumulador_followers / contador_users


def swap_lista(lista:list, i:int, j:int)-> None:
    """funcion que swapea dos indices de una lista

    Args:
        lista (list): lista recibida por parametros
        i (int): indice i
        j (int): indice j
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    
    
def ordenar_users(lista:list, campo:str, asc:bool = True)->None:
    """funcion que ordena los usuarios por el campo recibido

    Args:
        lista (list): lista a ordenar
        campo (str): campo a comparar
        asc (bool, optional): _description_. Defaults to True. : indicador para saber si se desea ordenar en orden ascendente o descendente. Si es ascendente no hace falta indicar nada por parametros, ya que esta explicito
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][campo] > lista[j][campo] if asc else lista[i][campo] < lista[j][campo]:
                swap_lista(lista, i, j)


def guardar_json(datos:list, nombre_archivo_nuevo:str):
    """funcion para guardar una lista en formato json

    Args:
        datos (list): lista recibida por parametro
        nombre_archivo_nuevo (str): nombre nuevo para el archivo que deseo guardar
    """
    with open(get_path_actual(nombre_archivo_nuevo), "w",encoding= "utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        
            
def obtener_mayor(lista)->int:
    """funcion para obtener el mayor de una lista

    Args:
        lista (_type_): lista

    Raises:
        Exception: si la lista esta vacia lanzara una excepcion

    Returns:
        int: retorna el numero mas grande de la lista
    """
    if len(lista) == 0:
        raise Exception ("La lista esta vacia")
    
    flag = True
    for el in lista:
        if flag or n_mayor < el:
            n_mayor = el
            flag = False
            
    return n_mayor

def buscar_users_mas_likeados(lista:list, campo:str)->list:
    """funcion que busca el o los users con mas likes

    Args:
        lista (list): lista a analizar
        campo (str): campo a comparar

    Returns:
        list: retorna una lista con los usuarios con mas likes (si es mas de uno, tendran la misma cantidad de likes)
    """
    lista_likes = []
    lista_usuarios = []
    
    for usuario in lista:
        lista_likes.append(usuario[campo])
    
    mas_likes = obtener_mayor(lista_likes)
    
    for usuario in lista:
        if usuario[campo] == mas_likes:
            lista_usuarios.append(usuario)
                
    return lista_usuarios