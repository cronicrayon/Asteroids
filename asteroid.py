import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        uniform_angle = random.uniform(20,50)
        new_velocities = [self.velocity.rotate(uniform_angle),self.velocity.rotate(-uniform_angle)]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for velocity in new_velocities:
            scaled_velocity = velocity * 1.2 #changes velocity for split
            new_asteroid = Asteroid(self.position.x,self.position.y, new_radius) #constucts new asteroid
            new_asteroid.velocity = scaled_velocity



        pass
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2) # magic number is width
        

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
