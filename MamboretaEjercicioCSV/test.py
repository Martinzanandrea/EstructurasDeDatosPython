"""e) Demuestre el correcto funcionamiento de los puntos anteriores."""
"""¡¡¡IMPORTANTE!!!: Para probar los métodos, asegúrate de descomentar las líneas correspondientes"""

from mamboreta_admin import MamboretaAdmin
from persona import Persona
from genero import Genero

def main():
    
    ruta_csv = 'imdb.csv'

    admin = MamboretaAdmin()
    admin.procesar_archivo(ruta_csv)

    """Imprimir todas las películas"""
    # print("TODAS LAS PELICULAS:")
    # print(admin)

    """Filtrar por género"""
    # genero_comedia = Genero('Comedy')
    # peliculas_comedia = admin.filtrar_por_genero(genero_comedia)
    # for pelicula in peliculas_comedia:
    #     print("\n PELICULA QUE PERTENECE  AL GENERO COMEDY:")
    #     print(pelicula)
    
    # genero_drama = Genero('Drama')
    # peliculas_drama = admin.filtrar_por_genero(genero_drama)
    # for pelicula in peliculas_drama:
    #     print("\n PELICULA QUE PERTENECE AL GENERO DRAMA:")
    #     print(pelicula)
        
    # genero_crime = Genero('Crime')
    # peliculas_crime = admin.filtrar_por_genero(genero_crime)
    # for pelicula in peliculas_crime:
    #     print("\n PELICULA QUE PERTENECE AL GENERO CRIME:")
    #     print(pelicula)
    """Filtrar por persona"""
    # actor_a1 = Persona('Tom Rack')
    # peliculas_actor_a1 = admin.filtrar_por_persona(actor_a1)
    # print("\nPELICULAS DONDE TRABAJO EL ACTOR TOM RACK:")
    # if not peliculas_actor_a1:
    #     print("VACIO")
    # else:
    #     for pelicula in peliculas_actor_a1:
    #         print(pelicula)
   

    """Filtrar compañeros"""
    # actor_a1 = Persona('Richard Bigotini')
    # actor_b1 = Persona('Pierre Taylou')
    # peliculas_companieros = admin.filtrar_companieros(actor_a1, actor_b1)
    # print("\nPELICULAS DONDE ESTOS DOS ACTORES HAN TRABAJADO JUNTOS:")
    # for pelicula in peliculas_companieros:
    #     print(pelicula)

    """Mostrar top 5 película"""
    # top_peliculas = admin.top_n(5)
    # print("\nTOP 5 PELICULAS:")
    # for pelicula in top_peliculas:
    #     print(pelicula)

    """Mostrar fracasos comerciales"""
    # fracasos = admin.fracasos_comerciales()
    # # print("\nFRACASOS COMERCIALES:")
    # if not fracasos:
    #     print("VACIO")
    # else:
    #     for pelicula in fracasos:
    #         print("\nFRACASO COMERCIAL:")
    #         print(pelicula)
    
if __name__ == '__main__':
   main()
