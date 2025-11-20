import pygame
#lista de estados
class EstadoJogo:
    SELECAO_PRINCIPAL = "principal"
    SELECAO_DIFICULDADE = "dificuldade"
    SELECAO_TRY_AGAIN = "try_again"

class Selecao():
    def __init__(self):
        #lista de diversos sprites
        self.selecao_1 = [
            [
                pygame.image.load("sprites/animação/seleção/star_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/star_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação/seleção/sair_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/sair_1.png").convert_alpha()
            ],
        ]

        self.dificuldade = pygame.image.load("sprites/animação/seleção/dificuldade.png")

        self.seta = pygame.image.load("sprites/animação/seleção/seta.png")

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
                pygame.image.load("sprites/animação/game over/try_again_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/game over/try_again_1.png").convert_alpha()
            ],
            [
                pygame.image.load("sprites/animação/seleção/sair_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/seleção/sair_1.png").convert_alpha()
            ]
        ]
        self.game_over = [
                pygame.image.load("sprites/animação/game over/game_over_0.png").convert_alpha(),
                pygame.image.load("sprites/animação/game over/game_over_1.png").convert_alpha()
        ]

        self.frame_atual = 1

    def desenhar_selecao(self, tela, selecionado, selecao_tipo):
        #os valores recebido vieram da tela inicial
        #dependedo do estado há um grupo de sprites e um numero de itens
        if selecao_tipo == "principal":
            sprites = self.selecao_1
            num_itens = 2
        elif selecao_tipo == "dificuldade":
            sprites = self.dificuldade_selecao
            num_itens = 4
            #no caso da dificuldade e do try_again, há imagens estáticas, então apenas às adiciono na tela
            tela.blit(self.dificuldade, (400 - (self.dificuldade.get_width()//2), 300))
        elif selecao_tipo == "try_again":
            sprites = self.game_over_select
            num_itens = 2
            gameover = self.game_over[self.frame_atual]
            tela.blit(gameover, ((400 - gameover.get_width()//2), 150))

        for i in range(num_itens):
            if i == selecionado:
                #para cada item eu mudo o sprite, para dar um destaque á ele e habilito a seta
                imagem = sprites[i][self.frame_atual]
                seta = True
            else:
                imagem = sprites[i][0]
                seta = False

            rect = imagem.get_rect()
            largura = imagem.get_width()
            x_pos = 400 - (largura//2)

            #posiciono cada grupo de sprites com base no seu valor i, que se refere a quantidade de itens que terá no menu
            if selecao_tipo == "principal":
                #então entre os itens terá uma distancha de 65 pixeis entre cada um
                y_pos = 300 + i * 65
            elif selecao_tipo == "dificuldade":
                y_pos = 350 + i * 45
            else:
                y_pos = 400 + i * 45

            rect.y = y_pos
            rect.x = x_pos

            tela.blit(imagem, rect)
            #printo a seta
            if seta:
                tela.blit(self.seta, (x_pos-30, y_pos))


        