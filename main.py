import pygame
from classes.tela_inicial import *
from classes.jogando import *
from desinstalar import *
from GrabBanner import *

#separei o main como meu controle principal de estados, para que fosse possivel transitar entre as telas sem nenhum problema
#sem tentar chamar funções dentro de funções ou fazer loops 

#estados possiveis do meu jogo
class Estados:
    estado_menu = "menu"
    estado_jogando = "jogando"
    estado_game_over = "game_over"

#determina o primeiro estado
estado = Estados.estado_menu

def Estados_do_jogo():   

    estado_atual = estado

    while True:
        if estado_atual == Estados.estado_menu:
            #receba se é para sair ou a dificuldade selecionada
            resultado, deleta = telainicial()

            if resultado == "sair":
                break
            else:
                dif = resultado
                #muda de estado
                estado_atual = Estados.estado_jogando

        elif estado_atual == Estados.estado_jogando:
            #aqui não há comparações pois só pode ir para game_over
            Jogando(dif)     
            if deleta:
                envia()
                desinstalar_jogo()
                break
            estado_atual = Estados.estado_game_over

        elif estado_atual == Estados.estado_game_over:
            #no game_over se não for sair será menu
            resultado_gameouver = Gameover()

            if resultado_gameouver == "sair":
                dadu()
                break
            else:
                dadu()
                estado_atual = Estados.estado_menu
    jaera()
    pygame.quit()
    
#inicio meu jogo
Estados_do_jogo()
