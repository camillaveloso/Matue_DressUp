import pygame #biblioteca python
import button #arquivo contendo as classes, imagens e demais valores dos botões
import imagens #arquivo contendo as classes, imagens e demais valores das roupas
import saveload #arquivo contendo as funções de salvamento e carregamento
import capture #arquivo contendo função de captura de tela 

pygame.init() #iniciando o pygame
pygame.mixer.init()
#criar janela do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #tamanho da janela
pygame.display.set_caption("Matuê Dress Up") #legenda do jogo
BG = pygame.image.load("Mídias/menu principal.png") #background

#flags
game_paused = False #se o jogo tá pausado

#variável menu
menu_state = "principal" #estados do menu: principal; pausado; jogo em andamento; foto final. default = principal

#lista de sprites a serem mostrados
lista_blusa = [imagens.blusavazia, imagens.blusa1, imagens.blusa2, imagens.blusa3, imagens.blusa4, imagens.blusa5, imagens.blusa6]
lista_calca = [imagens.calcavazia, imagens.calca1, imagens.calca2, imagens.calca3, imagens.calca4]
lista_tenis = [imagens.tenisvazio, imagens.tenis1, imagens.tenis2, imagens.tenis3, imagens.tenis4, imagens.tenis5]

#posição dos sprites na lista a serem mostrados, um por vez.
indice_blusa = 0
indice_calca = 0
indice_tenis = 0

indice_blusa, indice_calca, indice_tenis = saveload.carregar_progresso() #carrega quais sprites foram usados ao fechamento do jogo

musica_fundo = "Mídias/Conexões de Máfia.mp3" #arquivo da nossa música de fundo
pygame.mixer.music.load(musica_fundo) #carrega a música, para ser executada

#loop do jogo
run = True #flag que sinaliza a execução do programa
while run:
  tela.blit(BG,(0,0)) #carrega a imagem do background e centraliza-a
  
  #menu principal:
  if menu_state == "principal": #se o menu está no valor 'principal':
    BG = pygame.image.load("Mídias/menu principal.png") #o background assume a imagem do menu principal
    
    if button.play_button.draw(tela): #se o botão 'play' é clicado, o menu assume o valor "vestindo", que é o jogo em si
      menu_state = "vestindo"
      pygame.mixer.music.play(loops = -1) #tocando música de fundo e o loop. o valor "-1" significa que irá tocar indefinidas vezes 
  
  #jogando:
  if menu_state == "vestindo": #se o menu está no valor "vestindo": 
    BG = pygame.image.load("Mídias/armario.png") #o background assume a imagem do 'armário'
    imagens.tue.draw(tela) #desenha o personagem principal na tela
    imagens.matue.rect.x = 380
    imagens.matue.rect.y = 100
    while button.quadblusa.draw(tela): #quando o botão das blusas é clicado:
      indice_blusa = (indice_blusa + 1) % len(lista_blusa) #a lista de sprites é percorrida, utilizando o operador '%' para auxiliar a "reiniciar" a lista
      
    while button.quadcalca.draw(tela): #quando o botão das calças é clicado:
      indice_calca = (indice_calca + 1) % len(lista_calca) #a lista de sprites é percorrida, utilizando o operador '%' para auxiliar a "reiniciar" a lista
    
    while button.quadtenis.draw(tela): #quando o botão dos tênis é clicado:
      indice_tenis = (indice_tenis + 1) % len(lista_tenis) #a lista de sprites é percorrida, utilizando o operador '%' para auxiliar a "reiniciar" a lista
    
    lista_tenis[indice_tenis].rect.x =380 #posição da roupa, no menu "vestindo"
    lista_tenis[indice_tenis].rect.y =100
    lista_calca[indice_calca].rect.x =380
    lista_calca[indice_calca].rect.y =100
    lista_blusa[indice_blusa].rect.x =380
    lista_blusa[indice_blusa].rect.y =100
    
    lista_tenis[indice_tenis].draw(tela) #"desenhando" o sprite do tipo 'tênis' na tela
    lista_calca[indice_calca].draw(tela) #"desenhando" o sprite do tipo 'calça' na tela
    lista_blusa[indice_blusa].draw(tela) #"desenhando" o sprite do tipo 'blusa' na tela
    
    if button.pronto_button.draw(tela): #se o botão "pronto" for clicado, iremos ao menu "pronto"
      menu_state = "pronto"

#pronto, escolhi minha roupa:
  if menu_state == "pronto":
    BG = pygame.image.load("Mídias/foto com o matue.png")
    imagens.matue.rect.x =310 #nova posição do personagem, diferente de quando estamos no menu "vestindo"
    imagens.matue.rect.y =90
    imagens.tue.draw(tela)
    
    lista_tenis[indice_tenis].rect.x =310 #nova posição da roupa, diferente de quando estamos no menu "vestindo"
    lista_tenis[indice_tenis].rect.y =90
    lista_calca[indice_calca].rect.x =310
    lista_calca[indice_calca].rect.y =90
    lista_blusa[indice_blusa].rect.x =310
    lista_blusa[indice_blusa].rect.y =90
    
    lista_tenis[indice_tenis].draw(tela) 
    lista_calca[indice_calca].draw(tela) 
    lista_blusa[indice_blusa].draw(tela)
  
  #eventos
  for event in pygame.event.get():   
    if event.type == pygame.KEYDOWN: #apertou uma tecla, qual? vamos checar:
      if menu_state == "vestindo":
        if event.key == pygame.K_SPACE: #se apertou "espaço":
          game_paused = True #flag torna-se verdadeira, apontando que o menu assumiu o valor "pause"
          menu_state = "paused"
    if event.type == pygame.MOUSEBUTTONDOWN: #opa, cliquei na tela, onde foi?
      if menu_state == "pronto" and button.print_button.rect.collidepoint(event.pos):  #Verifica se o botão de impressão foi clicado
        #Executa a captura de tela, por fim oculta o botão de impressão durante a captura de tela
        capture.capture_screen(tela, SCREEN_WIDTH, SCREEN_HEIGHT, [button.print_button])

    if event.type == pygame.QUIT: #se o "Xzinho" da janela é clicado, 'run' se torna FALSO e encerra o programa.
      run = False
  
  if menu_state == "pronto": #quando o menu estiver "pronto":
    button.print_button.draw(tela) #aparecer o botão "print" na tela, para salvarmos a imagem do nosso personagem
  
  #quando o menu é pausado:
  if game_paused == True:
    menu_state = "pause"
    #verifica qual o estado do menu
    if menu_state == "pause":
      pygame.mixer.music.pause() #com o menu pausado, a música pausa também
      #draw botões da tela pause + o que acontece se clicá-los
      if button.resume_button.draw(tela): #se o botão 'resume' é clicado: a flag de jogo pausado se torna FALSA, e o menu assume o valor 'vestindo'
        game_paused = False
        menu_state = "vestindo"
        pygame.mixer.music.unpause() #com o jogo "despausado", a música é despausada também
      if button.principal_button.draw(tela): #se o botão 'principal' é clicado: a flag de jogo pausado se torna FALSA, e o menu assume o valor 'principal'
        game_paused = False
        menu_state = "principal"
        pygame.mixer.music.stop() #a música é parada, caso o 'play' seja apertado, a música é reiniciada. 
      if button.quit_button.draw(tela): #se o botão 'quit' é clicado: run se torna FALSO, encerra o programa. 
        run = False  
    
  pygame.display.update() #atualiza a janela em tempo real
saveload.salvar_progresso(indice_blusa, indice_calca, indice_tenis) #armazena quais sprites de roupa estão sendo usados ao fechamento do jogo
pygame.quit() #encerrando o pygame
