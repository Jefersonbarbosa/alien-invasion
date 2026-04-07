import sys

import pygame

class AlienInvasion:
    """Clase geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e crie recursos do jogo"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            # observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # deixa a tela desenhada mais recente visível
            pygame.display.flip()
            
if __name__ == '__main__':
    # Cria uma instância do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()
