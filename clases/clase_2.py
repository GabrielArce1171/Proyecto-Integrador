from clases.clase_1 import Usuario
import math


class RecomendadorPeliculas(Usuario):

    def __init__(self):
        super().__init__()

        # Cinco perfiles existentes.
        # Orden: 6 generos + 5 peliculas base.
        self.perfiles_existentes = [
            {
                "nombre": "Alejandro",
                "vector": [5, 2, 3, 1, 5, 3, 5, 2, 3, 1, 5]
            },
            {
                "nombre": "Sofia",
                "vector": [2, 4, 0, 5, 2, 5, 2, 4, 0, 5, 3]
            },
            {
                "nombre": "Diego",
                "vector": [3, 1, 5, 0, 3, 2, 3, 1, 5, 0, 3]
            },
            {
                "nombre": "Valentina",
                "vector": [2, 5, 1, 4, 1, 3, 2, 5, 1, 4, 2]
            },
            {
                "nombre": "Sebastian",
                "vector": [4, 2, 1, 2, 5, 4, 4, 2, 1, 2, 5]
            }
        ]

        # Catalogo de peliculas y calificaciones de los perfiles.
        self.catalogo_peliculas = [
            {
                "titulo": "Mad Max: Furia en el camino",
                "calificaciones": [5, 2, 3, 2, 4]
            },
            {
                "titulo": "Supercool",
                "calificaciones": [2, 5, 1, 5, 2]
            },
            {
                "titulo": "Hereditary",
                "calificaciones": [3, 1, 5, 2, 2]
            },
            {
                "titulo": "Diario de una pasion",
                "calificaciones": [1, 5, 0, 5, 2]
            },
            {
                "titulo": "El origen",
                "calificaciones": [5, 3, 3, 2, 5]
            },
            {
                "titulo": "Sueños de fuga",
                "calificaciones": [3, 5, 2, 4, 4]
            },
            {
                "titulo": "Los Vengadores",
                "calificaciones": [5, 2, 3, 2, 5]
            },
            {
                "titulo": "Un lugar en silencio",
                "calificaciones": [4, 1, 5, 2, 3]
            },
            {
                "titulo": "La La Land",
                "calificaciones": [1, 5, 0, 5, 2]
            },
            {
                "titulo": "Mision rescate",
                "calificaciones": [5, 3, 2, 2, 5]
            }
        ]

        self.cantidad_recomendaciones = 5

    def calcular_similitud_coseno(self, vector_usuario, vector_perfil):
        if len(vector_usuario) != len(vector_perfil):
            raise ValueError("Los vectores deben tener la misma dimension.")

        producto_punto = sum(
            a * b for a, b in zip(vector_usuario, vector_perfil)
        )

        magnitud_usuario = math.sqrt(
            sum(a ** 2 for a in vector_usuario)
        )

        magnitud_perfil = math.sqrt(
            sum(b ** 2 for b in vector_perfil)
        )

        if magnitud_usuario == 0 or magnitud_perfil == 0:
            return 0

        similitud = producto_punto / (
            magnitud_usuario * magnitud_perfil
        )

        return similitud

    def comparar_perfiles(self):
        vector_usuario = self.obtener_perfil_vector()
        resultados = []

        for perfil in self.perfiles_existentes:
            similitud = self.calcular_similitud_coseno(
                vector_usuario,
                perfil["vector"]
            )

            resultados.append({
                "nombre": perfil["nombre"],
                "similitud": similitud
            })

        resultados.sort(
            key=lambda perfil: perfil["similitud"],
            reverse=True
        )

        return resultados

    def calcular_puntuaciones_peliculas(self, perfiles_similares):
        puntuaciones = []

        for pelicula in self.catalogo_peliculas:
            suma_ponderada = 0
            suma_similitudes = 0

            for perfil in perfiles_similares:

                similitud = perfil["similitud"]

                if similitud > 0:
                    # Buscar la calificacion del perfil
                    # correspondiente a esta pelicula.
                    indice = next(
                        i for i, p in enumerate(self.perfiles_existentes)
                        if p["nombre"] == perfil["nombre"]
                    )

                    calificacion = pelicula["calificaciones"][indice]

                    suma_ponderada += similitud * calificacion
                    suma_similitudes += similitud

            if suma_similitudes > 0:
                puntuacion = suma_ponderada / suma_similitudes

                puntuaciones.append({
                    "titulo": pelicula["titulo"],
                    "puntuacion": puntuacion
                })

        puntuaciones.sort(
            key=lambda pelicula: pelicula["puntuacion"],
            reverse=True
        )

        return puntuaciones

    def generar_recomendaciones(self, puntuaciones):
        return puntuaciones[:self.cantidad_recomendaciones]

    def mostrar_recomendaciones(self, recomendaciones):
        print("\n========================================")
        print("RECOMENDACIONES PARA:", self.nombre.upper())
        print("========================================")

        if not recomendaciones:
            print("No fue posible generar recomendaciones.")
            return

        for numero, pelicula in enumerate(recomendaciones, start=1):
            print(
                f"{numero}. {pelicula['titulo']} "
                f"- Puntuacion: {pelicula['puntuacion']:.2f}/5"
            )
