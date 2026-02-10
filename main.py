import pygame

pygame.init()

janela = pygame.display.set_mode((940, 540)) #criando a janela de exibicao do jogo 
 
pygame.display.set_caption("Guerra na galáxia") # criando um nome para a janela 

imagem_fundo = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/img_galaxia.jpg")

nave_jogador = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/sprite_nave_pequena.png")

nave_inimiga = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/nave_inimiga_pequena.png")


# posicao nave do jogador
pos_x_jogador = 420
pos_y_jogador = 400
# velocidade de movimeto da nave, qnd apertar algm tecla
vel_nave_jogador = 2



# posicao nave inimiga
pos_x_inimigo = 420
pos_y_inimigo = 100
vel_nave_inimga = 2
# problema 1 -> a janela de exibicao abre, mas fecha imediatamente. PARA RESOLVER: (criar um loop para rodar sempre o codigo)

loop = True
while loop:

  for events in pygame.event.get():

    # adicionar o botao para fechar a janela de exibicao
    if events.type == pygame.QUIT:
      loop = False

  teclas = pygame.key.get_pressed()

  # MOVIMENTAÇÃO JOGADOR 
  # direção: CIMA
  if teclas[pygame.K_UP]:
    pos_y_jogador -= vel_nave_jogador
  # direção: BAIXO
  if teclas[pygame.K_DOWN]:
    pos_y_jogador += vel_nave_jogador
  # direção: ESQUERDA
  if teclas[pygame.K_LEFT]:
    pos_x_jogador -= vel_nave_jogador
  # direção: DIREITA
  if teclas[pygame.K_RIGHT]:
    pos_x_jogador += vel_nave_jogador






  # mostrando imagens na janela
  janela.blit(imagem_fundo, (0, 0)) 
  janela.blit(nave_jogador, (pos_x_jogador, pos_y_jogador))
  janela.blit(nave_inimiga, (pos_x_inimigo, pos_y_inimigo)) 





  pygame.display.update() # atualiza a janela de exibiçao(para tudo q esteja dentro do loop, seja aparecido(atualizado) na tela)








   

