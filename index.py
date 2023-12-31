import pygame
import os
from pygame.locals import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.png', [0, 0])

screen = pygame.display.set_mode([500, 500])

imp = pygame.image.load("indir.png").convert()
imp_rect = imp.get_rect()
imp_rect.center = (100, 100)

font = pygame.font.Font(None, 36)

# Initialize counters and timer
total_clicks = 0
current_clicks = 0
start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
game_duration = 60000  # 1 minute in milliseconds

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button
            total_clicks += 1
            current_clicks += 1

        if event.type == MOUSEBUTTONUP:
            current_clicks = 0

    # Check if the game time has exceeded 1 minute
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time >= game_duration:
        running = False

        # Display score and prompt to play again
        score_text = font.render(f"Your score: {total_clicks} clicks", True, (255, 255, 255))
        play_again_text = font.render("Do you want to play again? If so, please click", True, (255, 255, 255))

        screen.fill((255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(play_again_text, (10, 50))
        pygame.display.flip()

        # Wait for a new click to play again
        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_click = False

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    total_clicks = 0
                    start_time = pygame.time.get_ticks()
                    waiting_for_click = False

    screen.fill((255, 255, 255))
    screen.blit(BackGround.image, BackGround.rect)

    if current_clicks > 0:
        screen.blit(imp, [150, 125])

    # Render the counters
    total_counter_text = font.render(f"Total Clicks: {total_clicks}", True, (255, 255, 255))
    current_counter_text = font.render(f"Current Clicks: {current_clicks}", True, (255, 255, 255))

    # Render the timer
    remaining_time = max(0, (game_duration - elapsed_time) // 1000)  # Convert to seconds
    timer_text = font.render(f"Time Remaining: {remaining_time} seconds", True, (255, 255, 255))

    screen.blit(total_counter_text, (10, 10))
    screen.blit(current_counter_text, (10, 50))
    screen.blit(timer_text, (10, 90))

    pygame.display.flip()

pygame.quit()
