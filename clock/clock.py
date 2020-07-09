import pygame
import numpy as np
import time
import os
import math

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

######## DISPLAY SETTINGS #######

display_width = 720
display_height = 720
game_tick = 60
center = (int(display_width/2), int(display_height/2))
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()

####### MAIN PROGRAM LOOP #######


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def show_text(text, color, size, pos, adj):
    font_type = pygame.font.SysFont('', size)
    font_color = color
    TextSurf, TextRect = text_objects(text, font_type, font_color)
    if adj == 0:
        TextRect = pos
    if adj == 1:
        TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


def line(start, finish, width, color):
    pygame.draw.line(gameDisplay, color, start, finish, int(width))


def circle(pos, r, c, b):
    pygame.draw.circle(gameDisplay, c, pos, r, b)


def draw_lines(many_lines):
    for lines in many_lines:
        if lines:
            pygame.draw.lines(gameDisplay, green, False, lines, 3)


def mouse_data(mouse, x, y):

    max_pos = [display_width-60, 20]
    pos_x = mouse[0]+50  # -center[0]
    pos_y = mouse[1]-30  # -center[1]
    if pos_x > max_pos[0]:
        pos_x = max_pos[0]
    if pos_y < max_pos[1]:
        pos_y = max_pos[1]

    show_text(str((x, y)), white, 30, (pos_x, pos_y), 1)


def main_loop():

    inMainLoop = True
    loop_timer = 0
    time_in_game_sec = 40
    time_in_game_min = 47

    pygame.mouse.set_visible(0)

    while inMainLoop == True:

        gameDisplay.fill(black)
        ######## MAIN LOOP TIMER #########

        loop_timer += 1
       # print(time_in_game_sec, loop_timer)

        if loop_timer == game_tick:
            loop_timer = 0
            time_in_game_sec += 1
            time_in_game_min += 1
       #     print(time_in_game_sec)
        # print(loop_timer)
        if time_in_game_sec == 60:
            time_in_game_sec = 0
        ####### KEY / EVENT LOGIC #######

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

            if event.type == pygame.KEYUP:
                pass

        if mouse_button == (1, 0, 0):
            pass
        if mouse_button == (0, 1, 0):
            pass
        if mouse_button == (0, 0, 1):
            pass
        if mouse_button == (0, 0, 0):
            pass

        ####### MAIN CODE BEGIN ########

        # a2+b2=c2
        x = -int(center[0]-mouse[0])  # len       c   | y
        y = int(center[1]-mouse[1])  # hei   ___x___ |

        c = int(np.sqrt((x*x+y*y)))  # c

        try:
            angle_deg = np.degrees(np.arctan(y/x))
            angle_rad = np.arctan((x/y))
        except Exception as e:
            angle = 90
            print(e)
        line_lenght = 290
        second = np.pi/30*int(time.time())
        minute = second/60
        hour = np.pi/6*time.time()/3600+np.pi/6

        a = np.sin(second)*275  # angle_rad
        b = np.cos(second)*275  # angle_rad
        s1 = np.sin(minute)*250
        s2 = np.cos(minute)*250
        h1 = np.sin(hour)*150
        h2 = np.cos(hour)*150
        for i in range(12):
            x_dot = int(np.sin(np.pi/6*i) * 275)+center[0]
            y_dot = int(np.cos(np.pi/6*i)*275)+center[1]
          #  print(x_dot, y_dot)
            circle((x_dot, y_dot), 15, white, 15)
        # if y < 0:
        #     a = a*-1     ###angle rad
        #     b = b*-1

        line(center, tuple(np.add(center, (int(h1), -int(h2)))), 7, yellow)
        circle(tuple(np.add(center, (int(h1), -int(h2)))), 10, yellow, 10)
        line(center, tuple(np.add(center, (int(s1), -int(s2)))), 5, green)
        circle(tuple(np.add(center, (int(s1), -int(s2)))), 10, green, 10)
        line(center, tuple(np.add(center, (int(a), -int(b)))), 5, red)
        circle(tuple(np.add(center, (int(a), -int(b)))), 10, red, 10)
        circle(center, 20, red, 20)

        circle(center, 300, white, 5)
        if loop_timer == 0:
            print()
            print(x, 'X ', y, 'Y', angle_deg)
            print(round(a, 2), round(b, 2))
            print(minute, second)

        ####### MAIN CODE END ##########

        ####### RENDERING ##############
        #show_text('X', white, 32, (display_width-30, center[1]+30), 1)
        #show_text('Y', white, 32, (center[0]-30, 30), 1)
        # show_text('(0,0)', white, 32, (tuple(
        #    np.subtract(center, (30, -20)))), 1)
        #line((center[0], 0), (center[0], display_height), 3, white)
        #line((0, center[1]), (display_width, center[1]), 3, white)
        #mouse_data(mouse, x, y)
        circle(mouse, 5, white, 5)

        pygame.display.update()
        clock.tick(game_tick)


main_loop()
