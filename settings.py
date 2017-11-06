import pygame
#this class contain every setting for the game
class Settings():
    def __init__(self):
        self.screen_width=1400
        self.screen_height = 800
        self.ironman_speed_factor = 2.5
        self.bullets_allowed = 5
        self.bullet_speed_factor=50
        self.ironman_limit = 3
        self.speedup_scale = 1.1
        self.summon_rate=20
        self.initialize_dynamic_settings()
        self.ultron_speed=5
        self.ultron_point=50
        self.score_scale=1.5
        self.ultron_kill=25
        self.ultron_kill_add=10
        self.missile_speed=5

#resetting all the speed when the game restart
    def initialize_dynamic_settings(self):
        self.ironman_speed_factor=5
        self.bullet_speed_factor=10
        self.ultron_speed=5
        self.ultron_point=50
        self.ultron_kill=25


#increasing the speed of the game when certain condition is fulfilled
    def increase_speed(self):
        self.ironman_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.ultron_speed *=self.speedup_scale
        self.ultron_point = int(self.ultron_point*self.score_scale)
        self.ultron_kill +=self.ultron_kill_add
        print(self.ultron_point)
        print(self.ironman_speed_factor,self.bullet_speed_factor,self.ultron_speed)


