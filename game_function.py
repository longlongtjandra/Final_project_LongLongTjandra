import sys

import pygame

from bullet import *
from ultron import *
from missile import*
from time import sleep


# this function is used to check whether play button has been pressed
def check_play_button(ai_settings,screen, stats,sb,play_button,ironman,ultrons,bullets,mouse_x,mouse_y,music):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)#comparing position of the mouse with the button
    # what happen when the start button is clicked
    if button_clicked and not stats.game_active:
        music.theme_song()
        ironman.stand=pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_ironmans()
        stats.game_active =True#changin the state of the game from non active to active


        ultrons.empty()
        bullets.empty()

        ironman.center_ironman()# position ironman in middle of the screen

#this fucntion is used to decide what happen when ironman has been hit by ultron
def ironman_hit(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles):
    #when the player still has life after collided with ultron this code will be run
    if stats.ironman_left>0:
        stats.ironman_left -=1#reducing the life player has after collision
        sb.prep_ironmans()
        ultrons.empty()#removing all ultron left on the screen
        missiles.empty()
        bullets.empty()#removing all bullet on the screen
        ironman.stand=pygame.transform.scale(pygame.image.load("flyingedit.png"),(100,100))
        ironman.center_ironman()#re centering position of ironman

        sleep(0.5)#stopping the program for a while to give player time to get ready

     #when player has no life after collision this code will be run
    else:
        ironman.stand=pygame.image.load("explosion.png")#load the image of explosion
        stats.game_active=False#setting the game status to non active
        pygame.mouse.set_visible(True)#make the mouse cursor to re appear

#this function is used to check whether ironman has been hit by ultron

def update_ultrons(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles):
    #this is to hcekc for iron man and ultron collision
    if pygame.sprite.spritecollideany(ironman,ultrons):
        ironman_hit(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles)
        print("ironman is dead")

def update_missiles_ironman_collison(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles):
    #this is to hcekc for iron man and ultron collision
    if pygame.sprite.spritecollideany(ironman,missiles):
        ironman_hit(ai_settings,screen,stats,sb,ironman,ultrons,bullets,missiles)
        print("ironman is dead")


def update_missile(ai_settings,screen,stats,sb,ironman,ultrons,missiles):
    #to delete missiles that have gone out of the screen
     for mis in missiles.copy():
            if mis.rect.bottom ==ai_settings.screen_height:
                missiles.remove(mis)




def update_bullets(ai_settings,screen,stats,sb,ironman,ultrons,bullets):
    #to delete bullets that have gone out of the screen
     for bullet in bullets.copy():
            if bullet.rect.left <=0 or bullet.rect.right >=ai_settings.screen_width:
                bullets.remove(bullet)


    # for collision between bullet and ultron
     collision=pygame.sprite.groupcollide(bullets,ultrons,True,True)
     if collision:
         #to control what happen when an ultron has been hit
         for ultrons in collision.values():
             stats.score += ai_settings.ultron_point* len(ultrons)
             stats.counter += 1
             sb.prep_score()
            #every few ultron shot down game will speed up the game
             if stats.counter > ai_settings.ultron_kill:
                 ai_settings.increase_speed()
                 stats.counter = 0

         check_high_score(stats,sb)

#to check whether the current score has passed the high score
#update the high score when current score exceed previous high score
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score#updating the high score
        sb.prep_high_score()

#this function check the key that user pressed and decide action that will be excecuted
def check_keydown(event,ai_settings,screen,ironman,bullets):
    if event.key == pygame.K_x:
        sys.exit()

    if event.key == pygame.K_RIGHT:
                ironman.moving_right= True

    if event.key == pygame.K_LEFT:
                ironman.moving_left= True

    if event.key == pygame.K_UP:
                ironman.moving_up= True

    if event.key == pygame.K_DOWN:
                ironman.moving_down= True

    elif event.key == pygame.K_e:

        if len(bullets)<ai_settings.bullets_allowed:
            ironman.stand= pygame.transform.scale(pygame.image.load("shoooting.png"),(120,120))
            ironman.look_left=False
            new_bullet = bullet_right (ai_settings, screen, ironman)
            bullets.add(new_bullet)#adding bullet into the group of bullets

    elif event.key == pygame.K_w:
        if len(bullets)<ai_settings.bullets_allowed:

            ironman.stand= pygame.transform.flip(pygame.transform.scale(pygame.image.load("shoooting.png"),(120,120)),True,False)
            ironman.look_left=True
            new_bullet = bullet_left (ai_settings, screen, ironman)
            bullets.add(new_bullet)




#to check whether player has released the key pressed
def check_keyup(event,ironman):
    if event.key == pygame.K_RIGHT:
                ironman.moving_right = False

    if event.key == pygame.K_LEFT:
                ironman.moving_left = False

    if event.key == pygame.K_UP:
                ironman.moving_up = False

    if event.key == pygame.K_DOWN:
                ironman.moving_down= False


#this function check for every events that the user do
def check_events(ai_settings,screen,stats,sb,play_button,ironman,ultrons,bullets,music):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ironman,ultrons,bullets,mouse_x,mouse_y,music)


        elif event.type == pygame.KEYDOWN:
            check_keydown(event,ai_settings,screen,ironman,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event,ironman)


#this function update the screen to the newest screen
def update_screen(ai_settings, screen,stats, sb,ironman,ultrons,background,bgrect,bullets,play_button,missiles):
#drawing the background into screen
    screen.blit(background,bgrect)
#drawing the bullet
    for bullet in bullets.sprites():
        bullet.blitme()
    #drawing ironman
    ironman.blitme()
#displaying the score
    sb.show_score()

#display play button when game state is not active
    if not stats.game_active:
        play_button.draw_button()
# drawing ultron every several frames
    elif pygame.time.get_ticks()%20==0:
        new_ultron= Ultron (ai_settings,screen,ironman)
        ultrons.add(new_ultron)
    elif  pygame.time.get_ticks()%50==0:
        new_missiles=Missile(ai_settings,screen,ironman)
        missiles.add(new_missiles)

    for ult in ultrons:
        ult.update()
        ult.blitme()
    for mis in missiles:
        mis.update()
        mis.blitme()



    pygame.display.flip()

