import pygame
import random
pygame.init()

icone = pygame.image.load('assets/IconeHamburguer.png')
pygame.display.set_caption('Desvie do Hamburguer')
pygame.display.set_icon(icone)

#[inicio] Tela
largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()

fundo = pygame.image.load('assets/fundo.jpg')

#[Inicio] Cores
Preto = (0, 0, 0)
Branco = (255, 255, 255)

#[Inicio] colocando os personagens
cria = pygame.image.load('assets/criança.png')
hamburguer = pygame.image.load('assets/hamburgao.png')

def jogo():
    #[Inicio] Hamburguer
    hamburguer = pygame.image.load('assets/hamburgao.png')
    hamPosicaoX = largura * 0.45
    hamPosicaoY = altura -10
    hamLargura = 40
    hamAltura = 40
    #[Inicio] Posição da criança
    criaPosciaoX = largura * 0.45
    criaPosicaoY = altura * 0.8

    #[Inicio] Movimentos
    movimentoX = 0

    hamVelocidade = 5

    while True:
        #[Inicio] Verificação de inteiração
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    movimentoX = -10
                elif evento.key == pygame.K_d:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0
        #[Fim] Verificação de interação

        display.fill(Branco)
        display.blit(fundo, (0, -20))

        #[Inicio] Movimentos da criança
        criaPosciaoX = criaPosciaoX + movimentoX
        if criaPosciaoX < 0:
            criaPosciaoX = 0
        elif criaPosciaoX > 745:
            criaPosciaoX = 745
        display.blit(cria, (criaPosciaoX, criaPosicaoY))

        #[Inicio] Hamburguer movimentação
        display.blit(hamburguer, (hamPosicaoX, hamPosicaoY))
        hamPosicaoY = hamPosicaoY + hamVelocidade
        if hamPosicaoY > altura:
            hamPosicaoY = -10
            hamVelocidade = hamVelocidade +1
            hamPosicaoX = random.randrange(0, largura - 40)

        pygame.display.update()
        fps.tick(60)

jogo()