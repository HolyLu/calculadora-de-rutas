
# Algoritmo de Búsqueda de Rutas con A*

Este proyecto implementa un algoritmo de búsqueda de rutas usando el algoritmo A*. El programa permite definir un mapa con caminos transitables y obstáculos, agregar obstáculos adicionales, y encontrar la ruta más corta desde un punto de inicio a un punto de destino.
Descripción del Mapa

El mapa se define como una matriz bidimensional, donde:

    0 representa un camino transitable.
    1 representa un obstáculo que no se puede atravesar.
Funciones Principales
1. encontrar_ruta(mapa, inicio, fin)

Encuentra la ruta más corta desde el punto de inicio al punto de destino usando el algoritmo A*.

    Parámetros:
        mapa: La matriz que representa el mapa.
        inicio: Tupla con las coordenadas del punto de inicio (x, y).
        fin: Tupla con las coordenadas del punto de destino (x, y).

    Retorna:
        Una lista de tuplas con las coordenadas de la ruta más corta.

2. mostrar_mapa_con_ruta(mapa, ruta)

Muestra el mapa con la ruta encontrada marcada.

    Parámetros:
        mapa: La matriz que representa el mapa.
        ruta: Lista de tuplas con las coordenadas de la ruta.

3. agregar_obstaculos(mapa, obstaculos)

Agrega obstáculos al mapa en las coordenadas especificadas.

    Parámetros:
        mapa: La matriz que representa el mapa.
        obstaculos: Lista de tuplas con las coordenadas de los obstáculos a agregar.

    Retorna:
        El mapa actualizado con los obstáculos agregados.

4. coordenadas_validas(mapa, coordenadas)

Verifica si las coordenadas son válidas y transitables.

    Parámetros:
        mapa: La matriz que representa el mapa.
        coordenadas: Tupla con las coordenadas a verificar (x, y).

    Retorna:
        True si las coordenadas son válidas y transitables, False en caso contrario.

Ejecución del Programa

El programa principal permite al usuario:

    Ver el mapa inicial.
    Ingresar coordenadas de obstáculos adicionales.
    Verificar que las coordenadas de inicio y destino sean válidas.
    Encontrar y mostrar la ruta más corta.

Ejemplo de Uso

    Ejecuta el script. Se mostrará el mapa inicial.
    Ingresa las coordenadas de los obstáculos en el formato x,y. Cuando termines, ingresa fin.
    Ingresa las coordenadas del punto de inicio y destino en el formato x,y.
    El programa encontrará y mostrará la ruta más corta.

Requisitos

    Python 3.x

Ejecución

Para ejecutar el programa, guarda el código en un archivo, por ejemplo, ruta_astar.py, y ejecuta el script usando Python:
