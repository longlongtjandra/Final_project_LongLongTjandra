import pygame

#this class contain the stats for the game
class Gamestats():
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        self.high_score=0
#resetting the stats when the game ends
    def reset_stats(self):
        self.ironman_left = self.ai_settings.ironman_limit
        self.score = 0
        self.counter= 0

