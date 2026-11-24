class Usuario:
    # Generos y peliculas que se utilizaran para conocer los gustos
    GENEROS = [
        "Accion",
        "Comedia",
        "Terror",
        "Romance",
        "Ciencia ficcion",
        "Drama"
    ]

    PELICULAS_BASE = [
        "El caballero de la noche",
        "Que paso ayer",
        "El conjuro",
        "Titanic",
        "Interestelar"
    ]

    def __init__(self):
        self.nombre = ""
        self.calificaciones_generos = {}
        self.calificaciones_peliculas = {}

    def registrar_nombre(self):
        while True:
            nombre = input("Ingresa tu nombre: ").strip()

            if nombre and all(
                caracter.isalpha() or caracter.isspace()
                for caracter in nombre
            ):
                self.nombre = nombre
                break
            else:
                print("Error: ingresa un nombre sin numeros.")

    def solicitar_calificacion(self, elemento):
        while True:
            try:
                calificacion = int(
                    input(f"Califica {elemento} del 0 al 5: ")
                )

                if 0 <= calificacion <= 5:
                    return calificacion
                else:
                    print("Error: la calificacion debe estar entre 0 y 5.")

            except ValueError:
                print("Error: debes ingresar un numero entero.")

    def registrar_calificaciones_generos(self):
        print("\nCALIFICACION DE GENEROS")

        for genero in self.GENEROS:
            calificacion = self.solicitar_calificacion(genero)
            self.calificaciones_generos[genero] = calificacion

    def registrar_calificaciones_peliculas(self):
        print("\nCALIFICACION DE PELICULAS BASE")

        for pelicula in self.PELICULAS_BASE:
            calificacion = self.solicitar_calificacion(pelicula)
            self.calificaciones_peliculas[pelicula] = calificacion

    def obtener_perfil_vector(self):
        vector = []

        for genero in self.GENEROS:
            vector.append(self.calificaciones_generos[genero])

        for pelicula in self.PELICULAS_BASE:
            vector.append(self.calificaciones_peliculas[pelicula])

        return vector
