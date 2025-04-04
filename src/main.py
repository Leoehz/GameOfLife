from renderer import Renderer
from conf import GRID_SIZE, TICK_RATE, Estado, Celula, Escenario, cargarCelulas
from game import actualizarCeldas
import pygame
import sys

if __name__ == "__main__" :

    initial_config = Escenario.CAOS

    # Inicializar grilla vacia
    grid = [[Celula.MUERTA] * GRID_SIZE for _ in range(GRID_SIZE)]
    renderer = Renderer(grid)
    grid = cargarCelulas(grid, file_name=initial_config)
    renderer.draw_cells(grid)

    estado = Estado.PAUSA

    while estado != Estado.SALIR:
        if estado == Estado.CORRIENDO:
            grid = actualizarCeldas(grid)
            renderer.draw_cells(grid)

        elif estado == Estado.PAUSA:
            # TODO: Agregar logica adicional (siguiente gen por ejemplo)
            pass
        estado = renderer.handle_events(estado)
        renderer.tick(TICK_RATE)

    pygame.quit()
    sys.exit()