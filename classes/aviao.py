import pygame
from classes.entidade import Entidade
from classes.bala import Bala

class Aviao(Entidade):
    def __init__(self):
        sprite = "sprites/player.png"
        dims = (32, 32)
        pos = [384, 500]
        super().__init__(sprite, dims, pos)
        self.vel = 5

    def movPlayer(self, teclas):
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.vel
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.vel
    
    def atirar(self):
        bala = Bala((self.x+8, self.y-8))
        return bala

