import pygame
import random
import time
pygame.init()

icone = pygame.image.load('assets/IconeHamburguer.png')
pygame.display.set_caption('Ta chovendo Hamburguer')
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

#[Inicio] Sons
comendo = pygame.mixer.Sound('assets/comendo.wav')
fritando = pygame.mixer.Sound('assets/fritando.wav')


def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, Preto)
    return textSurface, textSurface.get_rect()


def message_display(texto):
    fonte = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TestRect = text_objects(texto, fonte)
    TestRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TestRect)
    pygame.display.update()
    time.sleep(5)
    jogo()


def dead(desvios):
    pygame.mixer.Sound.play(comendo)
    pygame.mixer.music.stop()
    message_display('!!!Você Perdeu!!! com' +str(desvios)+ 'desvios')


def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None,25)
    texto = font.render('Desvios:' +str(desvios),True, Preto)
    display.blit(texto, (0,0))


def jogo():
    pygame.mixer.music.load('assets/musica.wav')
    pygame.mixer.music.play(-1)
    #[Inicio] Hamburguer
    hamburguer = pygame.image.load('assets/hamburgao.png')
    hamPosicaoX = largura * 0.45
    hamPosicaoY = -10
    hamLargura = 40
    hamAltura = 40
    #[Inicio] Posição da criança
    criaPosciaoX = largura * 0.45
    criaPosicaoY = altura * 0.8
    criaLargura = 55
    #[Inicio] Movimentos
    movimentoX = 0

    hamVelocidade = 5

    desvios = 0

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
            pygame.mixer.Sound.play(fritando)
            hamPosicaoY = -10
            hamVelocidade = hamVelocidade +0.5
            hamPosicaoX = random.randrange(0, largura - 40)
            desvios = desvios + 1


        escrevendoPlacar(desvios)


        #[Inicio] Colisão
        if criaPosicaoY < hamPosicaoY + hamAltura:
            if criaPosciaoX < hamPosicaoX and criaPosciaoX + criaLargura > hamPosicaoX  or hamPosicaoX + hamLargura > criaPosciaoX and hamPosicaoX + hamLargura < criaPosciaoX + criaLargura:
                dead(desvios)
        
        pygame.display.update()
        fps.tick(60)

jogo()