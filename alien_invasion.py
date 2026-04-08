import sys

import pygame

class AlienInvasion:
    """Clase geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e crie recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Define a cor do background
        self.bg_color = (130, 130, 130)

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            # observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.bg_color)

            # deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Cria uma instância do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()
