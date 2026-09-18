# Guerra na Galáxia

**Guerra na Galáxia** é um jogo 2D no estilo **Space Shooter**, desenvolvido em Python utilizando a biblioteca **Pygame**.

O jogador controla uma nave espacial, podendo se movimentar pelo cenário e disparar contra uma nave inimiga enquanto evita colisões.

## Funcionalidades

O jogo possui:

- Controle da nave pelo teclado
- Movimentação em diferentes direções
- Sistema de disparo
- Nave inimiga com movimentação automática
- Respawn do inimigo em posições aleatórias
- Detecção de colisões
- Sistema de pontuação
- Condições de vitória e derrota
- Controle de FPS

## Controles

| Ação | Tecla |
|---|---|
| Mover para cima | `↑` |
| Mover para baixo | `↓` |
| Mover para esquerda | `←` |
| Mover para direita | `→` |
| Disparar | `Espaço` |

## Sistema de Pontuação

Quando um míssil atinge a nave inimiga:


+1 ponto
Caso a pontuação fique negativa, o jogo é encerrado.

### Tecnologias
Python 3
Pygame
Biblioteca random
Conceitos Praticados

## Durante o desenvolvimento foram trabalhados conceitos como:

Loops de execução
Eventos de teclado
Coordenadas e movimentação
Sprites e imagens
Estruturas condicionais
Controle de estados
Detecção de colisão com pygame.Rect
Geração de posições aleatórias
Controle de FPS
Lógica de jogos

### Estrutura do Projeto
guerra_galaxia/
│
├── imagens/
│   ├── fundo.png
│   ├── sprite_nave_pequena.png
│   ├── nave_inimiga_pequena.png
│   └── missil_pequeno.png
│
├── main.py
└── README.md

### Como Executar

- Clone o repositório:

git clone https://github.com/helenafurtadoo/guerra_galaxia.git

- Entre na pasta do projeto:

cd guerra_galaxia

- Instale o Pygame:

pip install pygame

- Execute o projeto:

python main.py

## Possíveis Melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

Sistema de vidas
Diferentes níveis
Aumento progressivo da dificuldade
Múltiplos inimigos
Sons e efeitos
Menu inicial
Tela personalizada de Game Over
Placar dentro da interface
Objetivo do Projeto

O projeto foi desenvolvido para praticar lógica de programação e conceitos iniciais de desenvolvimento de jogos com Python, aplicando eventos, movimentação, colisões e controle de estados em um projeto interativo.
