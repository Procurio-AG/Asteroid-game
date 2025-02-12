import pygame
import circleshape as cs
from constants import *
from shot import *

#player class
class Player(cs.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #overriding draw
    def draw(self,screen):
        pygame.draw.polygon(
                surface = screen,
                color = "white",
                points = self.triangle(),
                width = 2)

    #player rotation
    def rotate(self,dt):
        #print(f"Current rotation: {self.rotation}")  #debug line
        self.rotation += PLAYER_TURN_SPEED*dt
        self.rotation = self.rotation%360

    #player movement
    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    #player shoots
    def shoot(self):
        shot = Shot(x = self.position[0], y = self.position[1],radius = SHOT_RADIUS)
        shot.velocity = PLAYER_SHOT_SPEED * (pygame.math.Vector2(0,1).rotate(self.rotation))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # left key
            #print("A key pressed")  #  debug line
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            # right key
            #print("D key pressed")  # Add this debug line
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            # up key
            #print("W key pressed")  #  debug line
            self.move(dt)
        
        if keys[pygame.K_s]:
            # down key
            #print("s key pressed")  # Add this debug line
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            # space key
            #print("space key pressed")  # Add this debug line
            self.shoot()
