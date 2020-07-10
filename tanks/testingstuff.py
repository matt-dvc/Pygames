import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((100, 100))
pygame.display.set_caption('gra')
clock = pygame.time.Clock()
vec2 = pygame.math.Vector2(1, 1)
vec1 = pygame.math.Vector2(0, 0)
vel = pygame.math.Vector2.rotate
crashed = False
while not crashed:
    crashed = True
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left')
                vec2 = vel(vec2, 1)

    print(vec2)
    pygame.math.Vector2.scale_to_length(vec2, 2)
    print(vec2)

    pygame.display.update()

    clock.tick(40)

pygame.quit()
