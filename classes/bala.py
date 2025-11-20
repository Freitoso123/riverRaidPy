import pygame
from classes.entidade import Entidade

class Bala(Entidade):
    def __init__(self, pos):
        sprite = "sprites/tiro.png"
        dims = (8, 8)
        super().__init__(sprite, dims, pos)
        self.vel = 8

    def movTiro(self):
        self.y -= self.vel
