import pygame #biblioteca python

#classe do botão
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		#com a altura e largura da imagem, podemos delimitar o campo clicável correspondente ao botão
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#pegar a posição do mouse
		pos = pygame.mouse.get_pos()

		#checar o "mouseover" e condições clicadas
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #se foi clicado
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0: #se nao foi clicado
			self.clicked = False

		#'desenhar' o botão na tela
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#imagens dos botões de menu
play_img = pygame.image.load("Botões/botao play.png")
resume_img = pygame.image.load("Botões/botao resume.png")
quit_img = pygame.image.load("Botões/botao quit.png")
principal_img = pygame.image.load("Botões/botao principal.png")
#preenchendo os parâmetros dos botões de menu
play_button = Button(304, 385, play_img, 1) #posição x e y; imagem; escala
resume_button = Button(304, 125, resume_img, 1) #posição x e y; imagem; escala
principal_button = Button(290,245, principal_img, 1) #posição x e y; imagem; escala
quit_button = Button(304, 375, quit_img, 1) #posição x e y; imagem; escala

#imagens dos botões das roupas
quadblusa_img = pygame.image.load("Botões/quadblusa.png")
quadcalca_img = pygame.image.load("Botões/quadcalca.png")
quadtenis_img = pygame.image.load("Botões/quadtenis.png")
#parâmetros dos botões das roupas
quadblusa = Button(100, 30, quadblusa_img, 1)
quadcalca = Button(100, 215, quadcalca_img, 1 )
quadtenis = Button(100, 400,quadtenis_img, 1)

#imagens dos outros botões:
pronto_img = pygame.image.load("Botões/botao pronto.png")
print_img = pygame.image.load("Botões/botao print.png")
#parâmetros dos outros botões:
pronto_button = Button(600, 500, pronto_img, 1)

print_button = Button(600, 500, print_img, 1)