import pygame

#contain method to play music
class Music():
    def __init__(self,music,vol,str):
        self.music=music
        self.vol=vol
        self.str=str

    def theme_song(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)#this is used to load the music that you want to play
        pygame.mixer.music.set_volume(self.vol)#setting up the volume of the music
        pygame.mixer.music.play(loops=-1,start=self.str)#loop=-1 make sure that the music keep on looping after it ends
                                                        #start define at which second you want teh music to start from

