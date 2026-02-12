🚀 Guerra na Galáxia

Um jogo 2D estilo Space Shooter desenvolvido em Python utilizando a biblioteca Pygame.
O jogador controla uma nave espacial que deve destruir naves inimigas e evitar colisões.

🎮 Demonstração

O jogo possui:

Nave controlada pelo jogador

Nave inimiga com respawn aleatório

Sistema de disparo de mísseis

Sistema de colisão

Controle de pontuação

Condição de vitória e derrota

🛠️ Tecnologias Utilizadas

Python 3

Pygame

Random (biblioteca padrão do Python)

📂 Estrutura do Projeto
📁 projeto
 ├── main.py
 ├── 📁 imagens
 │     ├── fundo.png
 │     ├── sprite_nave_pequena.png
 │     ├── nave_inimiga_pequena.png
 │     └── missil_pequeno.png

⚙️ Funcionalidades
🎯 Movimentação do Jogador

↑ Seta para cima

↓ Seta para baixo

← Seta para esquerda

→ Seta para direita

💥 Sistema de Tiro

Barra de espaço para disparar

Apenas um tiro por vez na tela

O míssil retorna automaticamente quando sai da tela

👾 Inimigo

Movimento vertical automático

Respawn em posição aleatória

Velocidade controlada por contador interno

🔥 Sistema de Colisão

Colisão entre tiro e inimigo → +1 ponto

Colisão entre jogador e inimigo → -1 ponto

Caso a pontuação fique negativa → Game Over

🧠 Lógica do Jogo

O projeto utiliza:

pygame.Rect() para detecção de colisão

Loop principal com controle de FPS (60 FPS)

Controle de estados com variáveis booleanas

Sistema simples de pontuação

A função colisoes() é responsável por verificar:

Colisão do tiro com inimigo

Colisão do jogador com inimigo

Atualização da pontuação

▶️ Como Executar

Instale o Python (3.10+ recomendado)

Instale o Pygame:

pip install pygame


Execute o arquivo:

python main.py

📈 Melhorias Futuras

Sistema de vidas

Sons e efeitos especiais

Menu inicial

Tela de Game Over personalizada

Sistema de níveis e aumento progressivo de dificuldade

Placar visual na tela

Múltiplos inimigos

🎓 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

Praticar lógica de programação

Trabalhar com eventos e controle de teclado

Implementar sistema de colisão

Aprender desenvolvimento de jogos com Pygame
