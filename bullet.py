import pygame
from pygame.sprite import Sprite

#this class contain everything about the bullet that is shot to the right
class bullet_right(Sprite):
    def __init__ (self,ai_settings,screen,ironman):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = ai_settings

        self.image_original = pygame.image.load("fireball.png")
        self.image= pygame.transform.scale(self.image_original,(40,30))
        self.rect=self.image.get_rect()
        self.rect.x=ironman.rect.right
        self.rect.y=ironman.rect.centery-25
        self.x= float(self.rect.x)
#drawing the bullet into the screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)
#updating the position of the bullet
    def update(self):
        self.x += self.settings.bullet_speed_factor
        self.rect.x = self.x

#this class contain everything about the bullet that is hsot to the left
class bullet_left(Sprite):
    def __init__ (self,ai_settings,screen,ironman):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = ai_settings

        self.image_original = pygame.transform.flip(pygame.image.load("fireball.png"),True,False)
        self.image= pygame.transform.scale(self.image_original,(40,30))
        self.rect=self.image.get_rect()
        self.rect.x=ironman.rect.left
        self.rect.y=ironman.rect.centery-25
        self.x= float(self.rect.x)
#drawing the bullet into the screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)
#updating the position of the bullet
    def update(self):
        self.x -= self.settings.bullet_speed_factor
        self.rect.x = self.x

