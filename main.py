#importing pygame open source library
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    #adding players and others to groups
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group,updatable_group,drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group,updatable_group,drawable_group)


    #adding instances of players
    player_1 = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)

    #adding instances of asteroidfield
    as_f = AsteroidField()
    
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for _ in drawable_group:
            _.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for _ in updatable_group:
            _.update(dt)
        for _ in asteroids_group:
            if _.is_collision(player_1):
                print("Game Over!")
                exit(1)

if __name__ == "__main__":
    main()
