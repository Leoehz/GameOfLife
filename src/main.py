from renderer import Renderer
from conf import GRID_SIZE, TICK_RATE, Estado, Celula, Escenario, cargarCelulas
from game import actualizarCeldas
import pygame
import sys
from menu import *

if __name__ == "__main__" :
    esMenu = True
    menu = Menu()
    escenarios = list(Escenario)
    cambio = False
    render_game = False
    menu.draw_start_menu()
    while esMenu:
        #print(list(Escenario))
        esMenu, cambio, render_game = menu.handle_events_menu(esMenu, cambio, render_game)
        #print(esMenu)
        if cambio:
            menu.draw_start_menu()
            cambio = False
    if render_game:
        initial_config = menu.obtenerEscenario()#Escenario.CAOS

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