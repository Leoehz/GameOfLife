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
    ya_atraso = False

    while estado != Estado.SALIR:
        if estado == Estado.CORRIENDO:
            grid, old_grid = actualizarCeldas(grid)
            renderer.next_generation(grid)
            ya_atraso = False

        elif estado == Estado.PAUSA:
            pass

        elif estado == Estado.AVANZA:
                grid, old_grid = actualizarCeldas(grid)
                renderer.next_generation(grid)
                estado = Estado.PAUSA
                ya_atraso = False

        elif estado == Estado.ATRASA:
                if not ya_atraso:  
                    renderer.prev_generation(old_grid)
                    grid = old_grid
                    ya_atraso = True
                estado = Estado.PAUSA

        estado = renderer.handle_events(estado)
        renderer.tick(TICK_RATE)

        

    pygame.quit()
    sys.exit()