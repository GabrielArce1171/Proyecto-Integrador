Nombre de la clase: Usuario

Objetivo: Representar al usuario que utiliza el programa, almacenar sus preferencias cinematográficas y conservar las calificaciones que proporciona.

Responsabilidad: Recibir, almacenar y validar el nombre del usuario, sus calificaciones por género y sus calificaciones de las películas base.

Atributos
Atributo	                Tipo de dato	    Significado

nombre	                    String	            Nombre del usuario.
calificaciones_generos	    Diccionario	        Calificación de cada género cinematográfico.
calificaciones_peliculas	Diccionario	        Calificación de cada película base.

Los diccionarios permitirán relacionar cada género o película con su respectiva calificación.

Constructor __init__ :

Recibirá el nombre del usuario y creará los diccionarios de calificaciones vacíos.
- nombre: cadena de texto.
- calificaciones_generos: diccionario vacío inicialmente.
- calificaciones_peliculas: diccionario vacío inicialmente.

Métodos:

1. registrar_nombre()
- Objetivo: registrar el nombre del usuario.
- Entrada: nombre mediante consola.
- Atributos utilizados: nombre.
- Algoritmo: solicitar el nombre, comprobar que no esté vacío y que no contenga números. Si no cumple las condiciones, volver a solicitarlo.
- Resultado: nombre almacenado correctamente.

2. registrar_calificaciones_generos()
- Objetivo: registrar las preferencias del usuario respecto a los géneros cinematográficos.
- Entrada: calificaciones enteras del 0 al 5.
- Atributos utilizados: calificaciones_generos.
- Algoritmo: recorrer una lista de géneros, solicitar una calificación para cada uno y almacenarla en el diccionario.
- Validaciones: aceptar únicamente números enteros entre 0 y 5.
- Resultado: diccionario con las calificaciones de todos los géneros.

3. registrar_calificaciones_peliculas()
- Objetivo: conocer qué tanto le gustan al usuario determinadas películas conocidas.
- Entrada: calificaciones enteras del 0 al 5.
- Atributos utilizados: calificaciones_peliculas.
- Algoritmo: recorrer la lista de películas base, solicitar una calificación para cada una y almacenarla en el diccionario.
- Validaciones: aceptar únicamente números enteros entre 0 y 5.
- Resultado: diccionario con las calificaciones de las películas base.

4. obtener_perfil()
- Objetivo: reunir las preferencias del usuario en una estructura que pueda utilizar la clase recomendadora.
- Entrada: ninguna.
- Atributos utilizados: todos los atributos de la clase.
- Algoritmo: organizar las calificaciones de géneros y películas en una estructura de datos.
- Resultado: perfil completo del usuario.

Reglas que no puede alterar Copilot
1. El nombre del usuario debe ser texto y no puede contener números.
2. Todas las calificaciones deben ser números enteros.
3. Las calificaciones deben encontrarse entre 0 y 5, incluyendo ambos extremos.
4. No se deben almacenar calificaciones inválidas.
5. Cada género y película debe conservar su propia calificación.