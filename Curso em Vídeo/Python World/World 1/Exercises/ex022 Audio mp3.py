# Make a code that opens and reproduces an audio of a file Mp3

import pygame

pygame.init()
pygame.mixer.music.load(" ==> name of file <== ")
pygame.mixer.music.play()
pygame.mixer.wait()