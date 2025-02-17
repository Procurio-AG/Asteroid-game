import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
                surface = screen,
                color = "white",
                center = self.position,
                radius = self.radius,
                width = 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,score):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            score+=1
            return score
        else:
            ang = random.uniform(20,50)
            r1 = self.velocity.rotate(ang) * 1.2
            r2 = self.velocity.rotate(-ang) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            as1 = Asteroid(self.position[0],self.position[1],new_radius)
            as1.velocity = r1
            as2 = Asteroid(self.position[0],self.position[1],new_radius)
            as2.velocity = r2
            return score
