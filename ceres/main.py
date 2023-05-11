import os.path

import pygame
from pygame import Vector2

import core
from ceres.states import States


def setup():
    core.WINDOW_SIZE = [1280, 720]
    core.fps = 60
    core.memory('states', States.START)


def run():
    core.cleanScreen()
    if core.memory('states') == States.START:
        display_start()


def draw_start_menu():
    text_spacequest((255, 255, 255), 'CERES', (440, 40))
    text_spacequest((255, 255, 255), 'ENHANCED', (320, 140))


def display_start():
    core.memory("texture", core.Texture("assets/img/background.jpg", Vector2(0, 0), 0, [1280, 720]))

    if core.memory('states') == States.START:
        draw_start_menu()

    if not core.memory("texture").ready:
        core.memory("texture").load()
    core.memory("texture").show()

    draw_start_menu()


def display_game():
    core.setBgColor(0, 0, 0)


def display_gameover():
    pass


def text_spacequest(color, texte, position):
    myfont = pygame.font.Font("assets/fonts/Spacequest.ttf", 120)
    textsurface = myfont.render(texte, False, color)
    if len(color) > 3:
        textsurface.set_alpha(color[3])
    core.screen.blit(textsurface, position)


core.main(setup, run)
