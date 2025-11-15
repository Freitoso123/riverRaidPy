import pygame
from classes.entidade import Entidade

class Caem(Entidade):
    def __init__(self, sprite, dims, pos, velY):
        super().__init__(sprite, dims, pos)
        self.velY = velY

    def queda(self, teclas):
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y += self.velY*4
        else:
            self.y += self.velY
