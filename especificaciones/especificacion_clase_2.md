Nombre de la clase: RecomendadorPeliculas

Objetivo: Analizar las preferencias cinematográficas del usuario mediante operaciones de álgebra lineal y generar recomendaciones de películas que se adapten a sus gustos.

Responsabilidad: Almacenar los perfiles cinematográficos existentes, calcular la similitud coseno entre usuarios y determinar qué películas recomendar.

Atributos
Atributo	                Tipo de dato	    Significado

perfiles_existentes	        Lista	            Almacena los perfiles de usuarios anteriores.
peliculas_base	            Lista	            Películas utilizadas para conocer las preferencias del usuario.
catalogo_peliculas	        Lista	            Contiene las películas disponibles para recomendar.
cantidad_recomendaciones	Entero	            Número de películas que se mostrarán al usuario.

Constructor __init__ :

Recibirá la información necesaria para inicializar el recomendador:
- perfiles_existentes: lista con perfiles de usuarios previamente registrados.
- peliculas_base: lista de películas utilizadas como referencia.
- catalogo_peliculas: lista de películas disponibles para recomendar.
- cantidad_recomendaciones: inicialmente 5.

Métodos:

1. convertir_perfil_vector()
- Objetivo: convertir las calificaciones del usuario en un vector numérico.
- Entrada: perfil del usuario.
- Atributos utilizados: peliculas_base.
- Algoritmo: organizar las calificaciones de los géneros y las películas base en un orden establecido, convirtiéndolas en una lista de números.
- Resultado: vector numérico que representa los gustos del usuario.

2. calcular_similitud_coseno()
- Objetivo: determinar qué tan parecido es el perfil del usuario al de otro usuario.
- Entrada: dos vectores numéricos.
- Atributos utilizados: ninguno adicional.
- Algoritmo: calcular el producto punto de ambos vectores y dividirlo entre el producto de sus magnitudes.

La fórmula utilizada será:
\[
\operatorname{Sim}(A,B)=
\frac{A\cdot B}{\|A\|\|B\|}
\]

- Resultado: valor numérico de similitud entre los dos perfiles.
- Validaciones: comprobar que los vectores tengan la misma dimensión y que ninguno tenga magnitud cero.

3. comparar_perfiles()
- Objetivo: comparar el perfil del usuario con todos los perfiles existentes.
- Entrada: perfil del usuario.
- Atributos utilizados: perfiles_existentes.
- Algoritmo:
  1. Convertir el perfil del usuario en un vector.
  2. Recorrer la lista de perfiles existentes.
  3. Convertir cada perfil en un vector con el mismo orden de características.
  4. Calcular la similitud coseno.
  5. Almacenar el resultado de cada comparación.
  6. Ordenar los perfiles de mayor a menor similitud.
- Resultado: lista de perfiles ordenados según su similitud con el usuario.

4. generar_recomendaciones()
- Objetivo: seleccionar películas que puedan interesarle al usuario.
- Entrada: lista de perfiles similares.
- Atributos utilizados: catalogo_peliculas y cantidad_recomendaciones.
- Algoritmo:
  1. Identificar los perfiles con mayor similitud.
  2. Revisar las películas que han calificado esos usuarios.
  3. Identificar las películas mejor calificadas por los usuarios similares.
  4. Excluir las películas base que el usuario ya calificó.
  5. Ordenar las películas candidatas según su puntuación de recomendación.
  6. Seleccionar las cinco mejores recomendaciones.
- Resultado: lista de películas recomendadas.

5. mostrar_recomendaciones()
- Objetivo: presentar al usuario los resultados obtenidos.
- Entrada: lista de películas recomendadas.
- Atributos utilizados: ninguno adicional.
- Algoritmo: recorrer la lista e imprimir el título de cada película en la terminal.
- Resultado: recomendaciones visibles en consola.

Reglas que no puede alterar Copilot

1. La similitud debe calcularse mediante la fórmula de similitud coseno.
2. Todos los vectores comparados deben tener la misma dimensión y el mismo orden de características.
3. Los perfiles deben ordenarse de mayor a menor similitud.
4. No se deben recomendar películas que el usuario ya haya calificado.
5. Las películas recomendadas deben pertenecer al catálogo disponible.
6. Si no existen perfiles comparables, el programa debe informar que no fue posible generar recomendaciones personalizadas.
7. Si un vector tiene magnitud cero, no se debe realizar una división entre cero.
8. El número de recomendaciones no puede superar la cantidad de películas candidatas disponibles.