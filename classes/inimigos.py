import pygame
from classes.caem import Caem

class Inimigos(Caem):
    def __init__(self, sprite, dims, pos, velY, direcao, velx):
        super().__init__(sprite, dims, pos, velY)
        self.velx = velx
        self.direcao = direcao

    def movHoriz(self):
        if self.y >= 300:
            if self.direcao == 1:
                self.x += self.velx
            else:
                self.x -= self.velx
    
