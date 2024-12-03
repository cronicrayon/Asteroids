import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2) # magic number is width
        

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
