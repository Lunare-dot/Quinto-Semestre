import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets\Corinthians_simbolo.png")
        self.image_size = (60, 60)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1