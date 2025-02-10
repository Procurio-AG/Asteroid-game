import pygame
import math

#base class for game objects

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        #later
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def is_collision(self,other):
        dist = self.position.distance_to(other.position)
        ch = self.radius + other.radius
        return (ch >= dist)

    def draw(self, screen):
        #override by subclass
        pass
    
    def update(self, dt):
        #override by subclass
        pass