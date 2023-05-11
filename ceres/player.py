import random

from pygame import Vector2

import core


class Player:
    def __int__(self):
        self.debug = False
        self.name = "Vaisseau"
        self.uuid = random
        self.mass = 10
        self.vMax = 10
        self.accMax = 5
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.acc = Vector2(0,0)
        self.speed = Vector2 (0,0)


    core.memory("texture", core.Texture("assets/img/ship.jpg", Vector2(0, 0), 0, [100, 50]))


    def movements(self):
        pass


    def growing(self):
        pass

    def loss(self):
        pass

    def show(self):
        core.Draw.polygon(self.position)

    if core.getKeyPressList("z") :
        core.memory("direction", Vector2(core.memory("direction").y, 1))

    if core.getKeyPressList("Q") :
        core.memory("direction",Vector2(core.memory("direction").x, 1))

    if core.getKeyPressList("D") :
        core.memory("direction",Vector2(core.memory("direction").x, -1))

