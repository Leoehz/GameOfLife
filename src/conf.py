from enum import Enum
import os

nombre_archivo = 'initial_state.txt'

class Celula(Enum):
    VIVA = 1
    MUERTA = 0

class Estado(Enum):
    CORRIENDO = 1
    PAUSA = 2
    SALIR = 3

TICK_RATE = 5

# Tamaños de celda y celula
GRID_SIZE = 6
CELL_SIZE = 20

# Definir colores
WHITE = (255, 255, 255)
GRID_COLOR = (200, 200, 200)
CELL_COLOR = (50, 150, 50)

def cargarCelulas(grid):
    ruta_rel = os.path.dirname(os.getcwd().replace('\\', '/')) + '/config/'
    path = ruta_rel + nombre_archivo
    celdas_con_celulas = []

    with open(path, 'r') as file_to_read:
        for line in file_to_read:
            x, y = line.split(',')
            #print(x, y)
            celdas_con_celulas.append([int(x), int(y)])

    for par in celdas_con_celulas:
        grid[par[0]][par[1]] = Celula.VIVA

    #for fila in grid:
    #    print(" ".join(map(str, fila)))

    return grid