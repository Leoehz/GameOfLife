from renderer import Renderer
from conf import GRID_SIZE, TICK_RATE, Estado, Celula
import pygame

if __name__ == "__main__" :
    renderer = Renderer()

    # Inicializar grilla vacia
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    # TODO: Cargar valores desde config/initial_state.txt

    estado = Estado.CORRIENDO
    while estado in (Estado.CORRIENDO, Estado.PAUSA):
        if estado == Estado.CORRIENDO:

            grid[10][11] = Celula.MUERTA
            grid[10][10] = Celula.VIVA
            estado = renderer.handle_events(estado)
            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

            grid[10][10] = Celula.MUERTA
            grid[10][11] = Celula.VIVA

            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

        elif estado == Estado.PAUSA:
            estado = renderer.handle_events(estado)
            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

    pygame.quit()