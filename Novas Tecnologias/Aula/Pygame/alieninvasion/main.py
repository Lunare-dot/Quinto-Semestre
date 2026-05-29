import pygame
from pygame.sprite import Group

from configs import Settings
from sprites import Ship
from events import gamefunctions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))
    bullets = Group()
    ship = Ship(screen)

    pygame.display.set_caption("PARE OS PORCOS!")

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()