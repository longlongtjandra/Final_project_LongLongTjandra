import pygame
from pygame.sprite import Sprite
import random
from ironman import*

#this class contain evry information about ultron
class Ultron(Sprite):
    def __init__(self,ai_settings,screen,Ironman):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #loading ultron image
        self.image_original = pygame.transform.scale(pygame.image.load("ultron.png"),(150,80))
        self.rect = self.image_original.get_rect()
        self.ironman = Ironman


      #to random from which side ultron will spawn
        side = random.randint(1,2)

        if side == 1:
            self.image = pygame.transform.scale(pygame.image.load("ultron.png"),(150,80))
            self.rect.left=0
        elif side == 2:
            self.image = pygame.transform.flip(self.image_original,True,False)
            self.rect.right=ai_settings.screen_width

        #random at ehich height ultron will spawn
        self.rect.y=random.randint(0,800)

        self.x= float(self.rect.x)
        self.y= float (self.rect.y)

 #drawing ultron into the screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    #making ultron movement towards player
    def update(self):
         if self.rect.x < self.ironman.rect.x:
             self.x += float(self.ai_settings.ultron_speed)
             self.rect.x=self.x


         if self.rect.x> self.ironman.rect.x:
             self.x -=float(self.ai_settings.ultron_speed)
             self.rect.x=self.x

         if self.rect.y<self.ironman.rect.y or self.rect.y>self.ironman.rect.y:
                 if self.rect.y< self.ironman.rect.y:
                     self.y+=float(self.ai_settings.ultron_speed)
                     self.rect.y=self.y

                 if self.rect.y>self.ironman.rect.y:
                     self.y -=float(self.ai_settings.ultron_speed)
                     self.rect.y = self.y


