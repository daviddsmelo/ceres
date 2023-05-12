import random

from pygame import Vector2, Vector3

import core


class Player:
    def __int__(self):
        self.position = Vector2()
        self.acc = Vector2()
        self.vMax = 1
        self.aMax = 1
        self.orientation = Vector2()

    def show(self):
        p1 = Vector2(self.orientation)
        p1.scale_to_length(10)
        p1 = self.position + p1.rotate(90)

        p1 = Vector2(self.orientation)
        p1.scale_to_length(10)
        p1 = self.position + p1.rotate(90)

    def drawPlayer():
        p1 = Vector2(core.memory("vaisseauPosition").x,core.memory("vaisseauPosition").y) + Vector2(-5,0).rotate(180 - core.memory("vaisseauPosition").z)
        p1.y = -p1.y
        p1 = p1 + core.memory("origine")

        p2 = Vector2(core.memory("vaisseauPosition").x, core.memory("vaisseauPosition").y) + Vector2(0,-15).rotate(180 - core.memory("vaisseauPosition").z)
        p2.y = -p2.y
        p2 = p2 + core.memory("origine")

        p3 = Vector2(core.memory("vaisseauPosition").x, core.memory("vaisseauPosition").y) + Vector2(5, 0).rotate(180 - core.memory("vaisseauPosition").z)
        p3.y = -p3.y
        p3 = p3 + core.memory("origine")

        core.Draw.polygon(255,0,0), ((p1), (p2), (p3))

    def movePlayer():
        core.memory("PLayerHistorique").append(Vector2(core.memory("vaisseauPosition").x, -core.memory("vaisseauPosition").y) + core.memory("origine"))

        vel = Vector2(random.randint(-10,10), random.randint(10,-10))
        angle = ( vel.angle_to(Vector2(0,1)) + core.memory("vaisseauPosition").z ) % 360
        posx = core.memory("vaisseauPosition").x +vel.x
        posy = core.memory("vaisseauPosition").y +vel.y
        core.memory("vaisseauPosition", Vector3(posx,posy,angle))




