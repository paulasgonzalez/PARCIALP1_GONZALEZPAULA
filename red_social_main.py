from funciones_red_social import *
from random import randint


while True:
    match menu():
        case 'A':
            datos = cargar_csv()
        case 'B':
            mostrar_users(datos)
        case 'C':
            likes_mapeados = mapear_lista(lambda user: cargar_enteros_random(user, 'likes', 500, 3000), datos)
            dislikes_mapeados = mapear_lista(lambda user: cargar_enteros_random(user, 'dislikes', 300, 3500), likes_mapeados)
            datos_nuevos = mapear_lista(lambda user: cargar_enteros_random(user, 'followers', 10000, 20000), dislikes_mapeados)
        case 'D':
            mejores_posts = filtrar_lista(lambda user: user['likes'] > 2000, datos_nuevos)
            guardar_csv("mejores_posts.csv", mejores_posts)
        case 'E':
            haters_posts = filtrar_lista(lambda user: user['dislikes'] > user['likes'], datos_nuevos)
            guardar_csv("haters_posts.csv", haters_posts)
        case 'F':
            print(f"El promedio de followers es: {promedio_followers(datos_nuevos)}")
        case 'G':
            ordenar_users(datos_nuevos, 'user')
            guardar_json(datos_nuevos, "posts_ordenado.json")
        case 'H':
            mas_likeados = buscar_users_mas_likeados(datos_nuevos, 'likes')
            print("El/los user/s mas likeado/s es/son:")
            for user in mas_likeados:
                for key, value in user.items():
                    print(f"{key}: {value}")
        case 'I':
            break
        case _:
            print("La opcion seleccionada es invalida")
        
    pausar()
    
print("Fin del programa")