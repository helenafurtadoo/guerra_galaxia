import pygame
from pygame import mixer
from time import sleep
from random import randint
from random import Random


x, y = (940, 540)
# criando a janela de exibicao do jogo
janela = pygame.display.set_mode([x, y])

# criando um nome para a janela
pygame.display.set_caption("Guerra na galáxia")

imagem_fundo = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/img_galaxia.jpg")

nave_jogador = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/sprite_nave_pequena.png")

nave_inimiga = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/nave_inimiga_pequena.png")

tiro = pygame.image.load("C:/Users/helen/OneDrive/Desktop/jogo python/imagens/missil_pequeno.png")




# posicao nave do jogador
pos_x_jogador = 420
pos_y_jogador = 400
vel_nave_jogador = 10  # velocidade de movimeto da nave, qnd apertar algm tecla

# posicao nave inimiga
pos_x_inimigo = 430
pos_y_inimigo = 50
vel_nave_inimgo = 15

# posicao missil
pos_x_missil = 430
pos_y_missil = 450
vel_missil = 10


pontuacao = 0

tiro_alvo = False


rodando = True


# definindo funcoes
def colisoes():
    global pontuacao
    global pos_y_inimigo
    global pos_x_inimigo

    # se o jogador principal colidir com a nave_inimiga
    if jogador_rect.colliderect(inimigo_rect) or inimigo_rect.y > 500:
        pontuacao -= 1
        print(pontuacao)
        return True
    elif tiro_rect.colliderect(inimigo_rect):
        pontuacao += 1
        pos_y_inimigo -= 1200
        if pos_y_inimigo < -1000:
            random_y = randint(1,440)
            random_x = randint(1, 870)
            pos_y_inimigo -= 450
            pos_y_inimigo = random_y
            pos_x_inimigo = random_x
        print(pontuacao)
        return True

    else:
        return False

while rodando:

    for events in pygame.event.get():
        # adicionar o botao para fechar a janela de exibicao
        if events.type == pygame.QUIT:
            rodando = False

        teclas = pygame.key.get_pressed()


        # criando barreiras para a nave
        if pos_y_jogador <= -10:
            pos_y_jogador = -10
        if pos_y_jogador >= 440:
            pos_y_jogador = 440
        if pos_x_jogador <= 0:
            pos_x_jogador = 0
        if pos_x_jogador >= 850:
            pos_x_jogador = 850

        # mostrando imagens na janela
        janela.blit(imagem_fundo, (0, 0))
        janela.blit(nave_jogador, (pos_x_jogador, pos_y_jogador))
        janela.blit(nave_inimiga, (pos_x_inimigo, pos_y_inimigo))        
        tiro = pygame.transform.scale(tiro, (30,30)) # transforma o tamanho da imagem (missil)



        # MOVIMENTAÇÃO DO INIMIGO
        pos_y_inimigo += 10
    
        # RESPAWN DA NAVE INIMIGA (quando morrer)
        if pos_y_inimigo > 540:
            # sorteando valores para a nave nascer
            random_y = randint(1, 440)
            random_x = randint(1, 870)
            pos_y_inimigo -= 450 # se a nave passar do final da tela
            pos_y_inimigo = random_y
            pos_x_inimigo = random_x

        # obtem todos os comandos pressionados no teclado
        comandos = pygame.key.get_pressed()

        # verifia qual o comando precionado, e retorna uma acao
        # MOVIMENTAÇÃO JOGADOR
        # direção: CIMA
        if comandos[pygame.K_w]:
            pos_y_jogador -= vel_nave_jogador
        # direção: BAIXO
        if comandos[pygame.K_s]:
            pos_y_jogador += vel_nave_jogador
        # direção: ESQUERDA
        if comandos[pygame.K_a]:
            pos_x_jogador -= vel_nave_jogador
        # direção: DIREITA
        if comandos[pygame.K_d]:
            pos_x_jogador += vel_nave_jogador
        # ATIRAR MISSIL
        if comandos[pygame.K_SPACE]:
            tiro_alvo = True
            if tiro_alvo:
                vel_missil = 10
                pos_y_missil -= vel_missil
        # RESPAWN DO MISSIL DE VOLTA A NAVE PRONTO PARA SER ATIRADO NOVAMENTE
        if pos_y_missil < 1:
            tiro_alvo = True
            pos_y_missil = pos_y_jogador
            pos_x_missil = pos_x_jogador
            vel_missil = 10

    

        # reconhecendo objetos
        jogador_rect = nave_jogador.get_rect()
        inimigo_rect = nave_inimiga.get_rect()
        tiro_rect = tiro.get_rect()

                    
        jogador_rect.y = pos_y_jogador
        jogador_rect.x = pos_x_jogador

        inimigo_rect.y = pos_y_inimigo
        inimigo_rect.x = pos_x_inimigo

        tiro_rect.y = pos_y_missil
        tiro_rect.x = pos_x_missil

        #colisoes()


        pygame.draw.rect(janela, (255, 0, 0), jogador_rect, 4)
        pygame.draw.rect(janela, (255, 0, 0), inimigo_rect, 4)
        pygame.draw.rect(janela, (255, 0, 0), tiro_rect, 4)

        # verificando se o tiro_alvo é verdadeiro
        if tiro_alvo:
            pos_y_missil = vel_missil
          
        # atualiza a janela de exibiçao(para tudo q esteja dentro do loop, seja aparecido(atualizado) na tela)
        pygame.display.update()
