import lixo_class as LI
from os import getcwd, name
from random import choice, randint
from pygame.image import load
from time import sleep

path_atual = getcwd()
if name == 'nt':
    path_imagens_outras = path_atual+'\\imagens\\Outras\\'
else:
    path_imagens_outras = path_atual+'/imagens/Outras/'

tipos = ('Metal', 'Organico', 'Papel', 'Plastico', 'Vidro')
imagem_vilao = load(path_imagens_outras+'vilao.png')

class Vilao(object):
    def __init__(self, fase, boss=False):
        self.pos = [0, -80]
        self.fase = fase
        self.imagem = imagem_vilao
        self.aparecendo = False
        self.boss = boss

    def aparecer_topo(self, screen, lixo):
        if self.pos[1] != 0:
            self.pos[1] += 2
            screen.blit(self.imagem, tuple(self.pos))
        else:
            sleep(0.2)
            self.lancar_lixo(screen, lixo)

    def sumir_topo(self, screen):
        if self.pos[1] != -80:
            self.pos[1] -= 2
            screen.blit(self.imagem, tuple(self.pos))
        else:
            self.aparecendo = False

    def lancar_lixo(self, screen, lixo):
        if self.fase == 6:
            angulo = choice([0, 90, 180, 270])
            lixo.queda_lixo(self.pos[0]+2, angulo)
        else:
            lixo.queda_lixo(self.pos[0]+2)
        lixo.desenhar_lixo(screen)

