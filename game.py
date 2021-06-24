import pygame

pygame.init()

#[inicio] Tela
largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()

fundo = pygame.image.load('assets/fundo.jpg')

#[Inicio] Personagens
cria = pygame.image.load('assets/criança.png')
criaPosciaoX = largura * 0.45
criaPosicaoY = altura * 0.8

#[Inicio] Movimentos
movimentoX = 0
#[Inicio] Cores
Preto = (0, 0, 0)
Branco = (255, 255, 255)

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
    display.blit(fundo, (0, 0))

    #[Inicio] Movimentos da criança
    criaPosciaoX = criaPosciaoX + movimentoX
    if criaPosciaoX < 0:
        criaPosciaoX = 0
    elif criaPosciaoX > 745:
        criaPosciaoX = 745
    display.blit(cria, (criaPosciaoX, criaPosicaoY))

    pygame.display.update()
    fps.tick(60)