import heapq

# Definición del mapa, Es una matriz que representa el terreno donde se realizará la búsqueda de ruta
# 0: Caminos transitables.
# 1: Obstáculos que no se pueden atravesar.
mapa = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
]

# Función para encontrar la ruta más corta usando A*
def encontrar_ruta(mapa, inicio, fin):
    # Direcciones posibles: arriba, abajo, izquierda, derecha (movimientos en la matriz)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #Variables que almacenan el número de filas y columnas del mapa, respectivamente.
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    # Función heurística: distancia Manhattan
    # implementa una heurística basada en la distancia Manhattan para calcular la distancia aproximada 
    # entre dos puntos en una cuadrícula o espacio bidimensional.
    def heuristica(pos_actual, pos_final):
        return abs(pos_actual[0] - pos_final[0]) + abs(pos_actual[1] - pos_final[1])
    
    # Inicialización de A*
    heap = [(0, inicio)] # Inicialización del heap con el nodo inicial y costo cero
    heapq.heapify(heap) # Convertir lista en heap
    padres = {inicio: None} # Diccionario que almacenará el nodo padre de cada nodo en el camino más corto encontrado.
    costos = {inicio: 0} # Diccionario para almacenar costos acumulados hasta cada nodo
    
    while heap:
        costo_actual, nodo_actual = heapq.heappop(heap) # Extraer nodo con menor costo actual
        
        if nodo_actual == fin: #Se verifica si se ha alcanzado el nodo fin. Si es así, se detiene la búsqueda.
            break
        
        for direccion in direcciones: #Se itera sobre las direcciones posibles para moverse desde nodo_actual.
           #Calcula las coordenadas del vecino según la dirección actual.
            vecino = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            
            #Verifica que el vecino esté dentro de los límites del mapa.
            if 0 <= vecino[0] < num_filas and 0 <= vecino[1] < num_columnas:
                nuevo_costo = costo_actual + 1  #Calcula el nuevo costo acumulado para llegar al vecino desde inicio.
                
                #Verifica si el vecino es transitable y si se ha encontrado un nuevo camino más corto a este vecino.
                if mapa[vecino[0]][vecino[1]] != 1 and (vecino not in costos or nuevo_costo < costos[vecino]):
                    #Actualiza el costo acumulado y el nodo padre del vecino.
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, fin)
                    #Agrega el vecino al heap de prioridad con su prioridad calculada 
                    heapq.heappush(heap, (prioridad, vecino))
                    padres[vecino] = nodo_actual
    
    # Lista que almacenará la ruta desde inicio hasta fin.
    ruta = []
    nodo = fin
    #Reconstruye la ruta retrocediendo desde fin hasta inicio usando el diccionario padres.
    while nodo is not None:
        ruta.append(nodo)
        nodo = padres[nodo]
    #Invierte la lista ruta para obtener la ruta en el orden correcto desde inicio hasta fin.
    ruta.reverse()
    
    #contiene las coordenadas de las celdas desde inicio hasta fin representando la ruta más corta encontrada.
    return ruta
# Función para mostrar el mapa con la ruta encontrada
def mostrar_mapa_con_ruta(mapa, ruta):
    # Crea una copia visual del mapa para mostrar la ruta
    # Reemplaza celdas transitables (0) con '.' y obstáculos (1) con 'X'
    mapa_visual = [['.' if celda == 0 else 'X' for celda in fila] for fila in mapa]
    
    # Marca la ruta encontrada en el mapa visual con '*'
    for paso in ruta:
        mapa_visual[paso[0]][paso[1]] = '*'
    
    # Imprime el mapa visual celda por celda
    for fila in mapa_visual:
        print(' '.join(fila))

# Función para agregar obstáculos en el mapa
def agregar_obstaculos(mapa, obstaculos):
    # Itera sobre cada coordenada de obstáculo proporcionada
    for obstaculo in obstaculos:
        # Verifica que las coordenadas del obstáculo estén dentro de los límites del mapa
        if 0 <= obstaculo[0] < len(mapa) and 0 <= obstaculo[1] < len(mapa[0]):
            # Establece la celda correspondiente en el mapa a 1 (obstáculo)
            mapa[obstaculo[0]][obstaculo[1]] = 1
    # Retorna el mapa actualizado con los obstáculos agregados
    return mapa

# Verificación de coordenadas válidas
def coordenadas_validas(mapa, coordenadas):
    # Verifica que las coordenadas estén dentro de los límites del mapa
    # y que la celda correspondiente sea transitable (0)
    return (0 <= coordenadas[0] < len(mapa) and 
            0 <= coordenadas[1] < len(mapa[0]) and 
            mapa[coordenadas[0]][coordenadas[1]] == 0)

# Ejemplo de uso
if __name__ == "__main__":
    # Imprime el mapa inicial
    print("Mapa inicial:")
    for fila in mapa:
        # Representa celdas transitables (0) con '.' y obstáculos (1) con 'X'
        print(' '.join('.' if celda == 0 else 'X' for celda in fila))
    
    # Ingresar obstáculos
    obstaculos = []
    while True:
        # Solicita al usuario que ingrese coordenadas de un obstáculo
        entrada = input("Ingresa coordenadas de un obstáculo (formato x,y) o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            # Si el usuario ingresa 'fin', termina el ingreso de obstáculos
            break
        # Divide la entrada en coordenadas x e y y las convierte en enteros
        x, y = map(int, entrada.split(','))
        # Agrega las coordenadas a la lista de obstáculos
        obstaculos.append((x, y))
    
    # Actualiza el mapa con los obstáculos ingresados
    mapa = agregar_obstaculos(mapa, obstaculos)
    
    # Imprime el mapa con los obstáculos agregados
    print("\nMapa con obstáculos:")
    for fila in mapa:
        # Representa celdas transitables (0) con '.' y obstáculos (1) con 'X'
        print(' '.join('.' if celda == 0 else 'X' for celda in fila))
    
    # Ingresar punto de partida y destino final
    while True:
        # Solicita al usuario que ingrese las coordenadas de inicio
        inicio = tuple(map(int, input("Ingresa coordenadas de inicio (formato x,y): ").split(',')))
        # Verifica que las coordenadas de inicio sean válidas
        if coordenadas_validas(mapa, inicio):
            break
        print("Coordenadas no válidas o es un obstáculo. Intenta de nuevo.")
    
    while True:
        # Solicita al usuario que ingrese las coordenadas de destino
        fin = tuple(map(int, input("Ingresa coordenadas de destino (formato x,y): ").split(',')))
        # Verifica que las coordenadas de destino sean válidas
        if coordenadas_validas(mapa, fin):
            break
        print("Coordenadas no válidas o es un obstáculo. Intenta de nuevo.")
    
    # Encuentra la ruta más corta desde el inicio hasta el destino
    ruta_encontrada = encontrar_ruta(mapa, inicio, fin)
    
    # Imprime el mapa con la ruta más corta encontrada
    print("\nMapa con ruta más corta:")
    mostrar_mapa_con_ruta(mapa, ruta_encontrada)
