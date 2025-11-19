import random, time
from classes.caem import Caem

class Gasolina(Caem): 
    def __init__(self, dims, pos, velY):
        sprite_gasolina = "sprites/combustivel.png" 
        super().__init__(sprite_gasolina, dims, pos, velY)        

        self.combustivel = 100

        self.inicio_abastecer = None
        self.tempo_abastecer = 0.25

    def gera_gasolina(mapa):

        lista_gasolina = []  
        quantidade_gasolina = 0
        
        while quantidade_gasolina < 3:  
            x = random.randint(0, 800)  
            y = random.randint(-32, -800)
            
            teste_gasolina = Gasolina((31, 64), (x, y), 3)
            
            if not teste_gasolina.colisaoMask(mapa):
                lista_gasolina.append(teste_gasolina)
                quantidade_gasolina += 1
        return lista_gasolina
    
    def atualiza_abastecer(self, player):
        if player.colisaoMark(self):
            if self.inicio_abastecer is None:
                self.inicio_abastecer = time.time()
            
            while (time.time() - self.inicio_abastecer) >= self.tempo_abastecer:
                self.combustivel += 5
        