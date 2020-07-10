import pygame
import settings


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def show_text(win, text, color, size, pos, adj):
    fontType = pygame.font.SysFont('', size)
    TextSurf, TextRect = text_objects(text, fontType, color)
    if adj == 0:
        TextRect = pos
    if adj == 1:
        TextRect.center = pos
        win.blit(TextSurf, TextRect)


def line(win, start, finish, width, color):
    pygame.draw.line(win, color, start, finish, int(width))


def circle(win, pos, r, c, b):
    pygame.draw.circle(win, c, pos, r, b)


def rectangle(win, pos, c, b):
    pygame.draw.Rect()
