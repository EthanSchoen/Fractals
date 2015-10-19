import pygame
import sys

def main():
    windowWidth = 1200
    windowHeight = 600
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill((0,0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
        main()
