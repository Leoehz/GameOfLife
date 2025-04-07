from enum import Enum, StrEnum
import os
import re

nombre_archivo = 'initial_state.txt'
nombre_archivo = 'test.txt'
nombre_archivo = 'chaos.txt'
nombre_archivo = 'naves.txt'

TICK_RATE = 5

# Tamaños de celda y celula
GRID_SIZE = 25
CELL_SIZE = 20

class Celula(Enum):
    VIVA = 1
    MUERTA = 0

class Estado(Enum):
    CORRIENDO = 1
    PAUSA = 2
    SALIR = 0
    AVANZA = 4
    ATRASA = 5

class Color(tuple, Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRID = (200, 200, 200)
    CELL = (50, 150, 50)

    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    
class Escenario(StrEnum):
    NAVES = 'naves.txt'
    CAOS = 'chaos.txt'
    PULSAR = 'pulsar.txt'
    DIEHARD = 'diehard.txt'

def cargarCelulas(grid: list[list[Celula]], file_name: Escenario):
    ruta_rel = '../config/'
    path = ruta_rel + file_name
    celdas_con_celulas = []

    with open(path, 'r') as file_to_read:
        for line in file_to_read:
            if re.match(r'\d+,\d+', line):
                x, y = line.split(',')
                celdas_con_celulas.append([int(x), int(y)])

    for par in celdas_con_celulas:
        grid[par[0]][par[1]] = Celula.VIVA

    return grid