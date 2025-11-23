import pygame

class Bandeira_animação():
    def __init__(self, pos_anim_x, pos_anim_y):
        #lista de sprites
        self.bandeiras = [
            pygame.image.load("sprites/animação/bandeira/bandeira_0.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_1.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_2.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_3.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_4.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_3.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_2.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_1.png")
        ]
        #valor para a mudança de imagens
        self.imagem_inicial = 0
        #receba a imagem correspodente
        self.animado = self.bandeiras[self.imagem_inicial]

        #pega o retangulo para move-lo
        self.rect = self.animado.get_rect()
        self.rect.topleft = [pos_anim_x, pos_anim_y]

    def printa_bandeira(self, velocidade):

        self.imagem_inicial += velocidade
        
        if self.imagem_inicial >= len(self.bandeiras):
            self.imagem_inicial = 0
        #receba o proximo sprite
        self.animado = self.bandeiras[int(self.imagem_inicial)]
        self.image = self.animado