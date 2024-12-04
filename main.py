import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    updatable = pygame.sprite.Group() # Creates a group for updatable objects
    drawable = pygame.sprite.Group() # creates a group for drawable objects
    asteroids = pygame.sprite.Group() # creates a group for asteroids
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,) # 
    Asteroid.containers = (asteroids, updatable, drawable) #adds all asteroid objects to all groups
    Player.containers = (updatable, drawable) #adds the player object to updatable and drawable group
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(screen, timer, updatable, drawable, asteroids, shots)

def game_loop(screen, timer, updatable, drawable, asteroids, shots):
    dt = 0 # Delta time - Time since last frame in seconds
    for object in updatable:
        if isinstance(object, Player):
            player = object
    while True:
        dt = timer.tick(60) / 1000
        # Handle pygame events (like window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        pygame.Surface.fill(screen, "black") # Clear the screen before drawing new frame
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
                
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.kill()
            if asteroid.check_collisions(player):
                    print("Game Over")
                    return
           
        for object in drawable:
            object.draw(screen)
        pygame.display.flip() # Update the display with all changes
if __name__ == "__main__":
    main()
