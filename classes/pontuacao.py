import pygame
from classes.tela_inicial import gameDisplay, largurat

def pontuacao(pontos):
    pontos_texto = str(pontos)
    fonte_tamanho = pygame.font.Font("fonte/Pontos.ttf", 50)
    textoSuperficie = fonte_tamanho.render(pontos_texto, True, "gold")
    textoRect = textoSuperficie.get_rect()
    textoRect.center = ((largurat//2), 570)
    gameDisplay.blit(textoSuperficie, textoRect)