import pygame as pg
import settings as se
import sprites as sp
# from sprites import *


class Game:
    def __init__(self):

        pg.init()
        self.win = pg.display.set_mode((se.displayWidth, se.displayHeight))
        self.clock = pg.time.Clock()
        pg.display.set_caption(se.title)
        self.running = True
        self.x = 10

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(se.gameTick)
            self.events()
            self.update()
            self.draw()

    def new(self):
        # self.playerList = []
        self.all_sprittes = pg.sprite.Group()
        self.all_bullets = pg.sprite.Group()
        self.player1 = sp.Player1()
        self.player2 = sp.Player2()
        self.all_sprittes.add(self.player1)
        self.all_sprittes.add(self.player2)
        # self.circlePlayer = sp.CirclePlayer(self.win)
        # self.all_sprittes.add(self.circlePlayer)
        # print(self.playerList)
        self.run()

    def update(self):
        self.all_sprittes.update()
        self.all_bullets.update()
        print(len(sp.bullets))
        print(len(self.all_bullets))
        for bullet in sp.bullets:
            self.all_bullets.add(bullet)
            if len(sp.bullets) > 20:
                sp.bullets.pop(0)
                self.all_bullets.remove(bullet)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                if self.playing:
                    self.playing = False
                self.running = False
                pg.quit()
                quit()

    def draw(self):
        self.win.fill(se.BLACK)
        self.all_sprittes.draw(self.win)
        self.all_bullets.draw(self.win)
        # self.x += 1
        # if self.x > se.displayWidth:
        #     self.x = 0
        #     self.win.fill(se.BLACK)
        # pg.draw.circle(self.win, se.WHITE,
        #                (self.x, int(50*self.player.vel.length())), 10)
        # for circlePlayer in self.playerList:
        #    circlePlayer.update()
        #    print(circlePlayer.pos, circlePlayer.vel, circlePlayer.acc)
        #    circlePlayer.image
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_end_screen(self):
        pass


G = Game()
while G.running:
    G.new()
    G.show_end_screen()

pg.quit()
