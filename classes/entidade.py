import pygame

class Entidade:
    gameDisplay = pygame.display.set_mode((800, 600))
    def __init__(self, sprite, dims, pos):
        # Carrega e redimensiona o sprite
        self.sprite = pygame.transform.scale(
            pygame.image.load(sprite).convert_alpha(),
            (dims[0], dims[1])
        )
         
        # Posição
        self.x = pos[0]
        self.y = pos[1]

        # Caixa de colisão
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def imprimir(self):
        # Atualiza posição e desenha o sprite na tela
        self.rect.topleft = (self.x, self.y)
        self.gameDisplay.blit(self.sprite, (self.x, self.y))

    def colisaoMask(self, outro):
        offset = (int(outro.x - self.x), int(outro.y - self.y))
        return self.mask.overlap(outro.mask, offset) is not None

    def colisaoRect(self, outro):
        return self.rect.colliderect(outro.rect)
