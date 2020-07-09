###########################
#
#     ALMOST A GAME
#     v.1.1
#     by @matt_dvc ®2020
#
###########################


import time
import math
import random
import pygame
import os


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 1280
display_height = 720
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ALMOST A GAME by matt_dvc ®2020')
clock = pygame.time.Clock()

boxes = []
random.seed()

gameExit = False
gap = 0
player_x = 10
player_y = 300
player_width = 50
player_height = 50
box_width = 100
box_height = 50
box_speed = 15
speed_increase = 0
timer = 0
max_time_alive = 0
coliding = False
health = 200
health_bar_lenght = health
health_bar_color = white
font = 20
score = 0
highscore = 0
player_shift_x = 0

planeImg = pygame.image.load('.\\files\\aircraft.png')
planeCrashImg = pygame.image.load('.\\files\\crash.png')
rockImg = pygame.image.load('.\\files\\asteroid.png')
color = planeImg


# CLASSES AND FUNCTIONS


class Box:
    def __init__(self, color, x, y, speed):

        self.color = color
        self.x = x
        self.y = y
        self.speed = speed

    def show(self):
        gameDisplay.blit(rockImg, (self.x, self.y))
       # pygame.draw.rect(gameDisplay, self.color, [
       #                  self.x, self.y, box_width, box_height])

        self.x -= self.speed


class Player:
    def __init__(self, color, x, y, shift):
        self.color = color
        self.x = x
        self.y = y
        self.shift = shift

    def spawn(self):
        if self.x <= 0:
            self.x = 0
        if self.x+100 >= display_width:
            self.x = display_width-100
        if self.y <= 0:
            self.y = 0
        if self.y+50 >= display_height:
            self.y = display_height-50
       # pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, 50, 50])
        gameDisplay.blit(pygame.transform.rotate(
            self.color, -self.shift), (self.x, self.y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def display_text(text, color, size, pos, adj):
    font_type = pygame.font.SysFont('8514fix', size)
    font_color = color
    TextSurf, TextRect = text_objects(text, font_type, font_color)
    if adj == 0:
        TextRect = pos
    if adj == 1:
        TextRect.center = pos
    # if adj == 2:
    #     TextRect.right, TextRect = (pos, 50)
    gameDisplay.blit(TextSurf, TextRect)


def collision():
    global coliding
    # for box in boxes:
    #     if (box.x < player.x+100 or box.x+100 < player.x+100) and (box.x > player.x or box.x+100 > player.x):
    #         if (box.y <= player.y+50 and box.y >= player.y) or (box.y+50 >= player.y and box.y+50 <= player.y+50):
    #             crash()
    for box in boxes:
        if (box.x < player.x+100) and (box.x+100 > player.x):  # LOL much easier
            if (box.y <= player.y+50) and (box.y+50 >= player.y):
                crash()


def crash():
    global coliding, health_bar_lenght
    coliding = True
    health_bar_lenght -= 2
   # print(health_bar_lenght)
    if health_bar_lenght < 1:
        end_screen()
    return coliding, health_bar_lenght


def health_bar(health_bar_color):
    if health_bar_lenght < 75:
        health_bar_color = (255, 255, 0)
    display_text('Health ', white, 30, (20, 20), 0)
    pygame.draw.rect(gameDisplay, health_bar_color, [
                     125, 20, health_bar_lenght, 30])


def scoreboard(score):
    global highscore
    pos_x = display_width - 100
    display_text('Best: '+str(highscore), white,
                 30, (pos_x, 30), 1)
    display_text('Score: '+str(score), white, 60,
                 (int(display_width/2), 60), 1)
    if score > highscore:
        highscore = score


def save_score():
    global highscore
    try:
        f = open('.\\files\\config.dat', 'r')
        score_check = f.read()

        if highscore > int(score_check, 0):
         #   print('grt')
            f = open('.\\files\\config.dat', 'w')
            f.write(str(hex(highscore)))
        else:
            highscore = int(score_check, 0)
       # print('Tried...')
    except:
        f = open('.\\files\\config.dat', 'w')
        f.write(str(hex(highscore)))
       # print('Exception...')


# MAIN GAME LOOPS
player = Player(color, player_x, player_y, player_shift_x)


def start_screen():
    notInGame = True
    save_score()
    while notInGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_loop()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        gameDisplay.fill(black)
        display_text('ALMOST A GAME', white, 144,
                     (int(display_width/2), int(display_height/3)), 1)
        display_text('Your goal is to avoid obstacles.', white, 64,
                     (int(display_width/2), int(display_height/2)), 1)
        display_text('Control your player with ARROW KEYS. Good luck and have fun!', white, 32,
                     (int(display_width/2), int(display_height/1.7)), 1)
        display_text('Press ENTER to start.          Press ESC to exit.', white, 48,
                     (int(display_width/2), int(display_height/1.4)), 1)

        display_text('Highscore: '+str(highscore), white, 72,
                     (int(display_width/2), int(display_height/1.1)), 1)

        pygame.display.update()
        clock.tick(30)


def end_screen():
    notInGame = True
    save_score()
    global highscore, score, boxes, health, health_bar_lenght
    while notInGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_reset = time.time()
                  #  print(start_reset)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    stop_reset = time.time()
                  #  print(stop_reset)
                    if stop_reset - start_reset > 2:
                        highscore = 0
                        os.remove('.\\files\\config.dat')

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            score = 0
            health, health_bar_lenght = 200, 200
            boxes = []
            game_loop()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        gameDisplay.fill(black)
        display_text('YOU ARE DEAD', red, 144,
                     (int(display_width/2), int(display_height/3)), 1)
       # display_text('Your goal is to avoid obstacles.', white, 64,
       #              (int(display_width/2), int(display_height/2)), 1)
        display_text('Your score: ' + str(score), white, 96,
                     (int(display_width/2), int(display_height/1.7)), 1)
        display_text('Press ENTER to start.          Press ESC to exit.', white, 48,
                     (int(display_width/2), int(display_height/1.1)), 1)
        display_text('Highscore: '+str(highscore), white, 48,
                     (int(display_width/2), int(display_height/1.4)), 1)
        display_text('Press and hold R to reset the Highscore', white, 15,
                     (int(display_width/2), int(display_height/1.3)), 1)

        pygame.display.update()
        clock.tick(30)


def game_loop():

    while not gameExit:

        # VARIABLES
        player_shift_y = 0
        global timer, coliding, gap, score

        # TIMER SECONDS
        timer += 1

        if timer % 4 == 0 and coliding == True:
            player.color = planeCrashImg
        if timer % 29 == 0:
            timer = 0
        if (timer % 4-2 == 0) and coliding == True:
            player.color = planeImg
        if timer % 10 == 0:
            player.color = planeImg
            coliding = False

        # KEY LOGIC
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    end_screen()

            if event.type == pygame.KEYUP:
                pass

        # PLAYER CONTROL

        if keys[pygame.K_UP]:
            player_shift_y = -10
        elif keys[pygame.K_DOWN]:
            player_shift_y = 10
        elif keys[pygame.K_LEFT]:
            player_shift_x = -15
        elif keys[pygame.K_RIGHT]:
            player_shift_x = 10
        else:
            player_shift_y = 0
            player_shift_x = 0
        player.y += player_shift_y
        player.x += player_shift_x

        # BLOCK SPAWN
        gap += 1
        if gap > random.randrange(5, 10):
            box_spawn_x = display_width
            box_spawn_y = random.randrange(5, display_height-50, 50)
            box_speed = random.randrange(7, 11)
            new_box = Box(red, box_spawn_x, box_spawn_y, box_speed)
            boxes.append(new_box)
            gap = 0

        for box in boxes:
            if box.x < -100:
                boxes.remove(box)
                score += 1

        # GRAPHICS DISPLAY
        gameDisplay.fill(black)
        for box in boxes:
            Box.show(box)

        player.spawn()
        collision()
        health_bar(health_bar_color)
        scoreboard(score)
        pygame.display.update()
        clock.tick(30)


start_screen()
