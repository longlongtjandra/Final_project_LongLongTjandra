import pygame.font
from pygame.sprite import Group

from ironman import Ironman

#this class is used to make the scoreboard for the game
class Scoreboard():
    def __init__(self,ai_settings, screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_ironmans()


    #method used to make the score
    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)#give coma to the score
        self.score_image = self.font.render(score_str,True,self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top=20
    #method used to diplay teh score in the game
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ironmans.draw(self.screen)

    #method used to make the high score
    def prep_high_score(self):
        high_score= int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)#giving coma to high score
        self.high_score_image= self.font.render(high_score_str,True,self.text_color)

        self.high_score_rect= self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    #method used to show how many life the player has
    def prep_ironmans(self):
        self.ironmans = Group()
        for ironman_number in range(self.stats.ironman_left):
            ironman = Ironman(self.ai_settings,self.screen)
            ironman.rect.x=10 + ironman_number*ironman.rect.width
            ironman.rect.y=10
            self.ironmans.add(ironman)


