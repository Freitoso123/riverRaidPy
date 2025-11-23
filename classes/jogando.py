import pygame, random, time
from classes.aviao import Aviao
from classes.helic import *
from classes.mapa import *
from classes.pontuacao import pontuacao

#criei um função separada para a lógica do jogo por conta da administração de estados do jogo, para que fosse possivel
#recomeçar o jogo
def Jogando(dif):
    #começo recebendo a dificuldade, que veio da minha tela inicial
    pygame.init()

    largurat = 800
    alturat = 600
    
    gameDisplay = pygame.display.set_mode((largurat, alturat))
    pygame.display.set_caption('aviãozinho explode tudo') 
    tempo = pygame.time.Clock() 

    player = Aviao()

    helic_list = []

    balas = []
    reload_time = 0.25
    lastShot = 0

    map_list = []
    first_map = True

    col_player = False

    pontos = 0
    pontuacao(pontos)

    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                #retorna sair para o meu controle de estados identificar a saida
                return "sair"

        gameDisplay.fill("royalblue4")
        tempo.tick(30)

        tecla = pygame.key.get_pressed()

        #gerar bala
        if tecla[pygame.K_SPACE] and (time.time() - lastShot) >= reload_time:
            balas.append(player.atirar())
            lastShot = time.time()

        #gerar helicopteros
        if random.randint(0,1000) > 330 and len(helic_list) < 10:
            #aquie eu recebo a dificuldade selecionada
            helic_list.append(gerarhelic(dif))

        #adiciona 1o modulo a lista de mapas
        if first_map:
            map_list.append(gerarMapa())
            first_map = False

        #for das entidades
        for module in map_list:
            module.imprimir()
            module.queda(tecla)
            
            #apagar modulo que passa da tela
            if module.y > 960:
                map_list.remove(module)

            #gerar modulo
            if module.y > 0 and len(map_list) < 2:
                map_list.append(gerarMapa())
                newMapTime = 0

            #gameOver
            if module.colisaoMask(player):
                return

        for bala in balas:
            bala.imprimir()
            bala.movTiro()

            #apagar bala fora da tela
            if bala.y < -32:
                balas.remove(bala)
        
        for helic in helic_list:
            helic.imprimir()
            helic.movHoriz()
            helic.queda(tecla)

            #apagar helicopteros que passaram da tela
            if helic.y > 832:
                helic_list.remove(helic)

            #gameOver
            if helic.colisaoMask(player):
                col_player = True

            #apagar helicopteros acertador por balas
            for bala in balas:
                helic_hitted = helic.colisaoRect(bala)
                if helic_hitted == True:
                    helic_list.remove(helic)
                    balas.remove(bala)
                    pontos += 60
        pontuacao(pontos)


        #gameOver
        if col_player == True:
            #não retorna nada pois o meu próximo estado é game_over
            return

        player.imprimir()
        player.movPlayer(tecla)

        pygame.display.update()