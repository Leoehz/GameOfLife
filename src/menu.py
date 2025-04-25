import pygame
from renderer import WIDTH, HEIGHT
from conf import Escenario

pygame.init()

class Menu:
   def __init__(self):
      self.numEscenario = 0
      self.escenarios = list(Escenario)
      self.escenario = self.escenarios[0]

   def draw_start_menu(self):
      screen = pygame.display.set_mode((WIDTH, HEIGHT))
      screen.fill((0, 0, 0))
      font = pygame.font.SysFont('arial', 40)
      title = font.render('Game of Life', True, (255, 255, 255))
      start_button = font.render('Escenario => ' + self.escenario.name, True, (255, 255, 255))
      screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
      screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))
      pygame.display.update()

   def handle_events_menu(self, menu, cambio, render_game):
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
               menu = False
               render_game = True
            elif event.key == pygame.K_q:
               menu = False
               pygame.quit()
            elif event.key == pygame.K_UP:
               self.numEscenario+=1
               if self.numEscenario == len(self.escenarios):
                  self.numEscenario = 0
               self.escenario = self.escenarios[self.numEscenario]
               cambio = True
            elif event.key == pygame.K_DOWN:
               self.numEscenario-=1
               if self.numEscenario < 0:
                  self.numEscenario = len(self.escenarios) - 1
               self.escenario = self.escenarios[self.numEscenario]
               cambio = True

      return menu, cambio, render_game

   def obtenerEscenario(self):
      return self.escenario