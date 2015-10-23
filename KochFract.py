import pygame
import sys
import math

def distance(p1, p2):
    return math.sqrt( ((p1[0] + p2[0]) ** 2) + ((p1[1] + p2[1]) ** 2) )

def extendD(p, m, d):
    nP

def kochInteration(screen, line, layers):
    layers -= 1
    pA = line[0]
    pB = line[1]

    m = (pA[1] + pB[1])/(pA[0] - pB[0])
    if not pA[0] - pB[0] == 0:
        hypRatioX = distance(pA, pB)/(pA[0] - pB[0])
    else:
        hypRatioX = distance(pA, pB)
    if not pA[1] - pB[1] == 0:
        hypRatioY = distance(pA, pB)/(pA[1] - pB[1])
    else:
        hypRatioY = distance(pA, pB)
    thirdD = distance(pA, pB)/3
    sin60 = math.sin(-(22/7)/3)
    cos60 = math.cos(-(22/7)/3)

    line1 = (pA, [pA[0] + (pB[0] - pA[0])/3, pA[1] + (pB[1] - pA[1])/3])
    line4 = ([pA[0] + 2*(pB[0] - pA[0])/3, pA[1] + 2*(pB[1] - pA[1])/3], pB)

    about1 = [line4[0][0] - line1[1][0], line4[0][1] - line1[1][1]]
    nP = [about1[0] * cos60 - about1[1] * sin60, about1[0] * sin60 + about1[1] * cos60]
    nP[0] += line1[1][0]
    nP[1] += line1[1][1]

    line2 = (line1[1], nP)
    line3 = (nP, line4[0])

    pygame.draw.lines(screen, (0,0,0), False, (line1[1], line4[0]), 4)

    pygame.draw.lines(screen, (255, 255, 255), True, line2, 2)
    pygame.draw.lines(screen, (255, 255, 255), True, line3, 2)

    if layers > 0:
        kochInteration(screen, line1, layers)
        kochInteration(screen, line2, layers)
        kochInteration(screen, line3, layers)
        kochInteration(screen, line4, layers)

def main():
    windowWidth = 1200
    windowHeight = 600
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill((0,0,0))

    #Initialize Fractal
    triangle = ([400,424], [600,70], [800,424])
    pygame.draw.lines(screen, (255,255,255), True, triangle, 2)
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        if i < 5:
            i += 1
            pygame.display.update()
            pygame.time.wait(1000)
            kochInteration(screen, (triangle[0], triangle[1]), i)
            kochInteration(screen, (triangle[1], triangle[2]), i)
            kochInteration(screen, (triangle[2], triangle[0]), i)
        else:
            pygame.display.update()

if __name__ == "__main__":
        main()
