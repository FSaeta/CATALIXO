from random import randint, choice
from jogo import lixeiras_imagens_tipos
import pygame
tipos_imagens = lixeiras_imagens_tipos

def iniciar_lixeiras(lixeiras_dict):
    seq_nums = list(range(1, 6))
    for tipo, lx in lixeiras_dict.items():
        seq = choice(seq_nums)
        seq_nums.remove(seq)
        lixeira = Lixeira(tipo, seq)
        lixeiras_dict[tipo] = lixeira
    return lixeiras_dict
def mudar_sequencias(lixeiras_dict):
    seq_nums = list(range(1, 6))
    for tipo in lixeiras_dict.keys():
        seq = choice(seq_nums)
        seq_nums.remove(seq)
        lixeiras_dict[tipo].seq = seq
        lixeiras_dict[tipo].pos = lixeiras_dict[tipo].definir_pos()
        lixeiras_dict[tipo].rect = lixeiras_dict[tipo].criar_rect()

class Lixeira:
    def __init__(self, tipo, sequencia=0):
        self.seq = sequencia
        self.tipo = tipo
        self.imagem = tipos_imagens[self.tipo]
        self.pos = self.definir_pos()
        self.rect = self.criar_rect()

    def criar_rect(self):
        rect = pygame.Rect(self.pos[0]+40, self.pos[1], self.imagem.get_width()-80, self.imagem.get_height())
        return rect

    def desenhar_lixeira(self, tela):
        x, y = tela.get_size()
        quinto = x/5
        r = 12
        if self.seq == 1:
            pos = (0*quinto + r, y-140)
        elif self.seq == 2:
            pos = (1*quinto + r, y - 140)
        elif self.seq == 3:
            pos = (2*quinto + r, y - 140)
        elif self.seq == 4:
            pos = (3*quinto + r, y - 140)
        elif self.seq == 5:
            pos = (4*quinto + r, y - 140)
        else:
            pos = self.pos
        tela.blit(self.imagem, pos)
        return pos

    def definir_pos(self):
        x, y = 800, 680
        quinto = x/5
        r = 12
        if self.seq == 1:
            pos = (0*quinto + r, y-140)
        elif self.seq == 2:
            pos = (1*quinto + r, y - 140)
        elif self.seq == 3:
            pos = (2*quinto + r, y - 140)
        elif self.seq == 4:
            pos = (3*quinto + r, y - 140)
        elif self.seq == 5:
            pos = (4*quinto + r, y - 140)
        return pos
