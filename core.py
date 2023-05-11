import copy
import inspect
import sys
from math import *
from random import *

import pygame

import core

title = "Fenetre"
bgColor = (0, 0, 0)
screenCleen = True
runfuntion = None
setupfunction = None
screen = None
fps = 60
loopLock = False
WINDOW_SIZE = [100, 100]
width = 0
height = 1
mouseclickleft = None
mouseclickL = False
mouseclickright = [-1, -1]
mouseclickR = False
keyPress = False
keyPressValue = None
keyReleaseValue = None
keyPressList = None
memoryStorage = {}
keyReleaseList = None
fullscreen = False

def printMemory():
    print("--------------MEMORY:-------------------")
    for k, v in memoryStorage.items():
        print("Nom : ", k, " Valeur :", v, " Type : ", type(v))
    print("----------------------------------------")
    print("\n")


def memory(key: object, value: object = None) -> object:
    global memoryStorage
    if " " in key:
        sys.stderr.write("ERREUR : Espace interdit dans les noms de variable : " + key + "\n")
        sys.exit()
    if value is not None:
        memoryStorage[key] = value
    else:
        try:
            return memoryStorage[key]
        except:
            sys.stderr.write("ERREUR : Nom de variable inconnue : " + key)
            sys.exit()


def setTitle(t):
    global title
    title = t


def setBgColor(c):
    global bgColor
    bgColor = c


def noLoop():
    global loopLock
    loopLock = True


def cleanScreen():
    global screenCleen
    screenCleen = True


def getMouseLeftClick():
    if mouseclickL:
        return mouseclickleft


def getMouseRightClick():
    if mouseclickR:
        return mouseclickright


def getkeyPress():
    return keyPress


def getKeyPressList(value):
    if keyPressList is not None:
        key = getattr(pygame, 'K_' + str(value))
        if len(keyPressList) > key:
            return keyPressList[key] == 1
    return False


def getKeyReleaseList(value):
    if keyReleaseList is not None:
        key = getattr(pygame, 'K_' + str(value))
        if len(keyReleaseList) > key:
            return keyReleaseList[key] != 0
    return False


def getkeyPressValue():
    return keyPressValue


def getkeyRelease():
    return keyReleaseValue


def setup():
    pygame.init()
    global WINDOW_SIZE
    WINDOW_SIZE
    if (setupfunction is not None):
        setupfunction()

    global screen
    if not fullscreen:
        screen = pygame.display.set_mode(WINDOW_SIZE)
    else:
        screen = pygame.display.set_mode(
            (0,0),
            pygame.FULLSCREEN
        )
        WINDOW_SIZE = (screen.get_size())
    # Set title of screen
    pygame.display.set_caption(title)


def run():
    if (runfuntion is not None):
        runfuntion()


def main(setupf, runf):
    print(inspect.stack()[1].function)
    global runfuntion
    runfuntion = runf
    global setupfunction
    setupfunction = setupf
    global keyPressList, keyReleaseList, screenCleen, mouseclickleft, mouseclickL, mouseclickright, mouseclickR, keyPress, keyPressValue, keyReleaseValue, screen

    setup()

    clock = pygame.time.Clock()

    done = False
    print("Run START-----------")
    while not done:

        if not loopLock:
            if screenCleen:
                screenCleen = False
                screen.fill(bgColor)
                pygame.display.set_caption(title)

            run()

        if keyReleaseList is not None:
            keyReleaseList = [i - 1 if i > 0 else 0 for i in keyReleaseList]

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.KEYDOWN:
                keyPress = True
                keyPressValue = event.key


            elif event.type == pygame.KEYUP:
                keyPressValue = None
                if keyReleaseList is None:
                    keyReleaseList = [0 for i in keyPressList]

                for i, k in enumerate(keyPressList):
                    if k == True and event.scancode == i:
                        keyReleaseList[event.key] = 1






            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    mouseclickL = True
                    mouseclickleft = event.pos
                if event.button == 3:
                    mouseclickR = True
                    mouseclickright = event.pos


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouseclickL = False
                    mouseclickleft = None
                if event.button == 3:
                    mouseclickR = False
                    mouseclickright = None

            elif event.type == pygame.MOUSEMOTION:
                if mouseclickL:
                    mouseclickleft = event.pos
                if mouseclickR:
                    mouseclickright = event.pos

            if hasattr(event, 'key'):

                keyPressList = [pygame.key.get_pressed()[i] for i in range(0,len(pygame.key.get_pressed()))]

                if keyPressValue:
                    keyReleaseValue = event.key
                else:
                    keyReleaseValue = None

        clock.tick(fps)

        # print(clock.get_time())
        # Go ahead and update the screen with what we 've drawn.
        pygame.display.flip()


class Math:
    def map(value, istart, istop, ostart, ostop):
        return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


class Draw:
    def rect(color, rect, width=0):
        if len(color) > 3:
            shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            core.screen.blit(shape_surf, rect)
        else:
            pygame.draw.rect(core.screen, color, rect, width)

    def circle(color, center, radius, width=0):
        if len(color) > 3:
            target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
            shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
            pygame.draw.circle(shape_surf, color, (radius, radius), radius, width)
            core.screen.blit(shape_surf, target_rect)
        else:
            pygame.draw.circle(core.screen, color, center, radius, width)

    def polyline(color, points, width=0):
        if len(color) > 3:
            surface = screen.convert_alpha()
            surface.fill([0, 0, 0, 0])
            pygame.draw.polygon(surface, color, points, width)
            screen.blit(surface, (0, 0))
        else:
            pygame.draw.polygon(core.screen, color, points, width)

    def line(color, start_pos, end_pos, width=1):
        if len(color) > 3:
            surface = screen.convert_alpha()
            surface.fill([0, 0, 0, 0])
            pygame.draw.line(surface, color, start_pos, end_pos, width)
            screen.blit(surface, (0, 0))
        else:
            pygame.draw.line(core.screen, color, start_pos, end_pos, width)

    def ellipse(color, rect, width=0):

        if len(color) > 3:
            shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.ellipse(shape_surf, color, shape_surf.get_rect(), width)
            core.screen.blit(shape_surf, rect)
        else:
            pygame.draw.ellipse(core.screen, color, rect, width)

    def arc(color, rect, start_angle, stop_angle, width=1):
        if len(color) > 3:
            shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.arc(shape_surf, color, rect, start_angle, stop_angle, width)
            core.screen.blit(shape_surf, rect)
        else:
            pygame.draw.arc(core.screen, color, rect, start_angle, stop_angle, width)


    def lines(color, closed, points, width=1):
        if len(color) > 3:
            surface = screen.convert_alpha()
            surface.fill([0, 0, 0, 0])
            pygame.draw.lines(surface, color, closed, points, width)
            screen.blit(surface, (0, 0))
        else:
            pygame.draw.lines(core.screen, color, closed, points, width)

    def polygon(color, points, width=0):
        if len(color) > 3:
            lx, ly = zip(*points)
            min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
            target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
            shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
            pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
            core.screen.blit(shape_surf, target_rect)
        else:
            pygame.draw.polygon(core.screen, color, points, width)

    def text(color, texte, position, taille=30, font='Arial'):
        pygame.font.init()
        myfont = pygame.font.SysFont(font, taille)
        textsurface = myfont.render(texte, False, color)
        if len(color)>3:
            textsurface.set_alpha(color[3])
        screen.blit(textsurface, position)


class Sound:

    def __init__(self,url):
        self.ready = False
        self.url = url
        self.play=False
        self.thread=None
        if self.url!="":
            pygame.mixer.pre_init(44100, -16, 2, 2048)
            pygame.mixer.init()
            pygame.mixer.music.load(url)

    def start(self):
        if not self.play:
            self.play = True
            self.thread=threading.Thread(target=self.playin(), args=(1,))

    def rewind(self):
        if self.play:
            pygame.mixer.music.rewind()

    def pause(self):
        if self.play:
            self.play = False
            pygame.mixer.music.pause()
        else:
            self.play = True
            pygame.mixer.music.unpause()


    def stop(self):
        if self.play:
            self.play = False
            pygame.mixer.music.stop()



    def playin(self):
        pygame.mixer.music.play()
        print("playin")

class Texture:
    def __init__(self, url, pos=pygame.Vector2(), offset=0, scaleSize=(100, 100), display=True,alpha=255):
        self.ready = False
        self.sprit = None
        self.url = url
        self.w = None
        self.h = None
        self.pos = pos
        self.scaleSize = scaleSize
        self.angle = 0
        self.offset = offset
        self.display = display
        self.alpha=alpha
        self.box=False

    def load(self):

        self.sprit = pygame.image.load(self.url).convert_alpha()
        self.sprit = pygame.transform.scale(self.sprit, self.scaleSize)
        self.w = self.sprit.get_width()
        self.h = self.sprit.get_width()
        self.ready = True

    def show(self):
        if self.display:
            if self.box:
                core.Draw.rect((0,255,0),(self.pos.x,self.pos.y,self.w,self.h),1)
            if self.ready:
                self.sprit.set_alpha(self.alpha)
                rotated_image = pygame.transform.rotate(self.sprit, self.angle)
                new_rect = rotated_image.get_rect(center=self.sprit.get_rect(topleft=self.pos).center)

                core.screen.blit(rotated_image, new_rect)


