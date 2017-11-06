import pygame

import sys
from settings import Settings
from ironman import Ironman
import game_function as gf
from pygame.sprite import Group
from ultron import Ultron
from gamestats import Gamestats
from button import Button
from scoreboard import Scoreboard
from music import Music


def main():

#starting the game and setting up variables for classes imported to main
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ironman=Ironman(ai_settings,screen)
    ultron=Ultron(ai_settings, screen,ironman)
    stats = Gamestats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

# play music as long as the game is being played
    music=Music("theme.mp3.mp3",7,0)

#setting up the group
    bullets=Group()
    ultrons=Group()
    missiles=Group()

#naming the game
    pygame.display.set_caption("ultron invasion")
    #displaying background image and drawing it on screen
    background=pygame.transform.scale(pygame.image.load("background.bmp"),(ai_settings.screen_width,ai_settings.screen_height))
    bgrect=background.get_rect()

    #drawing the start button for the game
    play_button = Button(ai_settings, screen, "suit-up")



#keeping the game looping and running using the while loop
    while True:


        gf.check_events(ai_settings,screen,stats,sb,play_button,ironman,ultrons,bullets,music)

        if stats.game_active:
            #update the screen
            ironman.update()
            bullets.update()
            gf.update_ultrons(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles)
            gf.update_missiles_ironman_collison(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles)
            gf.update_bullets(ai_settings,screen,stats,sb,ironman,ultrons,bullets)
            gf.update_missile(ai_settings,screen,stats,sb,ironman,ultrons,missiles)

        gf.update_screen(ai_settings, screen, stats,sb,ironman,ultrons,background,bgrect,bullets,play_button,missiles)


main()
