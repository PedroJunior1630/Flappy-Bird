import os
import pygame
import random


TELA_LARGURA = 500
TELA_ALTURA = 800

IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMG_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMG_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))

IMGS_PASSAROS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png'))),
]

pygame.font.init()

TEXTO_FONT = pygame.font.SysFont('Arial',40)

class Passaro():
    IMGS = IMGS_PASSAROS
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.x
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMG[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        #calcular deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        #restringir o deslocamento
        if deslocamento  > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        
        self.y += deslocamento

        #o angulo do passaro
        if deslocamento < 0 or self.y < (self.alura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo  > -98:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self,tela):
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4+1:
            self.imagem = self.IMGS[0]
            self.conatgem_imagem = 0
        
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem =  self.TEMPO_ANIMACAO * 2

        #desenhar a imagem
        imagem_rotacionado =  pygame.transform.rotate(self.imagem,selrf.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x,self.y)).center
        retangulo = imagem.rotacionando.get_rect(center=pos_centro_imagem)
        tela.blit(tempo_rotacionando,retangulo.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.imagem)
        

class Cano():
    pass
