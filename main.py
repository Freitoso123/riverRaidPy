import pygame
from classes.tela_inicial import telainicial, Gameover
from classes.jogando import *

class Estados:
    estado_menu = "menu"
    estado_jogando = "jogando"
    estado_game_over = "game_over"

estado = Estados.estado_menu

def Estados_do_jogo():    
    estado_atual = estado

    while True:
        if estado_atual == Estados.estado_menu:
            resultado = telainicial()

            if resultado == "sair":
                break
            else:
                dif = resultado
                estado_atual = Estados.estado_jogando

        elif estado_atual == Estados.estado_jogando:
            Jogando(dif)

            estado_atual = Estados.estado_game_over

        elif estado_atual == Estados.estado_game_over:
            resultado_gameouver = Gameover()

            if resultado_gameouver == "sair":
                break
            else:
                estado_atual = Estados.estado_menu
    pygame.quit()

Estados_do_jogo()