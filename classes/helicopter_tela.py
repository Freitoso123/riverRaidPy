import pygame
import random

class Helicoptero_tela(pygame.sprite.Sprite):
    def __init__(self, pos_anim_x, pos_anim_y):
        super().__init__()
        self.heli = []
        self.heli.append(pygame.image.load("sprites/animação/heli\helic3.png"))
        self.heli.append(pygame.image.load("sprites/animação/heli\helic2.png"))
        self.heli.append(pygame.image.load("sprites/animação/heli\helic1.png"))
        self.heli.append(pygame.image.load("sprites/animação/heli\helic0.png"))
        
        tamanho = random.randint(32, 64)

        for i in range(len(self.heli)):
            self.heli[i] = pygame.transform.scale(self.heli[i], (tamanho, tamanho))

        self.imagem_inicial = 0
        self.animado = self.heli[self.imagem_inicial]

        self.rect = self.animado.get_rect()
        self.rect.topleft = [pos_anim_x, pos_anim_y]

    def printa_helicoptero(self, velocidade):
        
        self.imagem_inicial += velocidade
        
        if self.imagem_inicial >= len(self.heli):
            self.imagem_inicial = 0
        self.animado = self.heli[int(self.imagem_inicial)]
        self.image = self.animado