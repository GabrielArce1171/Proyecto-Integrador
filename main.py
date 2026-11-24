
from clases.clase_2 import RecomendadorPeliculas


def mostrar_menu():
    print("\n========================================")
    print("       RECOMENDADOR DE PELICULAS")
    print("========================================")
    print("1. Obtener recomendaciones")
    print("2. Salir")
    print("========================================")


def obtener_recomendaciones():
    # Crear objeto del recomendador
    recomendador = RecomendadorPeliculas()

    # Registrar informacion del usuario
    print("\n--- REGISTRO DE USUARIO ---")
    recomendador.registrar_nombre()

    recomendador.registrar_calificaciones_generos()

    recomendador.registrar_calificaciones_peliculas()

    # Comparar el usuario con los perfiles existentes
    print("\n--- COMPARANDO PERFILES ---")

    perfiles_similares = recomendador.comparar_perfiles()

    print("\nSimilitud con los perfiles existentes:")

    for perfil in perfiles_similares:
        print(
            f"{perfil['nombre']}: "
            f"{perfil['similitud']:.4f}"
        )

    # Calcular las puntuaciones de las peliculas
    puntuaciones = recomendador.calcular_puntuaciones_peliculas(
        perfiles_similares
    )

    # Obtener las cinco mejores recomendaciones
    recomendaciones = recomendador.generar_recomendaciones(
        puntuaciones
    )

    # Mostrar resultados
    recomendador.mostrar_recomendaciones(recomendaciones)


def main():
    while True:
        mostrar_menu()

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            obtener_recomendaciones()

        elif opcion == "2":
            print("\nGracias por utilizar nuestro recomendador.")
            print("Hasta pronto.")
            break

        else:
            print("\nOpcion invalida. Selecciona 1 o 2.")


if __name__ == "__main__":
    main()
