import pygame
from pygame.sprite import Sprite

#this class stores every method that the ironman has

class Ironman(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image= pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))

        self.stand = pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))
        self.rect = self.stand.get_rect()
        self.screen_rect=screen.get_rect()

        #starting position of iron man

        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.centery = float(self.screen_rect.centery)
        self.center = float(self.rect.centerx)
        #flagging the movement of ironman allowing smooth movement
        self.moving_right= False
        self.moving_left= False
        self.moving_up=False
        self.moving_down=False
        #deciding which side the ironman is looking
        self.look_left=False
        # self.right=pygame.transform.scale(pygame.image.load("flyingedit.png"),(150,150))
        # self.left=pygame.transform.flip(pygame.transform.scale(pygame.image.load("flyingedit.png"),(150,150)),True,False)

    # movement of ironman and which image need to be displayed when a button is pressed
    def update(self):
        if self.moving_right:
            self.look_left=False
            if self.rect.right<=self.ai_settings.screen_width:
                self.stand = pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))

                self.rect.centerx +=float(self.ai_settings.ironman_speed_factor)

        if self.moving_left:
            self.look_left=True
            if self.rect.left>=0:
                self.stand =pygame.transform.flip(pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100)),True,False)
                self.rect.centerx -=float(self.ai_settings.ironman_speed_factor)

        if self.moving_up:
            if self.rect.top >=0:
                if self.look_left==True:
                    self.stand =  pygame.transform.flip(pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100)),True,False)

                else:
                    self.stand = pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))

                self.rect.centery -=float(self.ai_settings.ironman_speed_factor)

        if self.moving_down:
            if self.rect.bottom < 800:
                if self.look_left==True:
                    self.stand =  pygame.transform.flip(pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100)),True,False)

                else:
                    self.stand = pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))

                #self.stand = pygame.transform.scale(pygame.image.load("flyingedit.png"),(120,120))

                self.rect.centery +=float(self.ai_settings.ironman_speed_factor)
            elif self.rect.bottom == self.ai_settings.screen_height:
                #landing image
                if self.look_left==True:
                    self.stand =  pygame.transform.flip(pygame.transform.scale(pygame.image.load("ironman.png"),(100,100)),True,False)

                else:
                    self.stand = pygame.transform.scale(pygame.image.load("ironman.png"),(100,100))

#this method draw ironman into the screen
    def blitme(self):
        self.screen.blit(self.stand, self.rect)
#this method is used to re position ironman when ultron hits ironman
    def center_ironman(self):
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.centery = float(self.screen_rect.centery)
