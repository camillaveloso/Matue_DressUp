import pygame #biblioteca python

class Roupa(pygame.sprite.Sprite):
    def __init__(self,imagem, x, y, layer):
        super().__init__()
        #parâmetros do sprite
        self.image = pygame.image.load(imagem) #imagem
        self.rect = self.image.get_rect() #tamanho
        self.rect.x = x #posição x
        self.rect.y = y #posição y
        self.layer = layer #camada
    
    def draw(self, screen): #função que "desenha" o sprite na tela
        screen.blit(self.image, self.rect)

#imagens dos sprites e seus parâmetros
matue = Roupa("Mídias/matue.png", 380, 100, 1)

blusa1 = Roupa("Blusa/blusa 1.png", 380, 100, 4)
blusa2 = Roupa("Blusa/blusa 2.png", 380, 100, 4)
blusa3 = Roupa("Blusa/blusa 3.png", 380, 100, 4)
blusa4 = Roupa("Blusa/blusa 4.png", 380, 100, 4)
blusa5 = Roupa("Blusa/blusa 5.png", 380, 100, 4)
blusa6 = Roupa("Blusa/blusa 6.png", 380, 100, 4)
blusavazia = Roupa("Mídias/sprite vazio.png", 380, 100, 4)

calca1 = Roupa("Calça/calca 1.png", 380, 100, 3)
calca2 = Roupa("Calça/calca 2.png", 380, 100, 3)
calca3 = Roupa("Calça/calca 3.png", 380, 100, 3)
calca4 = Roupa("Calça/calca 4.png", 380, 100, 3)
calcavazia = Roupa("Mídias/sprite vazio.png", 380, 100, 3)

tenis1 = Roupa("Tênis/nike.png", 380, 100, 2)
tenis2 = Roupa("Tênis/nike2.png", 380, 100, 2)
tenis3 = Roupa("Tênis/adidas.png", 380, 100, 2)
tenis4 = Roupa("Tênis/adidas2.png", 380, 100, 2)
tenis5 = Roupa("Tênis/adidas3.png", 380, 100, 2)
tenisvazio = Roupa("Mídias/sprite vazio.png", 380, 100, 2)

tue = pygame.sprite.Group() #adicionamos o sprite "matue" a um grupo, para podermos chamá-lo e desenhá-lo
tue.add(matue)




