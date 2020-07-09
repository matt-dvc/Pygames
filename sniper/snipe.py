import pygame
import numpy as np
import time
import os

pygame.init()

######## BASIC COLOURS ##########

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
grey = (127, 127, 127)

######## DISPLAY SETTINGS #######

display_width = 1280
display_height = 720
center = (int(display_width/2), int(display_height/2))
game_tick = 60
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PROGRAM NAME. EXC TO EXIT')
clock = pygame.time.Clock()

####### MAIN PROGRAM LOOP #######

score = 0
fire = 0
shot = 0


def line(start, finish, width, color):
    pygame.draw.line(gameDisplay, color, start, finish, int(width))


def circle(pos, r, c, b):
    pygame.draw.circle(gameDisplay, c, pos, r, b)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def show_text(text, color, size, pos, adj):
    font_type = pygame.font.SysFont('', size)
    font_color = color
    TextSurf, TextRect = text_objects(str(text), font_type, font_color)
    if adj == 0:
        TextRect = pos
    if adj == 1:
        TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


def crosshair(pos, colour):
    circle(pos, 52, colour, 5)
    line((pos[0]-50, pos[1]), (pos[0]+50, pos[1]), 2, colour)
    line((pos[0], pos[1]-50), (pos[0], pos[1]+50), 2, colour)


def spawn_circle():
    x = np.random.choice((np.arange(50, display_width-50, 1)))
    y = np.random.choice((np.arange(50, display_height-50, 1)))
    return (x, y)


def bullet_hole(pos, holes, targets, mouse_button):
    holes.append(pos)


def end_screen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_ESCAPE:
        #         pygame.quit()
        #         quit()
    gameDisplay.fill(grey)
    show_text(str('SCORE: ' + str(score)), yellow, 100, center, 1)
    show_text('ENTER to start.', yellow, 40, (center[0], center[1]+200), 1)
    try:
        accuracy = round(shot/fire*100, 2)
    except:
        accuracy = 100
    show_text(str('Accuracy: ' + str(accuracy)+' %'),
              yellow, 60, (center[0], center[1]+70), 1)

    crosshair(pygame.mouse.get_pos(), white)
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        main_loop()
    pygame.display.update()


def main_loop():

    global score, fire, shot
    inMainLoop = True
    loop_timer = 0
    time_in_game_sec = 0
    pygame.mouse.set_visible(False)
    colour = white
    targets = []
    holes = []
    score = 0
    fire = 0

    while inMainLoop == True:

        gameDisplay.fill(grey)
        ######## MAIN LOOP TIMER #########

        loop_timer += 1
       # print(time_in_game_sec, loop_timer)

        if loop_timer == game_tick:
            loop_timer = 0
            time_in_game_sec += 1
            print(time_in_game_sec)

        ####### KEY / EVENT LOGIC #######

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()

        if not targets:
            target = spawn_circle()
            targets.append(target)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_ESCAPE:
            #         pygame.quit()
            #         quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                colour = black
                bullet_hole(mouse, holes, targets, mouse_button)
                fire += 1
                for target in targets:
                    print(mouse, target)

                    sqx = (mouse[0]-target[0])**2
                    sqy = (mouse[1]-target[1])**2
                    if 25 <= np.sqrt(sqx+sqy) < 50:
                        targets.clear()
                        score += 1
                        shot += 1
                    if 15 <= np.sqrt(sqx+sqy) < 25:
                        targets.clear()
                        score += 2
                        shot += 1
                    if np.sqrt(sqx+sqy) < 15:
                        targets.clear()
                        score += 3
                        shot += 1

            if event.type == pygame.KEYUP:
                pass

      #  print(fire)
        ####### MAIN CODE BEGIN ########

        for hole in holes:
            circle(hole, 10, (80, 80, 80), 10)
            circle(hole, 5, black, 5)

        countdown = 60 - time_in_game_sec

        # print(*targets)
        for target in targets:
            circle(target, 50, red, 50)
            circle(target, 25, white, 15)

        if mouse_button == (0, 0, 0):
            colour = white
        crosshair(mouse, colour)
        show_text(score, yellow, 40, (10, 10), 0)
        show_text(countdown, yellow, 40, (display_width-50, 10), 0)
        if countdown < 0:
            inMainLoop = False
        # print(len(holes))
        ####### MAIN CODE END ##########

        ####### RENDERING ##############

        pygame.display.update()
        clock.tick(game_tick)
   # return score, fire


while True:
    end_screen()
