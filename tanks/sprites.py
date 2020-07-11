import pygame as pg
import settings as se
# import playerControls
vec = pg.math.Vector2
rot = pg.math.Vector2.rotate
gas = 0.1
bullets = []


class Player1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(se.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (se.displayWidth//4, se.displayHeight//2)
        self.pos = vec(se.displayWidth//4, se.displayHeight//2)
        self.vel = vec(-0.001, 0)
        self.acc = vec(0, 0)
        self.rot = 360
        self.leftPlayer = vec(0, 0)
        self.fired = 0

    def update(self):
        self.acc = vec(0, 0)
        self.drag = vec(0.1, 0.1)
        self.turnRate = int(se.ROT*(se.MAX_SPEED-self.vel.length())+1)
        self.fired += 1
        if self.turnRate > 5:
            self.turnRate = 5
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            # self.acc.x = -se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, -self.turnRate)
                self.rot -= se.ROT
        if keys[pg.K_RIGHT]:
            # self.acc.x = se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, self.turnRate)
                self.rot += se.ROT
        if keys[pg.K_UP]:
            # self.acc.y = -se.PLAYER_ACC-se.GRAVITY*0.1
            if self.vel.length() < 0.5:
                # self.acc = vec(self.vel.x*(abs(self.vel.length()-se.MAX_SPEED)),
                #                self.vel.y*(abs(self.vel.length()-se.MAX_SPEED)))
                self.acc = vec(self.vel.x*10,
                               self.vel.y*10)
            else:
                self.acc = vec(self.vel.x*gas*(abs(self.vel.length()-se.MAX_SPEED))/5,
                               self.vel.y*gas*(abs(self.vel.length()-se.MAX_SPEED))/5)

        if keys[pg.K_RCTRL] and self.fired > se.gameTick/2:
            bullets.append(Bullet(self.pos, self.vel))
            self.fired = 0

        if keys[pg.K_DOWN]:
            self.acc += self.vel * -0.05

        # added drag
        self.acc += self.vel * se.PLAYER_DRAG

        self.vel += self.acc

        if self.pos.x > se.displayWidth:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = se.displayWidth
        if self.pos.y > se.displayHeight:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = se.displayHeight
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
        # print(self.vel.length(), self.turnRate)


class Player2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(se.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (se.displayWidth//1.25, se.displayHeight//2)
        self.pos = vec(se.displayWidth//1.25, se.displayHeight//2)
        self.vel = vec(0.001, 0)
        self.acc = vec(0, 0)
        self.rot = 360
        self.leftPlayer = vec(0, 0)
        self.fired = 0

    def update(self):
        self.acc = vec(0, 0)
        self.drag = vec(0.1, 0.1)
        self.turnRate = int(se.ROT*(se.MAX_SPEED-self.vel.length())+1)
        self.fired += 1
        if self.turnRate > 10:
            self.turnRate = 10
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            # self.acc.x = -se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, -self.turnRate)
                self.rot -= se.ROT
        if keys[pg.K_d]:
            # self.acc.x = se.PLAYER_ACC
            if self.vel != vec(0, 0):
                self.vel = rot(self.vel, self.turnRate)
                self.rot += se.ROT
        if keys[pg.K_w]:
            # self.acc.y = -se.PLAYER_ACC-se.GRAVITY*0.1
            if self.vel.length() < 0.5:
                # self.acc = vec(self.vel.x*(abs(self.vel.length()-se.MAX_SPEED)),
                #                self.vel.y*(abs(self.vel.length()-se.MAX_SPEED)))
                self.acc = vec(self.vel.x*10,
                               self.vel.y*10)
            else:
                self.acc = vec(self.vel.x*gas*(abs(self.vel.length()-se.MAX_SPEED))/5,
                               self.vel.y*gas*(abs(self.vel.length()-se.MAX_SPEED))/5)

        if keys[pg.K_s]:
            self.acc += self.vel * -0.05

        if keys[pg.K_TAB] and self.fired > se.gameTick/2:
            bullets.append(Bullet(self.pos, self.vel))
            self.fired = 0

        # added drag
        self.acc += self.vel * se.PLAYER_DRAG

        self.vel += self.acc

        if self.pos.x > se.displayWidth:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = se.displayWidth
        if self.pos.y > se.displayHeight:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = se.displayHeight
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
        # print(self.vel.length(), self.turnRate)


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos, vel):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(se.RED)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.vel = pg.math.Vector2.normalize(vel)*(se.MAX_SPEED+2)
        self.rect.center = (self.pos.x, self.pos.y)

    def update(self):
        self.pos = self.pos+self.vel
        self.rect.center = self.pos
