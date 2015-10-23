import pygame
import sys
import math

def distance(p1, p2):
    return math.sqrt(

def kochInteration(screen, line, layers):
    layers -= 1

    line1 = 

    if layers > 0:
        kochInteration(screen, , layers)
        kochInteration(screen, , layers)
        kochInteration(screen, , layers)
        kochInteration(screen, , layers)

def main():
    windowWidth = 1200
    windowHeight = 600
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill((0,0,0))

    #Initialize Fractal
    triangle = ([250,574], [600,20], [950,574])
    pygame.draw.lines(screen, (255,255,255), True, triangle,3)
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if i < 7:
            i += 1
            pygame.time.wait(1000)
            pygame.display.update()
            kochInteration(screen, triangle[0], i)
            kochInteration(screen, triangle[1], i)
            kochInteration(screen, triangle[2], i)
        else:
            pygame.display.update()

if __name__ == "__main__":
        main()
