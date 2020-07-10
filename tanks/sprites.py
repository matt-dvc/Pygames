import pygame as pg
import settings as se
vec = pg.math.Vector2
rot = pg.math.Vector2.rotate
gas = 0.05


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(se.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (se.displayWidth//2, se.displayHeight//2)
        self.pos = vec(se.displayWidth//2, se.displayHeight//2)
        self.vel = vec(0, -0.001)
        self.acc = vec(0, 0)
        self.rot = 360

    def update(self):
        self.acc = vec(0, 0)
        self.drag = vec(0.1, 0.1)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            # self.acc.x = -se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, -se.ROT)
                self.rot -= se.ROT
        if keys[pg.K_RIGHT]:
            # self.acc.x = se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, se.ROT)
                self.rot += se.ROT
        if keys[pg.K_UP]:
            #self.acc.y = -se.PLAYER_ACC-se.GRAVITY*0.1
            if self.vel.length() < 0.5:
                self.acc = vec(self.vel.x*gas*(abs(self.vel.length()-4)),
                               self.vel.y*gas*(abs(self.vel.length()-4)))
            else:
                self.acc = vec(self.vel.x*gas*(abs(self.vel.length()-4))/5,
                               self.vel.y*gas*(abs(self.vel.length()-4))/5)

        if keys[pg.K_DOWN]:
            self.acc.y = se.PLAYER_ACC

        # added drag
        self.acc += self.vel * se.PLAYER_DRAG

        self.vel += self.acc

        if se.displayWidth <= self.pos.x or self.pos.x <= 0:
            self.vel.x *= -1
        if se.displayHeight <= self.pos.y or self.pos.y <= 0:
            self.vel.y *= -1
        # print(self.vel, self.vel.rotate(10))
        # motion equations
        if self.vel.length() < 0.5:
            pass
        else:
            self.pos += self.vel+0.5*self.acc
        # self.pos += vec(0, se.GRAVITY)
        self.rect.center = self.pos
        if self.rot > 719 or self.rot < 1:
            self.rot = 360
        # print(self.rot-360, self.vel.length())
