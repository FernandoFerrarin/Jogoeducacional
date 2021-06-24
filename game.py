import pygame

pygame.init()

#[inicio] Tela
largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()

fundo = pygame.image.load('assets/fundo.jpg')

#[Inicio] Cores
Preto = (0, 0, 0)
Branco = (255, 255, 255)

while True:
    #[Inicio] Verificação de inteiração
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()




    display.fill(Branco)
    display.blit(fundo, (0, 0))

    pygame.display.update()

    fps.tick(60)