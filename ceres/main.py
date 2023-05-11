import os.path

import pygame

import core
from ceres.states import States


def setup():
    core.WINDOW_SIZE = [1280, 720]
    core.fps = 60
    core.memory('states', States.START)


def run():
    core.cleanScreen()
    if core.memory('states') == States.START:
        draw_start_menu()


def draw_start_menu():
    core.setBgColor((255, 255, 255))
    text_hyperspace((0, 0, 0), 'ASTEROÏDES', (285, 180))


def text_hyperspace(color, texte, position):
    myfont = pygame.font.Font("assets/fonts/HyperspaceBold-GM0g.ttf", 120)
    textsurface = myfont.render(texte, False, color)
    if len(color) > 3:
        textsurface.set_alpha(color[3])
    core.screen.blit(textsurface, position)


core.main(setup, run)
