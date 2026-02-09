import pygame

pygame.init()

tela = pygame.display.set_mode((800, 400)) #criando a janela de exibicao do jogo 
 
pygame.display.set_caption('Guerra na galáxia) # criando um nome para a janela 

imagem_fundo = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/img_galaxia.jpg")

# problema 1 -> a janela de exibicao abre, mas fecha imediatamente. PARA RESOLVER: (criar um loop para rodar sempre o codigo)

loop = True
while loop: # mantem a janela do jogo aberta
    # desenhar todos os elementos
    # atualizar tudo
    for events in pygame.event.get():

          # 1°evento a tratar -> adicionar o botao para fechar a janela de exibicao
          if events.type == pygame.QUIT:
            loop = False





    pygame.display.update() # atualiza a janela de exibiçao(para tudo q esteja dentro do loop, seja aparecido(atualizado) na tela)








   

