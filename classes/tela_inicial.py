import pygame, random
from classes.selecao import Selecao, EstadoJogo
from classes.helicopter_tela import Helicoptero_tela
from classes.nuvem_tela import Nuvens_tela
from classes.bandeira import Bandeira_animação

largurat = 800
alturat = 600

gameDisplay = pygame.display.set_mode((largurat, alturat))
tempo = pygame.time.Clock() 

#o primeiro estado é onde tem o start e o sair e determina o primeiro selecionado 
estado_atual = EstadoJogo.SELECAO_PRINCIPAL
selecionado = 0

posicoes = []
helicopteros = []

def gera_heli_tela(qnt):
    if qnt > 1:
        helicopteros.clear()
        posicoes.clear()
    #cria uma posição aleatória para o helicoptero
    for i in range(qnt):
        posicoes.append([-1*random.randint(0, 1000), random.randint(0, 500)])
    for x, y in posicoes:
        helicopteros.append(Helicoptero_tela(x, y))
    return helicopteros

def gera_nuvem(qnt):
    #recebo a lsita de nuvens e depoias às adiciono em uma lista em ordem aleatória e tamanho determinado
    imagens_nuvem = Nuvens_tela.gera_nuvem_tela()
    nuvens = []
    for i in range(qnt):
        imagem, rect = random.choice(imagens_nuvem)
        nuvens.append((imagem, rect))
    return nuvens

def selecao_desenho():
    #mando os valores requisitados na minhas seleção conforme o estado
    if estado_atual == EstadoJogo.SELECAO_PRINCIPAL:
        Selecao().desenhar_selecao(gameDisplay, selecionado, "principal")
    
    elif estado_atual == EstadoJogo.SELECAO_DIFICULDADE:
        Selecao().desenhar_selecao(gameDisplay, selecionado, "dificuldade")

    elif estado_atual == EstadoJogo.SELECAO_TRY_AGAIN:
        Selecao().desenhar_selecao(gameDisplay, selecionado, "try_again")

def telainicial():
    global estado_atual, selecionado, dific

    img_fundo = pygame.image.load("sprites/fundo.png")
    fundo = pygame.transform.scale(img_fundo, (800, 600))
    #devolve uma lista com os helicopters
    helicopteros = gera_heli_tela(10)

    #devolve ma lista com as nuvens
    nuvem = gera_nuvem(7)

    bandeira_x = 500
    bandeira_y = 50
    bandeira = Bandeira_animação(bandeira_x, bandeira_y)

    while True:
        tempo.tick(30)

        gameDisplay.fill("royalblue4")
        gameDisplay.blit(fundo, (0, 0))

        #=======Nuvens====== 
        for imagem, rect in nuvem:
            rect.x += 2
            if rect.x >= 800:
                nuvem.remove((imagem, rect))
                novas = gera_nuvem(1)
                #adiciono apenas um elemento dessa nova lista pois senão ficará uma lista dentre as tuplas
                nuvem.append(novas[0])
            gameDisplay.blit(imagem, (rect.x, rect.y))
       
        
        #=======Helicopteros======
        for heli in helicopteros:
            
            heli.printa_helicoptero(1)
            size = heli.image.get_width()
            if size <= 42:
                heli.rect.x += 2
            elif size <= 52:
                heli.rect.x += 4
            else:
                heli.rect.x += 6
            
            #corrigido 1, agora ele não printa o grupo em si, ele printa imagem à imagem nas devidas posições
            gameDisplay.blit(heli.animado, (heli.rect.x, heli.rect.y))

        if heli.rect.x >= 800:
                helicopteros.remove(heli)
                gera_heli_tela(1)
        #=======Bandeira======
        if bandeira_x <= 50:
            bandeira_x = 50
        else:
            bandeira_x -= 4
        bandeira.rect.x = bandeira_x
        bandeira.printa_bandeira(0.1)
        #corrigido 2, agora ele não printa o grupo em si, ele printa imagem à imagem nas devidas posições
        gameDisplay.blit(bandeira.animado, (bandeira_x, bandeira_y))

        selecao_desenho()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            #=======SELEÇÃO=======
            elif evento.type == pygame.KEYDOWN:
                if estado_atual == EstadoJogo.SELECAO_PRINCIPAL:
                    #aqui eu mudo o meu selecionado e divido pelo resto da divisão para que não saia da minha lista de
                    #elementos, então nesse caso eu tenho o star e o sair, ou seja, 0 e 1 no meu vetor, e quando meu valor  
                    #tenta ser 2, ele retorna ao 0. O mesmo valo para quando tentar ser -1
                    #também vale para os que tem mais opções, basta mudar o valor da divisão conforme o tamanho
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        selecionado = (selecionado - 1) % 2
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        selecionado = (selecionado + 1) % 2

                    elif evento.key == pygame.K_RETURN:
                        if selecionado == 0: 
                            estado_atual = EstadoJogo.SELECAO_DIFICULDADE
                        #aqui eu retorno "sair" para ser identificado no meu controle de estados
                        elif selecionado == 1:  
                            return "sair"
                        
                elif estado_atual == EstadoJogo.SELECAO_DIFICULDADE:
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        selecionado = (selecionado - 1) % 4
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        selecionado = (selecionado + 1) % 4

                    elif evento.key == pygame.K_BACKSPACE:
                        #posso retorar ao menu principal
                        estado_atual = EstadoJogo.SELECAO_PRINCIPAL
                        selecionado = 0
                    elif evento.key == pygame.K_RETURN:
                        #seleciono minha dificuldade
                        if selecionado == 0:    # FÁCIL
                            dific = 4
                            return dific, False
                        elif selecionado == 1:  # NORMAL
                            dific = 6
                            return dific, False
                        elif selecionado == 2:  # DIFÍCIL
                            dific = 8
                            return dific, False
                        elif selecionado == 3:  # Deleta jogo
                            dific = 10
                            return dific, True
                        
        pygame.display.update()

def Gameover():
    global estado_atual, selecionado

    img_fundo = pygame.image.load("sprites/animação/game over/fundo_game_over.png")
    fundo = pygame.transform.scale(img_fundo, (800, 600))

    estado_atual = EstadoJogo.SELECAO_TRY_AGAIN
    selecionado = 0

    while True:
        tempo.tick(30)
        gameDisplay.fill("royalblue4")
        gameDisplay.blit(fundo, (0, 0))

        selecao_desenho()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            #=======SELEÇÃO_GAME_OVER=======
            elif evento.type == pygame.KEYDOWN:
                if estado_atual == EstadoJogo.SELECAO_TRY_AGAIN:
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        selecionado = (selecionado - 1) % 2
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        selecionado = (selecionado + 1) % 2

                    elif evento.key == pygame.K_RETURN:
                        if selecionado == 0: 
                            estado_atual = EstadoJogo.SELECAO_PRINCIPAL
                            selecionado = 0
                            #não retorna nada pois nesse caso o proximo estado sempre será o menu
                            return 
                        elif selecionado == 1:  
                            return "sair"

        pygame.display.update()