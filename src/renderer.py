from conf import (Celula, Estado, Color,
                  GRID_SIZE, CELL_SIZE, FONT_SIZE, TICK_RATE,)
import pygame

# Configuración de la pantalla
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE + FONT_SIZE

class Renderer:
    def __init__(self, grid: list[list[Celula]]):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("Console", FONT_SIZE)
        self.clock = pygame.time.Clock()
        
        self.live_cells = 0
        self.generation = 1
        self.grid = grid

    def set_grid(self, grid: list[list[Celula]]):
        self.grid = grid

    def draw_grid(self):
        """Dibuja la grilla del tablero."""
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID, (x, 0), (x, HEIGHT-FONT_SIZE))
        for y in range(0, HEIGHT-FONT_SIZE+1, CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID, (0, y), (WIDTH, y))

    def draw_text(self):
        text = f"Generacion {self.generation} - Celulas {self.live_cells}"
        text_surface = self.font.render(text, True, Color.BLACK)
        text_rect = text_surface.get_rect()

        text_rect.centerx = WIDTH // 2
        text_rect.bottom = HEIGHT + 2
        self.screen.blit(text_surface, text_rect)

    def draw_cells(self, grid):
        """Dibuja las células en función del estado actual del juego."""
        self.screen.fill(Color.WHITE)
        self.set_grid(grid)
        self.draw_grid()
        self.live_cells = 0

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == Celula.VIVA:
                    pygame.draw.rect(surface=self.screen, color=Color.CELL, 
                                     rect=(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    self.live_cells += 1

        self.draw_text()
        pygame.display.flip()  # Actualiza la pantalla

    def next_generation(self, grid):
        self.generation += 1
        self.draw_cells(grid)
    
    def prev_generation(self, grid):
        self.generation -= 1
        self.draw_cells(grid)

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
                elif event.key == pygame.K_SPACE and estado != Estado.PAUSA:
                    return Estado.PAUSA
                elif event.key == pygame.K_SPACE and estado == Estado.PAUSA:
                    return Estado.CORRIENDO
                elif event.key == pygame.K_RIGHT and estado == Estado.PAUSA:
                    return Estado.AVANZA
                elif event.key == pygame.K_LEFT and estado == Estado.PAUSA:
                    return Estado.ATRASA

        return estado

    def tick(self, fps=TICK_RATE):
        """Controla la velocidad de actualización del juego."""
        self.clock.tick(fps)
