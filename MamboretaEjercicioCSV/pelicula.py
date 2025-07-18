"""a) Construir las clases que considere necesarias para soportar la información
presentada.

b) Para cada una de las clases del punto anterior defina un constructor
parametrizado y el método __str__().

c) Identifique los campos clave de cada una de las clases y programe el método
__eq__()."""

from datetime import datetime
from typing import List
from persona import Persona
from genero import Genero

class Pelicula:
    def __init__(self, id: int, titulo: str, fecha_publicacion: datetime, retorno: float, duracion_minutos: int, 
                 presupuesto: float, sitio_web: str, idioma_original: str, poster: str, rating: float, 
                 famosos_list: List[Persona], generos_list: List[Genero]) -> None:
        self.id = id
        self.titulo = titulo
        self.fecha_publicacion = fecha_publicacion
        self.retorno = retorno
        self.duracion_minutos = duracion_minutos
        self.presupuesto = presupuesto
        self.sitio_web = sitio_web
        self.idioma_original = idioma_original
        self.poster = poster
        self.rating = rating
        self.famosos_list = famosos_list
        self.generos_list = generos_list

    def __str__(self) -> str:
        generos_str = ', '.join(str(genero) for genero in self.generos_list)
        famosos_str = ', '.join(str(persona) for persona in self.famosos_list)
        return (f"Pelicula: {self.titulo}\n"
                f"ID: {self.id}\n"
                f"Fecha de Publicación: {self.fecha_publicacion.strftime('%Y-%m-%d')}\n"
                f"Retorno: ${self.retorno:.2f}\n"
                f"Duración: {self.duracion_minutos} minutos\n"
                f"Presupuesto: ${self.presupuesto:.2f}\n"
                f"Sitio Web: {self.sitio_web}\n"
                f"Idioma Original: {self.idioma_original}\n"
                f"Poster: {self.poster}\n"
                f"Rating: {self.rating:.1f}\n"
                f"Famosos: {famosos_str}\n"
                f"Géneros: {generos_str}")

    def __eq__(self, other) -> bool:
        if isinstance(other, Pelicula):
            return (self.id == other.id and
                    self.titulo == other.titulo and
                    self.fecha_publicacion == other.fecha_publicacion and
                    self.retorno == other.retorno and
                    self.duracion_minutos == other.duracion_minutos and
                    self.presupuesto == other.presupuesto and
                    self.sitio_web == other.sitio_web and
                    self.idioma_original == other.idioma_original and
                    self.poster == other.poster and
                    self.rating == other.rating and
                    self.famosos_list == other.famosos_list and
                    self.generos_list == other.generos_list)
        return False

