from conf import (Celula, Estado, Color,
                  GRID_SIZE, CELL_SIZE, TICK_RATE,)
import pygame

# Configuración de la pantalla
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE

class Renderer:
    def __init__(self, grid: list[list[Celula]]):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()
        self.grid = grid

    def set_grid(self, grid: list[list[Celula]]):
        self.grid = grid

    def draw_grid(self):
        """Dibuja la grilla del tablero."""
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID, (0, y), (WIDTH, y))

    def draw_cells(self, grid):
        """Dibuja las células en función del estado actual del juego."""
        self.screen.fill(Color.WHITE)
        self.set_grid(grid)
        self.draw_grid()

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == Celula.VIVA:
                    pygame.draw.rect(surface=self.screen, color=Color.CELL, 
                                     rect=(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()  # Actualiza la pantalla

    def handle_events(self, estado: Estado):
        """Maneja los eventos de Pygame, como cerrar la ventana."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Estado.SALIR
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return Estado.CORRIENDO
                elif event.key == pygame.K_q:
                    return Estado.SALIR
                elif event.key == pygame.K_SPACE:
                    return Estado.PAUSA

        return estado

    def tick(self, fps=TICK_RATE):
        """Controla la velocidad de actualización del juego."""
        self.clock.tick(fps)
