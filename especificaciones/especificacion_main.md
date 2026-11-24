Nombre del archivo: main.py

Objetivo: Controlar el funcionamiento general de la aplicación, establecer la comunicación entre las clases y permitir que el usuario interactúe con el programa mediante un menú de consola.
Menú principal
El programa tendrá las siguientes opciones:

Objetos que se deben crear

Objeto de la clase Usuario:

Se creará cuando el usuario seleccione la opción de obtener recomendaciones. Será el encargado de almacenar su nombre y sus preferencias cinematográficas.

Objeto de la clase RecomendadorPeliculas:

Se creará para gestionar los perfiles existentes, el catálogo de películas y los cálculos matemáticos necesarios para generar recomendaciones.

Secuencia de operaciones

1. Iniciar el programa y mostrar el menú principal.
2. Solicitar al usuario que seleccione una opción.
3. Si selecciona obtener recomendaciones:
   - Crear un objeto de la clase Usuario.
   - Registrar su nombre.
   - Registrar las calificaciones de los géneros cinematográficos.
   - Registrar las calificaciones de las películas base.
   - Crear un objeto de la clase RecomendadorPeliculas.
   - Obtener el perfil del usuario mediante obtener_perfil().
   - Comparar el perfil con los perfiles existentes mediante comparar_perfiles().
   - Generar recomendaciones mediante generar_recomendaciones().
   - Mostrar los resultados mediante mostrar_recomendaciones().
4. Si selecciona salir, finalizar el programa.
5. Si introduce una opción inválida, mostrar un mensaje de error y volver a presentar el menú.

Condiciones de salida

- El programa finalizará cuando el usuario seleccione la opción 2.
- Si el usuario introduce una opción inexistente, el menú volverá a mostrarse.
- Si no existen perfiles suficientes para realizar una comparación, se informará al usuario.
- Si no existen películas disponibles para recomendar, se mostrará un mensaje indicándolo.

Reglas que no puede alterar Copilot

1. El menú debe ejecutarse mediante un ciclo que permita repetir las operaciones.
2. La opción de salir debe finalizar correctamente el programa.
3. Las clases deben estar separadas del archivo principal.
4. main.py debe encargarse de coordinar los objetos y sus métodos, no de realizar directamente los cálculos matemáticos.
5. Las validaciones deben respetarse durante todo el funcionamiento del programa.