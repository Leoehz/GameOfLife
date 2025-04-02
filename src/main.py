from renderer import Renderer
from conf import GRID_SIZE, TICK_RATE, Estado, Celula, cargarCelulas
from game import actualizarCeldas
import pygame

if __name__ == "__main__" :
    renderer = Renderer()

    # Inicializar grilla vacia
    grid = [[Celula.MUERTA] * GRID_SIZE for _ in range(GRID_SIZE)]
    grid = cargarCelulas(grid)

    # TODO: Cargar valores desde config/initial_state.txt

    estado = Estado.CORRIENDO
    while estado in (Estado.CORRIENDO, Estado.PAUSA):
        if estado == Estado.CORRIENDO:
            # TODO: Eliminar hardcodeo y dinamizar con game.py
            #grid[10][11] = Celula.MUERTA
            #grid[10][10] = Celula.VIVA
            grid = actualizarCeldas(grid)
            estado = renderer.handle_events(estado)
            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

            #grid[10][10] = Celula.MUERTA
            #grid[10][11] = Celula.VIVA

            #renderer.draw_cells(grid)
            #renderer.tick(TICK_RATE)

        elif estado == Estado.PAUSA:
            estado = renderer.handle_events(estado)
            renderer.draw_cells(grid)
            renderer.tick(TICK_RATE)

    pygame.quit()