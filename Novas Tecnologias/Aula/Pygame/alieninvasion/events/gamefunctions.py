import pygame
import sys

from pygame.sprite import Sprite
from configs.bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
             

def update_screen(ai_settings, screen, ship, bullets):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for bullets in bullets.sprites():
            bullets.draw_bullet()
        pygame.display.flip()