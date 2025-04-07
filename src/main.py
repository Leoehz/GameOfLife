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
    old_grid = cargarCelulas(grid, file_name=initial_config)
    renderer.draw_cells(grid)

    estado = Estado.PAUSA

    while estado != Estado.SALIR:
        if estado == Estado.CORRIENDO:
            grid, old_grid = actualizarCeldas(grid)
            renderer.draw_cells(grid)
            estado = renderer.handle_events(estado)
            renderer.tick(TICK_RATE)

        elif estado == Estado.PAUSA:
            estado = renderer.handle_events(estado)
            if estado == Estado.AVANZA:
                grid, old_grid = actualizarCeldas(grid)
                estado = Estado.PAUSA
            elif estado == Estado.ATRASA:
                old_grid, grid = actualizarCeldas(old_grid)
                estado = Estado.PAUSA
            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

        

    pygame.quit()
    sys.exit()