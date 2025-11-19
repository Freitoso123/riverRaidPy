import pygame
from classes.helicopter_tela import Helicoptero_tela


class Selecao():
    def __init__(self):

        self.selecao_1 = [
            [
                pygame.image.load("sprites/animação\seleção\star_0.png").convert_alpha(),
                pygame.image.load("sprites/animação\seleção\star_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação\seleção\sair_0.png").convert_alpha(),
                pygame.image.load("sprites/animação\seleção\sair_1.png").convert_alpha()
            ],
        ]

        self.dificuldade = pygame.image.load("sprites/animação\seleção\dificuldade.png")

        self.seta = pygame.image.load("sprites/animação\seleção\seta.png")

        self.dificuldade_selecao = [
            [
                pygame.image.load("sprites/animação/seleção/nivel1_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/nivel1_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação/seleção/nivel2_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/nivel2_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação/seleção/nivel3_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/nivel3_1.png").convert_alpha()  
            ],
            [
                pygame.image.load("sprites/animação/seleção/deleta_jogo_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/deleta_jogo_1.png").convert_alpha()  
            ]
        ]
        self.game_over_select = [
            [
                pygame.image.load("sprites/animação\game over/try_again_0.png").convert_alpha(),
                pygame.image.load("sprites/animação\game over/try_again_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação\seleção\sair_0.png").convert_alpha(),
                pygame.image.load("sprites/animação\seleção\sair_1.png").convert_alpha()
            ]
        ]
        self.game_over = [
             [
                pygame.image.load("sprites/animação\game over\game_over_0.png").convert_alpha(),
                pygame.image.load("sprites/animação\game over\game_over_1.png").convert_alpha()
            ]
        ]

        self.frame_atual = 1

    def desenhar_selecao(self, tela, selecionado, selecao_tipo):

        if selecao_tipo == "principal":
            sprites = self.selecao_1
            num_itens = 2
            titulo = None
        elif selecao_tipo == "dificuldade":
            sprites = self.dificuldade_selecao
            num_itens = 4
            titulo = self.dificuldade
        elif selecao_tipo == "try_again":
            sprites = self.game_over_select
            num_itens = 2
            titulo = self.game_over

        if titulo:
            if selecao_tipo == "try_again":
                titulo_img = titulo[int(self.frame_atual)]
                tela.blit(titulo_img, (400 - (titulo_img.get_width()//2), 200))
            else:
                tela.blit(titulo, (400 - (titulo.get_width()//2), 300))

        for i in range(num_itens):
            if i == selecionado:
                imagem = sprites[i][int(self.frame_atual)]
                seta = True
            else:
                imagem = sprites[i][0]
                seta = False

            rect = imagem.get_rect()
            largura = imagem.get_width()
            x_pos = 400 - (largura//2)

            if selecao_tipo == "principal":
                y_pos = 300 + i* 65
            elif selecao_tipo == "dificuldade":
                y_pos = 350 + i * 45
            else:
                y_pos = 350 + i * 45

            rect.y = y_pos
            rect.x = x_pos

            tela.blit(imagem, rect)
            if seta:
                tela.blit(self.seta, (x_pos-30, y_pos))

        self.frame_atual += 0.1
        if self.frame_atual >= 2:
            self.frame_atual = 1
class EstadoJogo:
    SELECAO_PRINCIPAL = "principal"
    SELECAO_DIFICULDADE = "dificuldade"
    SELECAO_TRY_AGAIN = "try_again"
        