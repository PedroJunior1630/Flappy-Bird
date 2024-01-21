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

