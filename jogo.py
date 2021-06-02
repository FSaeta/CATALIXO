import pygame
import random
from lixo_class import Lixo
import lixeira_class as LA
from vilao_class import Vilao
from pygame.locals import *
from sys import exit
import os
import time
import pdb

# --------------------------------------------------------
# Paths
if os.name == 'nt':
    path_atual = os.getcwd()
    path_imagens_lixos = path_atual+'\\imagens\\Lixos\\'
    path_imagens_lixeiras = path_atual+'\\imagens\\Lixeiras\\'
    path_imagens_cenarios = path_atual+'\\imagens\\Cenarios\\'
    path_imagens_telas = path_atual+'\\imagens\\Telas\\'
    path_imagens_outras = path_atual+'\\imagens\\Outras\\'

else:
    path_atual = os.getcwd()
    path_imagens_lixos = path_atual + '/imagens/Lixos/'
    path_imagens_lixeiras = path_atual+'/imagens/Lixeiras/'
    path_imagens_cenarios = path_atual+'/imagens/Cenarios/'
    path_imagens_telas = path_atual+'/imagens/Telas/'
    path_imagens_outras = path_atual+'/imagens/Outras/'

# Funções
# ------------------------------------------------------
def adicionar_imagens_telas():
    os.chdir(path_imagens_telas)
    for tipo in os.listdir():
        os.chdir(tipo)
        lista, lista_aux = [], []
        imagens_diretorio = os.listdir()
        for n in imagens_diretorio:
            if os.path.isdir(n):
                if n == 'botoes':
                    os.chdir(n)
                    adicionar_imagens_botoes(tipo)
                    os.chdir('..')
                imagens_diretorio.remove(n)
        if tipo == 'Tela_principal':
            for n in range(0, len(imagens_diretorio)):
                img = imagens_diretorio[n]
                imagem = pygame.image.load(img)
                lista_aux.append(imagem)
                try:
                    prox_img = imagens_diretorio[n+1]
                except IndexError:
                    prox_img = str(n+1) + '_over'
                if img[0] != prox_img[0]:
                    tupla = [x for x in lista_aux]
                    tupla = tuple(tupla)
                    lista.append(tupla)
                    lista_aux.clear()
                else:
                    pass
        elif tipo == 'Tela_gameover' or tipo == 'Tela_pause':
            for img in imagens_diretorio:
                imagem = pygame.image.load(img)
                if tipo == 'Tela_pause':
                    imagem.convert_alpha()
                lista.append(imagem)
        elif tipo == 'Tela_instrucoes':
            for img in imagens_diretorio:
                imagem = pygame.image.load(img)
                lista.append(imagem)
        telas.update({tipo: lista})
        os.chdir(path_imagens_telas)
    os.chdir(path_atual)

def adicionar_imagens_botoes(chave):
    botoes_tipo = {}
    for botao in os.listdir():
        nome = botao.split('-')
        img = pygame.image.load(botao)
        if nome[0] not in botoes_tipo.keys():
            dado = {nome[0]: [img]}
            botoes_tipo.update(dado)
        else:
            botoes_tipo[nome[0]].append(img)
    botoes.update({chave: botoes_tipo})

def adicionar_imagens_cenarios():
    os.chdir(path_imagens_cenarios)
    for img in os.listdir():
        imagem = pygame.image.load(img)
        cenarios_imagens.append(imagem)
    os.chdir(path_atual)

def adicionar_imagens_lixos():
    os.chdir(path_imagens_lixos)
    for tipo, lista in lixos_imagens_tipos.items():
        os.chdir(tipo)
        for img in os.listdir():
            imagem = pygame.image.load(img)
            lista.append(imagem)
        os.chdir(path_imagens_lixos)
    os.chdir(path_atual)

def criar_imagens_lixeiras():
    for tipo in lixeiras_imagens_tipos.keys():
        lixeiras_imagens_tipos[tipo] = pygame.image.load(path_imagens_lixeiras+lixeiras_imagens_tipos[tipo])

def get_highscore():
    with open('high_score.txt') as arquivo:
        hs = arquivo.read()
        return hs

def set_highscore(score):
    with open('high_score.txt', 'w') as arquivo:
        arquivo.write(str(score))

def blit_btn(screen, tipo_tela, botao, pos_cursor, clic):
    # passar para botao ->   'nomebotao'
    x, y = pos_cursor
    if botao == 'botao_musica':
        global musica
        botao = botoes[tipo_tela][botao]
        if musica:
            if 686 <= x <= 766 and 18 <= y <= 98:
                btn = botao[1]
                if clic:
                    musica = False
                    pygame.mixer_music.stop()
            else:
                btn = botao[0]
        else:
            if 686 <= x <= 766 and 18 <= y <= 98:
                btn = botao[2]
                if clic:
                    musica = True
                    pygame.mixer_music.play(-1)
            else:
                btn = botao[3]
        screen.blit(btn, (30, 0))

def blit_tela_principal(screen, pos_cursor, clic=False):
    global tela_atual, musica
    tipo_tela = tela_atual
    x, y = pos_cursor
    tipo_tela = 'Tela_principal'
    # ---------
    if (212 <= x <= 557) and (271 <= y <= 331):
        if not clic:
            tela_ativa = telas[tipo_tela][1][0]
        else:
            tela_ativa = telas[tipo_tela][1][1]
            tela_atual = "Tela_jogo"
    elif (212 <= x <= 557) and (350 <= y <= 410):
        if not clic:
            tela_ativa = telas[tipo_tela][2][0]
        else:
            tela_ativa = telas[tipo_tela][2][1]
            tela_atual = "Tela_instrucoes"
    elif (212 <= x <= 557) and (439 <= y <= 499):
        if not clic:
            tela_ativa = telas[tipo_tela][3][0]
        else:
            tela_ativa = telas[tipo_tela][3][1]
    else:
        tela_ativa = telas[tipo_tela][0][0]
    screen.blit(tela_ativa, (0, 0))
    # Blit Botão Musica
    blit_btn(screen, tipo_tela, 'botao_musica', pos_cursor, clic)
    screen.blit(texto_high_score, (10, 10))
    screen.blit(lixos_principal, (0, 0))
    pygame.display.update()
    if clic:
        time.sleep(0.25)
    if tela_ativa == telas[tipo_tela][3][1]:
        pygame.quit()
        exit()

def blit_tela_instrucoes(screen, pos_cursor, clic=False):
    global tela_atual, pag
    x, y = pos_cursor
    btn_index = 0
    if (212 <= x <= 557) and (570 <= y <= 630):
        if not clic:
            btn_index = 1
        else:
            btn_index = 2
    elif (310 <= x <= 343) and (531 <= y <= 560) and clic:
        if pag != 1:
            pag -= 1
    elif (457 <= x <= 490) and (531 <= y <= 560) and clic:
        if pag != 3:
            pag += 1
    tela_ativa = telas['Tela_instrucoes'][pag-1]
    screen.blit(tela_ativa, (0, 0))
    btn_voltar = botoes[tela_atual]['botao_voltar'][btn_index]
    screen.blit(btn_voltar, (0, 0))
    pygame.display.update()
    if btn_index == 2:
        pag = 1
        tela_atual = 'Tela_principal'
        time.sleep(0.25)

def blit_tela_fase(screen, fase, sc=True):
    global texto_vidas, texto_score, texto_tipo
    cenario = cenarios_imagens[fase-1]
    screen.blit(cenario, (0, 0))
    if sc:
        screen.blit(texto_score, (10, 10))
        screen.blit(texto_vidas, (10, 50))
        screen.blit(texto_tipo, (800 - (texto_tipo.get_width() + 10), 10))
        screen.blit(texto_pause, (250, 10))


def blit_tela_gameover(screen, pos_cursor, clic, new_hs):
    global texto_score, vidas, tela_atual, texto_score_gameover
    x, y = pos_cursor
    index = 0
    if (308 <= x <= 382) and (571 <= y <= 597):
        index = 1
        if clic:
            tela_atual = "Tela_jogo"
    elif (434 <= x <= 482) and (571 <= y <= 597):
        index = 2
        if clic:
            tela_atual = "Tela_principal"
    screen.blit(telas['Tela_gameover'][index], (0, 0))
    blit_btn(tela, 'Tela_gameover', 'botao_musica', pos_cursor, clic)
    if new_hs:
        texto_highscore_gameover = fonte_highscore_gameover.render("NOVO HIGHSCORE", True, PRETO)
        screen.blit(texto_highscore_gameover, (295, 310))
    screen.blit(texto_score_gameover, (345, 255))
    score_gameover = fonte_num_score_gameover.render(str(score_atual), True, PRETO)
    if len(str(score_atual)) == 1:
        screen.blit(score_gameover, (370, 335))
    else:
        screen.blit(score_gameover, (350, 335))
    pygame.display.update()

def preparar_inicio_jogo(tp):
    img = lixeiras_imagens_tipos[tp]
    tam = img.get_size()
    tam_ajustado = (tam[0]*3, tam[1]*3)
    img = pygame.transform.scale(img, tam_ajustado)
    if tp == 'Plastico':
        img = pygame.transform.rotate(img, -30)
        return img

def iniciar_jogo(screen):
    img_lixo_plastico = preparar_inicio_jogo('Plastico')
    blit_tela_fase(tela, fase_atual, False)
    screen.blit(img_lixo_plastico, (-250, 300))
    pygame.display.update()
    time.sleep(2)

def relacionar_cores_tipos():
    cores = (AMARELO, PRETO, AZUL, VERMELHO, VERDE)
    cores_tipos = {}
    index = 0
    for tp in tipos:
        cores_tipos.update({tp: cores[index]})
        index += 1
    return cores_tipos
# ____________________________________________________________
pygame.init()
# ---------------------------------------------------------------------
# Imagens
cenarios_imagens = []
imagens_lixo_metal, imagens_lixo_organico, imagens_lixo_papel, imagens_lixo_plastico, imagens_lixo_vidro = [], [], [],\
                                                                                                           [], []
lixos_imagens_tipos = {'Metal': imagens_lixo_metal, 'Organico': imagens_lixo_organico, 'Papel': imagens_lixo_papel,
                       'Plastico': imagens_lixo_plastico, 'Vidro': imagens_lixo_vidro}
lixeiras_imagens_tipos = {'Metal': 'metal.png', 'Organico': 'organico.png', 'Papel': 'papel.png',
                          'Plastico': 'plastico.png', 'Vidro': 'vidro.png'}
lixos_principal = pygame.image.load(path_imagens_outras + 'lixos_principal.png')

tipos = ('Metal', 'Organico', 'Papel', 'Plastico', 'Vidro')
# -------------------------------------------------------------------
# CORES
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
VINHO = (150, 0, 0)
PRETO = (0, 0, 0)
tipo_cor = relacionar_cores_tipos()
# ___________________________________________________________________
# !!  TELAS  !!
telas = {}
tamanho_tela = (800, 680)
tela = pygame.display.set_mode(tamanho_tela, 0, 32)
pygame.display.set_caption('CATALIXO')
tela_atual = 'Tela_principal'
fundo_tela_pause = pygame.Surface((800, 680))
# botoes = Dict {Telas: {Tipos_Botoes: [Botões]}}
botoes = {}
# Textos
score_atual = 0
fonte_pause = pygame.font.SysFont('impact', 20)
fonte_score = pygame.font.SysFont('impact', 36)
fonte_score_gameover = pygame.font.SysFont('impact', 36)
fonte_highscore_gameover = pygame.font.SysFont('impact', 30)
fonte_num_score_gameover = pygame.font.SysFont('impact', 90)

texto_pause = fonte_pause.render("Pressione 'P' para pausar o jogo", True, PRETO)
texto_high_score = fonte_score.render("HIGH SCORE: " + get_highscore(), True, VINHO)
texto_score = fonte_score.render("SCORE: " + str(score_atual), True, VINHO)
# ----------------------------------
# Iniciar Elementos do Jogo
# --------------------------------
criar_imagens_lixeiras()
lixeiras = {'Metal': None, 'Organico': None, 'Papel': None,
            'Plastico': None, 'Vidro': None}
# Clock
clock = pygame.time.Clock()
if __name__ == '__main__':
    adicionar_imagens_lixos()
    adicionar_imagens_cenarios()
    adicionar_imagens_telas()
    lixeiras = LA.iniciar_lixeiras(lixeiras)
    print(f"telas: {telas}")
    print(f"Imagens cenarios: {cenarios_imagens}")
    print(f"Imagens lixos: {lixos_imagens_tipos}")
    print(f"Imagens lixeiras: {lixeiras_imagens_tipos}")
    print(f"Lixeiras iniciadas: {lixeiras}")
    print(f"Botões: {botoes}")
    print("Telas:")
    for k, v in telas.items():
        nums = list(range(len(v)))
        print(f'{k}: {v}')
    # Música
    pygame.mixer.music.load("bike_rides-TheGreenOrbs.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)
    musica = True

    pag = 1
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                click = True
                print(time.process_time())
                print(pygame.mouse.get_pos())

        if tela_atual == "Tela_principal":
            blit_tela_principal(tela, pygame.mouse.get_pos(), click)

        elif tela_atual == "Tela_instrucoes":
            blit_tela_instrucoes(tela, pygame.mouse.get_pos(), click)

        elif tela_atual == "Tela_gameover":
            blit_tela_gameover(tela, pygame.mouse.get_pos(), click, new_highscore)

        elif tela_atual == "Tela_jogo":
            score_atual = 0
            pause = False
            vidas = 5
            fase_atual = 1
            vilao = Vilao(fase_atual)
            running = True
            lixo = Lixo('Metal', imagens_lixo_metal[0], fase_atual)
            iniciar_jogo(tela)
            time.sleep(0.5)
            teste = True
            new_highscore = False
            while fase_atual <= 6 and vidas > 0:
                texto_vidas = fonte_score.render("VIDAS: " + str(vidas), True, VERMELHO)
                texto_score = fonte_score.render("SCORE: " + str(score_atual), True, VINHO)
                texto_tipo = fonte_score.render("TIPO: " + lixo.tipo, True, tipo_cor[lixo.tipo])
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == MOUSEBUTTONDOWN:
                        click = True
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            pause = True
                            tela_jogo_pausado = tela
                            while pause:
                                click = False
                                for ev in pygame.event.get():
                                    if ev.type == QUIT:
                                        pygame.quit()
                                        exit()
                                    if ev.type == MOUSEBUTTONDOWN:
                                        click = True
                                        x, y = pygame.mouse.get_pos()
                                        if 305 <= x <= 497 and 330 <= y <= 407:
                                            pause = False
                                        elif 305 <= x <= 497 and 440 <= y <= 520:
                                            pause = False
                                            tela_atual = 'Tela_principal'
                                        print(pygame.mouse.get_pos())
                                fundo_tela_pause.fill(VERDE)
                                fundo_tela_pause.set_alpha(7)
                                tela.blit(tela_jogo_pausado, (0, 0))
                                tela.blit(fundo_tela_pause, (0, 0))
                                tela.blit(telas['Tela_pause'][1], (0, 0))
                                blit_btn(tela, 'Tela_gameover', 'botao_musica', pygame.mouse.get_pos(), click)
                                pygame.display.update()
                        if event.key == K_d and fase_atual == 6:
                            lixo.girar_lixo('d')
                        if event.key == K_e and fase_atual == 6:
                            lixo.girar_lixo('e')

                if tela_atual == 'Tela_principal':
                    break
                # Tecla pressionada para movimentação
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    lixo.mover_lixo('e')
                elif pressed[pygame.K_RIGHT]:
                    lixo.mover_lixo('d')
                # Passagem de fases
                if score_atual >= 5 and fase_atual == 1:
                    fase_atual += 1
                    LA.mudar_sequencias(lixeiras)
                elif score_atual >= 10 and fase_atual == 2:
                    fase_atual += 1
                    LA.mudar_sequencias(lixeiras)
                elif score_atual >= 16 and fase_atual == 3:
                    fase_atual += 1
                    LA.mudar_sequencias(lixeiras)
                elif score_atual >= 24 and fase_atual == 4:
                    fase_atual += 1
                    LA.mudar_sequencias(lixeiras)
                elif score_atual >= 30 and fase_atual == 5:
                    fase_atual += 1
                    vilao = Vilao(fase_atual, boss=True)
                    LA.mudar_sequencias(lixeiras)
                elif score_atual >= 100 and fase_atual == 6:
                    fase_atual += 1
                blit_tela_fase(tela, fase_atual, True)

                for lixeira in lixeiras.values():
                    lixeira.desenhar_lixeira(tela)

                if not lixo.caindo:
                    if not vilao.aparecendo:
                        vilao.pos[0] = random.randint(0, 720)
                        vilao.aparecendo = True
                        tipo = random.choice(list(lixos_imagens_tipos.keys()))
                        indx = random.randint(0, len(lixos_imagens_tipos[tipo])-1)
                        lixo = Lixo(tipo, lixos_imagens_tipos[tipo][indx], fase_atual)
                    vilao.aparecer_topo(tela, lixo)
                elif lixo.caindo and vilao.aparecendo:
                    vilao.sumir_topo(tela)

                if lixo.caindo:
                    lixo.pos_y += lixo.velocidade
                    lixo.rect = lixo.criar_rect()
                    lixo.desenhar_lixo(tela)

                    # Colisão
                    if lixo.pos_y > 400:
                        for lxa in lixeiras.values():
                            colide = lixo.rect.colliderect(lxa.rect)
                            if colide:
                                if lixo.tipo == lxa.tipo and fase_atual < 6:
                                    score_atual += 1
                                elif lixo.tipo == lxa.tipo and fase_atual == 6:
                                    if lixo.angulo == 0:
                                        score_atual += 1
                                    else:
                                        vidas -= 1
                                else:
                                    vidas -= 1
                                lixo.desenhar_lixo(tela)
                                lixo.caindo = False
                    if lixo.pos_y > 600:
                        vidas -= 1
                        lixo.caindo = False
                """for lixeira in lixeiras.values():
                    pygame.draw.rect(tela, tipo_cor[lixeira.tipo], lixeira.rect, 4)
                pygame.draw.rect(tela, VERMELHO, lixo.rect, 2)"""
                pygame.display.update()
                tela_atual = 'Tela_gameover'
                texto_score_gameover = fonte_score_gameover.render("SCORE", True, BRANCO)
                if score_atual > int(get_highscore()):
                    set_highscore(score_atual)
                    texto_high_score = fonte_score.render("HIGH SCORE: " + get_highscore(), True, VINHO)
                    new_highscore = True
        clock.tick(30)
