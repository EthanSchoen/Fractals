import pygame
import sys

def drawTri(screen, pointList):
    pygame.draw.lines(screen, (255,255,255), True, pointList, 1)

def drawTriFract(screen, tri, layers):
    layers -= 1

    pA = tri[0]
    pB = tri[1]
    pC = tri[2]

    mAB = [(pA[0] + pB[0])/2, (pA[1] + pB[1])/2]
    mBC = [(pC[0] + pB[0])/2, (pC[1] + pB[1])/2]
    mAC = [(pA[0] + pC[0])/2, (pA[1] + pC[1])/2]

    nTri = (mAB, mBC, mAC)
    drawTri(screen, nTri)

    if layers > 0:
        drawTriFract(screen, (pA, mAB, mAC), layers)
        drawTriFract(screen, (pB, mAB, mBC), layers)
        drawTriFract(screen, (pC, mBC, mAC), layers)

def main():
    windowWidth = 1200
    windowHeight = 600
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill((0,0,0))

    #Initialize Fractal
    triangle = ([250,574], [600,20], [950,574])
    pygame.draw.lines(screen, (255,255,255), True, triangle,3)
    triSide = 500
    i = 0
    maxV = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        if i < 7:
            i += 1
        else:
            maxV = True

        if not maxV:
            pygame.time.wait(1000)
            drawTriFract(screen, triangle, i)
            pygame.display.update()

        pygame.display.update()

if __name__ == "__main__":
        main()
