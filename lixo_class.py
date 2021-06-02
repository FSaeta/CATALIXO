from random import randint, choice
import pygame
import os

path_atual = os.getcwd()
if os.name == 'nt':
    path_marcadores = path_atual + '\\imagens\\Outras\\Marcadores\\'
else:
    path_marcadores = path_atual + '/imagens/Outras/Marcadores/'

tipos = ('Metal', 'Organico', 'Papel', 'Plastico', 'Vidro')
marcador = {}
def add_imagens_marcador():
    os.chdir(path_marcadores)
    cont = 0
    for img in os.listdir():
        imagem = pygame.image.load(img)
        marcador.update({tipos[cont]: imagem})
        cont += 1
    os.chdir(path_atual)
add_imagens_marcador()

class Lixo(object):
    def __init__(self, tipo, imagem, fase, caindo=False):
        self.pos_x = 0
        self.pos_y = 0
        self.tipo = tipo
        self.fase = fase
        self.angulo = choice((0, 90, 180, 270)) if fase == 6 else 0
        self.imagem = imagem
        self.caindo = caindo
        self.velocidade = self._def_velocidade()
        self.rect = self.criar_rect()

    def __str__(self):
        msg = f"Tipo: {self.tipo}\nPosição x: {self.pos_x}\nPosição y: {self.pos_y}\n"
        return msg

    def criar_rect(self):
        r = pygame.Rect(self.get_pos(), self.imagem.get_size())
        return r

    def _def_velocidade(self):
        if self.fase == 1:
            vel = 1.2
        elif self.fase == 2:
            vel = 1.35
        elif self.fase == 3:
            vel = 1.6
        elif self.fase == 4:
            vel = 1.70
        elif self.fase == 5:
            vel = 1.95
        elif self.fase == 6:
            vel = 2.1
        else:
            vel = 0
        return vel

    def girar_lixo(self, lado):
        if lado == 'd':
            self.angulo += 90
            if self.angulo == 360:
                self.angulo = 0
            self.imagem = pygame.transform.rotate(self.imagem, 90)
        elif lado == 'e':
            self.angulo -= 90
            if self.angulo == -360:
                self.angulo = 0
            self.imagem = pygame.transform.rotate(self.imagem, -90)

        else:
            raise ValueError

    def mover_lixo(self, direcao):
        if direcao == 'd':
            if self.pos_x <= 800-76:
                self.pos_x += 5.5
        elif direcao == 'e':
            if self.pos_x >= 0:
                self.pos_x -= 5.5
        self.rect.move_ip(self.pos_x, self.pos_y)

    def queda_lixo(self, posx, angulo=0):
        global marcador
        self.caindo = True
        self.pos_x = posx
        self.angulo = angulo
        if self.fase == 6:
            self.imagem.blit(marcador[self.tipo], (0, 0))
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)

    def desenhar_lixo(self, screen):
        if self.caindo:
            screen.blit(self.imagem, self.get_pos())

    def get_pos(self):
        pos = (self.pos_x, self.pos_y)
        return pos
