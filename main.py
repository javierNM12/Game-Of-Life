import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import grid

pygame.init()

width, height = 1000, 1000
size = (width, height)
background = (255, 0, 0)
cell_color = (210, 168, 255)
block = 25
velocidad = 30

pygame.display.set_caption("Game Of Life")
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

grid = grid.Grid(width, height, block)
background_surface = pygame.Surface(size)
background_surface.fill(background)
grid.init(surface=background_surface)

run = True
pausa = False
while run:
    clock.tick(velocidad)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                grid.init(surface=background_surface)
            if event.key == pygame.K_SPACE:
                if pausa:
                    pausa = False
                else:
                    pausa = True
            if event.key == pygame.K_UP:
                print("aumentar velocidad en 1: ", velocidad)
                velocidad += 1
            if event.key == pygame.K_DOWN:
                print("disminuir velocidad en 1: ", velocidad)
                velocidad -= 1
            if event.key == pygame.K_LEFT:
                print("disminuir velocidad en 10: ", velocidad)
                velocidad -= 10
            if event.key == pygame.K_RIGHT:
                print("aumentar velocidad en 10: ", velocidad)
                velocidad += 10
            if event.key == pygame.K_ESCAPE:
                run = False
        if velocidad > 60:
            velocidad = 60
        elif velocidad < 1:
            velocidad = 1
    if not pausa:
        grid.turno(surface=background_surface, color=cell_color)
        screen.blit(background_surface, (0, 0))
        pygame.display.update()

pygame.quit()