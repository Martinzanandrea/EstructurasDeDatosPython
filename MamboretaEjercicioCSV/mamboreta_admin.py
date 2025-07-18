"""d) Programe la clase MamboretaAdmin como clase derivada de
MamboretadminAbstract y programe los métodos abstractos en ella definida"""

import pandas as pd
from datetime import datetime
from typing import List
from mamboreta_admin_abstracta import MamboretaAdminAbstract
from pelicula import Pelicula
from persona import Persona
from genero import Genero

class MamboretaAdmin(MamboretaAdminAbstract):
    def procesar_archivo(self, ruta: str) -> None:
        df = pd.read_csv(ruta)
        for _, row in df.iterrows():
            id = int(row['id'])
            titulo = row['title']
            fecha_publicacion = datetime.strptime(row['release_date'], '%Y-%m-%d')
            retorno = float(row['revenue']) if not pd.isna(row['revenue']) else 0.0
            duracion_minutos = int(row['runtime'])
            presupuesto = float(row['budget']) if not pd.isna(row['budget']) else 0.0
            sitio_web = row['homepage'] if not pd.isna(row['homepage']) else ''
            idioma_original = row['original_language']
            poster = row['Poster_Link'] if not pd.isna(row['Poster_Link']) else ''
            rating = float(row['IMDB_Rating']) if not pd.isna(row['IMDB_Rating']) else 0.0

            # Convertir las cadenas de géneros y actores en objetos
            generos_list = [Genero(nombre.strip()) for nombre in row['genres_list'].strip("[]").replace("'", "").split(',') if nombre.strip()]
            famosos_list = [Persona(nombre.strip()) for nombre in row['Cast_list'].strip("[]").replace("'", "").split(',') if nombre.strip()]

            pelicula = Pelicula(
                id=id,
                titulo=titulo,
                fecha_publicacion=fecha_publicacion,
                retorno=retorno,
                duracion_minutos=duracion_minutos,
                presupuesto=presupuesto,
                sitio_web=sitio_web,
                idioma_original=idioma_original,
                poster=poster,
                rating=rating,
                famosos_list=famosos_list,
                generos_list=generos_list
            )
            self.lista.append(pelicula)
            
          
            # print(f"Pelicula cargada: {pelicula}")
            #print(f"Géneros: {[str(genero) for genero in generos_list]}")
            #print(f"Famosos: {[str(persona) for persona in famosos_list]}")
            # print(f"Retorno: {retorno}, Presupuesto: {presupuesto}")
    def __str__(self) -> str:
        return '\n'.join(str(pelicula) for pelicula in self.lista)

    def filtrar_por_genero(self, genero: Genero) -> List[Pelicula]:
        return [pelicula for pelicula in self.lista if genero in pelicula.generos_list]

    def filtrar_por_persona(self, persona: Persona) -> List[Pelicula]:
        return [pelicula for pelicula in self.lista if persona in pelicula.famosos_list]

    def filtrar_companieros(self, persona1: Persona, persona2: Persona) -> List[Pelicula]:
        return [pelicula for pelicula in self.lista if persona1 in pelicula.famosos_list and persona2 in pelicula.famosos_list]

    def top_n(self, n: int = 5) -> List[Pelicula]:
        return sorted(self.lista, key=lambda pelicula: pelicula.rating, reverse=True)[:n]

    def fracasos_comerciales(self, umbral: float = 0.0) -> List[Pelicula]:
     print("\nPELICULAS QUE HAN SIDO UN FRACASO COMERCIAL: ")
     return [pelicula for pelicula in self.lista if (pelicula.retorno - pelicula.presupuesto) < umbral]

 