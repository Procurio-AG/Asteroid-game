#importing pygame open source library
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_1 = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player_1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        player_1.update(dt)

if __name__ == "__main__":
    main()
