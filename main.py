import pygame
from pygame import mixer
from time import sleep
from random import randint
from random import Random

pygame.init()

x, y = (940, 540)
# criando a janela de exibicao do jogo
janela = pygame.display.set_mode([x, y])

# criando um nome para a janela
pygame.display.set_caption("Guerra na galáxia")

clock = pygame.time.Clock()

imagem_fundo = pygame.image.load("imagens/fundo.png")

nave_jogador = pygame.image.load("imagens/sprite_nave_pequena.png")

nave_inimiga = pygame.image.load("imagens/nave_inimiga_pequena.png")

tiro = pygame.image.load("imagens/missil_pequeno.png")


tiro = pygame.transform.scale(tiro, (30,30)) # transforma o tamanho da imagem (missil)



# posicao nave do jogador
pos_x_jogador = 420
pos_y_jogador = 400
vel_nave_jogador = 10  # velocidade de movimeto da nave, qnd apertar algm tecla

# posicao nave inimiga
pos_x_inimigo = 430
pos_y_inimigo = 50
vel_nave_inimigo = 15

# posicao missil
pos_x_missil = 430
pos_y_missil = 450
vel_missil = 10

# CONTROLE DE tiro
tiro_disparado = False

pontuacao = 0

contador_inimigo = 0

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
            random_y = randint(50,258)
            random_x = randint(1, 870)
            pos_y_inimigo = random_y
            pos_x_inimigo = random_x
        print(pontuacao)
        return True

    else:
        return False

def resultado():
    global pontuacao

    if pontuacao < 0:
        print("Você perdeu o jogo! GAME OVER")
    else:
        print("Você ganhou o jogo! PARABÉNS")

rodando = True

while rodando:
    # EVENTOS
    for events in pygame.event.get():
        # adicionar o botao para fechar a janela de exibicao
        if events.type == pygame.QUIT:
            rodando = False

    # ==== MOVIMENTAÇÃO DO INIMIGO ====
    contador_inimigo += 1
    if contador_inimigo > 8 :
        pos_y_inimigo += 5
        contador_inimigo = 0

    # RESPAWN DA NAVE INIMIGA (quando morrer)
    if pos_y_inimigo > 540 or pos_y_inimigo < -100:
        # sorteando valores para a nave nascer
        random_y = randint(50, 250)
        random_x = randint(1, 870)
        pos_y_inimigo = random_y
        pos_x_inimigo = random_x
 

    # ==== MOVIMENTACAO DO JOGADOR ====
    comandos = pygame.key.get_pressed()
    # direção: CIMA
    if comandos[pygame.K_UP]:
        pos_y_jogador -= vel_nave_jogador
    # direção: BAIXO
    if comandos[pygame.K_DOWN]:
        pos_y_jogador += vel_nave_jogador
    # direção: ESQUERDA
    if comandos[pygame.K_LEFT]:
        pos_x_jogador -= vel_nave_jogador
    # direção: DIREITA
    if comandos[pygame.K_RIGHT]:
        pos_x_jogador += vel_nave_jogador
    
    # === BARREIRAS DA NAVE ====
    if pos_y_jogador <= -10:
        pos_y_jogador = -10
    if pos_y_jogador >= 440:
        pos_y_jogador = 440
    if pos_x_jogador <= 0:
        pos_x_jogador = 0
    if pos_x_jogador >= 850:
        pos_x_jogador = 850

    # ===== SISTEMA DE TIRO =====
    # ATIRAR MISSIL - só dispara se nenhum tiro está na tela
    if comandos[pygame.K_SPACE] and not tiro_disparado:
        tiro_disparado = True
        pos_x_missil = pos_x_jogador
        pos_y_missil = pos_y_jogador

    # MOVIMENTO DO TIRO (contínuo enquanto disparado)
    if tiro_disparado:
        pos_y_missil -= vel_missil

    # RESPAWN DO MISSIL DE VOLTA A NAVE (quando sai da tela)
    if pos_y_missil < 0:
        tiro_disparado = False
        pos_y_missil = pos_y_jogador
        pos_x_missil = pos_x_jogador

    # ==== COLISÕES ====
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

    colisoes()

    # ==== DESENHAR TUDO NA TELA ====
    janela.blit(imagem_fundo, (0, 0))
    janela.blit(nave_jogador, (pos_x_jogador, pos_y_jogador))
    janela.blit(nave_inimiga, (pos_x_inimigo, pos_y_inimigo))    
    janela.blit(tiro, (pos_x_missil, pos_y_missil))    

    # ==== ATUALIZAR TELA ====
    pygame.display.update()
    clock.tick(60)


print("-=" * 20)
resultado()
print("-=" * 20)
