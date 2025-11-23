import pygame, random
from classes.caem import Caem

class Mapa(Caem):
    def __init__(self, mapModule, velY):
        modulesList = ["map0.png", "map1.png", "map2.png"]
        sprite = "sprites/maps/" + modulesList[mapModule]
        height = (960, 960, 960)
        dims=(800, height[mapModule])
        self.dims = dims
        pos = [0, -1*dims[1]]
        super().__init__(sprite, dims, pos, velY)

def gerarMapa():
    return Mapa((random.randint(0,2)), 7)
