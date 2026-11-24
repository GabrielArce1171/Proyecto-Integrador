1.  Caso original con resultado conocido. 

(.venv) PS C:\Users\198670-A\Documents\Proyecto-Integrador> python .\main.py

========================================
       RECOMENDADOR DE PELICULAS
========================================
1. Obtener recomendaciones
2. Salir
========================================
Selecciona una opcion: 1

--- REGISTRO DE USUARIO ---
Ingresa tu nombre: Gabriel 

CALIFICACION DE GENEROS
Califica Accion del 0 al 5: 5
Califica Comedia del 0 al 5: 5
Califica Terror del 0 al 5: 5
Califica Romance del 0 al 5: 5
Califica Ciencia ficcion del 0 al 5: 5
Califica Drama del 0 al 5: 5

CALIFICACION DE PELICULAS BASE
Califica El caballero de la noche del 0 al 5: 5
Califica Que paso ayer del 0 al 5: 5
Califica El conjuro del 0 al 5: 5
Califica Titanic del 0 al 5: 5
Califica Interestelar del 0 al 5: 5

--- COMPARANDO PERFILES ---

Similitud con los perfiles existentes:
Alejandro: 0.9016
Sebastian: 0.8958
Valentina: 0.8786
Sofia: 0.8528
Diego: 0.8173

========================================
RECOMENDACIONES PARA: GABRIEL
========================================
1. El origen - Puntuacion: 3.62/5
2. Sueños de fuga - Puntuacion: 3.61/5
3. Mision rescate - Puntuacion: 3.44/5
4. Los Vengadores - Puntuacion: 3.43/5
5. Mad Max: Furia en el camino - Puntuacion: 3.22/5



2.  Caso normal adicional con datos válidos. 


(.venv) PS C:\Users\198670-A\Documents\Proyecto-Integrador> python .\main.py

========================================
       RECOMENDADOR DE PELICULAS
========================================
1. Obtener recomendaciones
2. Salir
========================================
Selecciona una opcion: 1

--- REGISTRO DE USUARIO ---
Ingresa tu nombre: Gabriel

CALIFICACION DE GENEROS
Califica Accion del 0 al 5: 4
Califica Comedia del 0 al 5: 4
Califica Terror del 0 al 5: 5
Califica Romance del 0 al 5: 5
Califica Ciencia ficcion del 0 al 5: 1
Califica Drama del 0 al 5: 0

CALIFICACION DE PELICULAS BASE
Califica El caballero de la noche del 0 al 5: 5
Califica Que paso ayer del 0 al 5: 5
Califica El conjuro del 0 al 5: 4
Califica Titanic del 0 al 5: 0
Califica Interestelar del 0 al 5: 1

--- COMPARANDO PERFILES ---

Similitud con los perfiles existentes:
Valentina: 0.7534
Diego: 0.7406
Alejandro: 0.7325
Sebastian: 0.6292
Sofia: 0.6062


3.  Caso límite permitido por el problema. 


(.venv) PS C:\Users\198670-A\Documents\Proyecto-Integrador> python .\main.py

========================================
       RECOMENDADOR DE PELICULAS
========================================
1. Obtener recomendaciones
2. Salir
========================================
Selecciona una opcion: 1

--- REGISTRO DE USUARIO ---
Ingresa tu nombre: Gabriel 

CALIFICACION DE GENEROS
Califica Accion del 0 al 5: 5
Califica Comedia del 0 al 5: 5
Califica Terror del 0 al 5: 5
Califica Romance del 0 al 5: 5
Califica Ciencia ficcion del 0 al 5: 5
Califica Drama del 0 al 5: 5

CALIFICACION DE PELICULAS BASE
Califica El caballero de la noche del 0 al 5: 5
Califica Que paso ayer del 0 al 5: 5
Califica El conjuro del 0 al 5: 5
Califica Titanic del 0 al 5: 5
Califica Interestelar del 0 al 5: 5

--- COMPARANDO PERFILES ---

Similitud con los perfiles existentes:
Alejandro: 0.9016
Sebastian: 0.8958
Valentina: 0.8786
Sofia: 0.8528
Diego: 0.8173

========================================
RECOMENDACIONES PARA: GABRIEL
========================================
1. El origen - Puntuacion: 3.62/5
2. Sueños de fuga - Puntuacion: 3.61/5
3. Mision rescate - Puntuacion: 3.44/5
4. Los Vengadores - Puntuacion: 3.43/5
5. Mad Max: Furia en el camino - Puntuacion: 3.22/5


4.  Caso con entrada inválida. 

========================================
       RECOMENDADOR DE PELICULAS
========================================
1. Obtener recomendaciones
2. Salir
========================================
Selecciona una opcion: 1

--- REGISTRO DE USUARIO ---
Ingresa tu nombre: 1
Error: ingresa un nombre sin numeros.
Ingresa tu nombre:


5.  Caso adicional de una regla o funcionalidad relevante. 


(.venv) PS C:\Users\198670-A\Documents\Proyecto-Integrador> python .\main.py

========================================
       RECOMENDADOR DE PELICULAS
========================================
1. Obtener recomendaciones
2. Salir
========================================
Selecciona una opcion: 1

--- REGISTRO DE USUARIO ---
Ingresa tu nombre: Gabriel

CALIFICACION DE GENEROS
Califica Accion del 0 al 5: 4
Califica Comedia del 0 al 5: 4
Califica Terror del 0 al 5: 5
Califica Romance del 0 al 5: 5
Califica Ciencia ficcion del 0 al 5: 1
Califica Drama del 0 al 5: 0

CALIFICACION DE PELICULAS BASE
Califica El caballero de la noche del 0 al 5: 5
Califica Que paso ayer del 0 al 5: 5
Califica El conjuro del 0 al 5: 4
Califica Titanic del 0 al 5: 0
Califica Interestelar del 0 al 5: 1

--- COMPARANDO PERFILES ---

Similitud con los perfiles existentes:
Valentina: 0.7534
Diego: 0.7406
Alejandro: 0.7325
Sebastian: 0.6292
Sofia: 0.6062