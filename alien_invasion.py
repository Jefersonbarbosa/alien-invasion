import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Clase geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e crie recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()       
            self.clock.tick(60)

    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False

    def _update_screen(self):
         """Atualiza as imagens na tela e mude para a nova tela"""
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()

        # deixa a tela desenhada mais recente visível
         pygame.display.flip()


if __name__ == '__main__':
    # Cria uma instância do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()
