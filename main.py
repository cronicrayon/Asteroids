import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(screen, timer, player)

def game_loop(screen, timer, player):
    dt = 0 # Delta time - Time since last frame in seconds
    while True:
        dt = timer.tick(60) / 1000
        # Handle pygame events (like window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        pygame.Surface.fill(screen, "black") # Clear the screen before drawing new frame
        player.update(dt)
        player.draw(screen)
        pygame.display.flip() # Update the display with all changes
if __name__ == "__main__":
    main()
