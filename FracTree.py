import pygame
import math
import sys

def drawTreeFract(screen, branch, layers, ang):
    layers -= 1

    pA = branch[0]
    pB = branch[1]

    nP = [pB[0] + int(math.cos(math.radians(ang)) * layers * 10.0),  pB[1] + int(math.sin(math.radians(ang)) * layers * 10.0)]

    pygame.draw.lines(screen, (255,255,255), True, (pB, nP), 3)

    if layers > 0:
        drawTreeFract(screen, (pB, nP), layers, ang - 30)
        drawTreeFract(screen, (pB, nP), layers, ang + 15)

def main():
    windowWidth = 1200
    windowHeight = 600
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill((0,0,0))

    #Initialize Fractal
    trunk = ([800,600], [800,450])
    pygame.draw.lines(screen, (255,255,255), True, trunk, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawTreeFract(screen, trunk, 10, -90)
        pygame.display.update()

if __name__ == "__main__":
        main()
