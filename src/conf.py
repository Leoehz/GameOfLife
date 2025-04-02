from enum import Enum

class Celula(Enum):
    VIVA = 1
    MUERTA = 0

class Estado(Enum):
    CORRIENDO = 1
    PAUSA = 2
    SALIR = 3

TICK_RATE = 5

# Tamaños de celda y celula
GRID_SIZE = 25
CELL_SIZE = 20

# Definir colores
WHITE = (255, 255, 255)
GRID_COLOR = (200, 200, 200)
CELL_COLOR = (50, 150, 50)