import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

# Player class inherits from Circleshape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(), 2) # magic number is line width

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # calulates the direction vector from the player's current rotation
        self.position += forward * PLAYER_SPEED * dt # Updates player position inline with direction vector
                                                     # uses delta time for smooth animation
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # updates self.rotation using delta time for smooth animation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            pass

        if keys[pygame.K_d]:
            self.rotate(dt)
            pass

        if keys[pygame.K_w]:
            self.move(dt)
            pass

        if keys[pygame.K_s]:
            self.move(-dt)
            pass