import os.path

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

    pass


def load_assets(self):
    self.fonts_dir = os.path.join(self.fonts_dir, 'font')


core.main(setup, run)
