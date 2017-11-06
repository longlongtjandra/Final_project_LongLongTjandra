import pygame
from pygame.sprite import Sprite
import random
from ironman import*

#class containing the method for missile and its behaviour
class Missile(Sprite):
    def __init__(self,ai_settings,screen,Ironman):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #loading ultron image
        self.image = pygame.transform.scale(pygame.image.load("missile.png"),(80,120))
        self.rect = self.image.get_rect()



#making the missiles to spawn in different position of coordinate x
        self.rect.x=random.randint(0,self.ai_settings.screen_width)
        self.rect.y=0

        self.x= float(self.rect.x)
        self.y= float (self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    #making missile move downward
    def update(self):
        self.y += float(self.ai_settings.missile_speed)
        self.rect.y = self.y



