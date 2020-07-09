import pygame
import numpy as np
import time
import os

pygame.init()

######## BASIC COLOURS ##########

white = (255, 255, 255)
black = (0, 0, 0)
gray = (127, 127, 127)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

######## DISPLAY SETTINGS #######

display_width = 1280
display_height = 720
game_tick = 15
background = black
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PROGRAM NAME. EXC TO EXIT')
clock = pygame.time.Clock()

####### MAIN PROGRAM LOOP #######


class Snake:
    def __init__(self, pos, move):
        self.pos = pos
        self.move = move

    def head(self):
        self.pos = tuple(np.add(self.pos, self.move))
      #  print(self.pos, self.move)
        pygame.draw.circle(
            gameDisplay, green, (self.pos), 10)
        return self.pos


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def display_text(text, color, size, pos, adj):
    font_type = pygame.font.SysFont('', size)
    font_color = color
    TextSurf, TextRect = text_objects(text, font_type, font_color)
    if adj == 0:
        TextRect = pos
    if adj == 1:
        TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


def body(pos):
    pygame.draw.circle(
        gameDisplay, green, (pos), 10)


def board(score):
    pygame.draw.rect(gameDisplay, gray, [
                     0, 0, display_width, display_height], 100)

    display_text('S N A K E       by @matt_dvc ©2020', yellow, 72,
                 (int(display_width/2), int(25)), 1)
    display_text('SCORE : ' + str(score), white, 72,
                 (int(display_width/2), int(display_height-22)), 1)


def dead(score):

    display_text('GAME OVER', red, 200,
                 (int(display_width/2), int(display_height/2)), 1)
    display_text('SCORE : ' + str(score), yellow, 144,
                 (int(display_width/2), int(display_height/1.5)), 1)
    display_text('Press ENTER to play.', yellow, 40,
                 (int(display_width/2), int(display_height/1.2)), 1)
    pygame.display.update()
    inMainLoop = False
    start_screen()


def start_screen():
    notInGame = True
    while notInGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            main_loop()


def spawn_fruit():

    fruit_pos_x = np.random.choice(np.arange(100, display_width-100, 20))
    fruit_pos_y = np.random.choice(np.arange(100, display_height-100, 20))
    fruit_pos = (fruit_pos_x, fruit_pos_y)
    fruit_eaten = False
    return fruit_pos


def draw_fruit(fruit_pos):
    pygame.draw.circle(gameDisplay, red, (fruit_pos), 10)


def main_loop():

    inMainLoop = True
    loop_timer = 0
    time_in_game_sec = 0
    last_move = (0, 0)
    init_move = (0, 0)
    init_pos = (int(display_width/2), int(display_height/2))
    pos = init_pos
    move = last_move
    head_last_pos = init_pos
    fruit_pos = (0, 0)
    spawn = True
    snake_body = []
    head = Snake(pos, move)
    fruit_eaten = True
    snake_lenght = 0
    direction = 0
    score = 0
    isDead = False
    while inMainLoop == True:

        gameDisplay.fill(background)

        ######## MAIN LOOP TIMER #########

        loop_timer += 1
        if loop_timer == game_tick:
            loop_timer = 0
            time_in_game_sec += 1

        ####### KEY / EVENT LOGIC #######

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        last_move = move

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYUP:
                pass

        if keys[pygame.K_UP]:
            if direction != 6:

                move = (0, -20)
                direction = 12
                last_move = move
        elif keys[pygame.K_DOWN]:
            if direction != 12:
                move = (0, 20)
                direction = 6
                last_move = move
        elif keys[pygame.K_LEFT]:
            if direction != 3:
                move = (-20, 0)
                direction = 9
                last_move = move
        elif keys[pygame.K_RIGHT]:
            if direction != 9:
                move = (20, 0)
                direction = 3
                last_move = move
        else:
            move = last_move

        ####### MAIN CODE BEGIN ########

        board(score)

        if fruit_eaten == True:
            fruit_pos = spawn_fruit()
        draw_fruit(fruit_pos)
        fruit_eaten = False

        head.move = move
        snake_body.append(head.pos)

        if head.pos == fruit_pos:
            snake_body.append(head.pos)
            snake_lenght += 5
            score += 1
            fruit_eaten = True

        if head.pos[0] <= 50 or head.pos[0] >= display_width-50 or head.pos[1] <= 50 or head.pos[1] >= display_height-50:
            isDead = True
            dead(score)

        if not isDead:

            Snake.head(head)

            if len(snake_body) > snake_lenght:
                snake_body.pop(0)

            for chunks in snake_body:
                body(chunks)
            for chunks in snake_body:
                if head.pos == chunks:

                    isDead = True
                    dead(score)

            ####### MAIN CODE END ##########

            ####### RENDERING ##############

        if not isDead:
            pygame.display.update()
        clock.tick(game_tick)


main_loop()
dead()
