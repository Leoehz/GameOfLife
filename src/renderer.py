from conf import (Celula, Estado, 
                  GRID_SIZE, CELL_SIZE, TICK_RATE,
                  WHITE, GRID_COLOR, CELL_COLOR)
import pygame

# Configuración de la pantalla
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        """Dibuja la grilla del tablero."""
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw_cells(self, grid):
        """Dibuja las células en función del estado actual del juego."""
        self.screen.fill(WHITE)
        self.draw_grid()

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == Celula.VIVA:
                    pygame.draw.rect(surface=self.screen, color=CELL_COLOR, 
                                     rect=(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()  # Actualiza la pantalla

    def handle_events(self, estado: Estado):
        """Maneja los eventos de Pygame, como cerrar la ventana."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Estado.SALIR
            
            elif event.type == pygame.KEYDOWN:
                print('Se entro al evento')
                if event.key == pygame.K_b:
                    print('Se presiono B')
                    return Estado.CORRIENDO
                elif event.key == pygame.K_q:
                    print('Se presiono Q')
                    return Estado.SALIR
                elif event.key == pygame.K_SPACE:
                    print('Se presiono Space')
                    return Estado.PAUSA

        return estado

    def tick(self, fps=TICK_RATE):
        """Controla la velocidad de actualización del juego."""
        self.clock.tick(fps)
