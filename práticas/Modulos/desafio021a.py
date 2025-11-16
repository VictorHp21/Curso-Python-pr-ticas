import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("Disfigure - Blank _ Melodic Dubstep _ NCS - Copyright Free Music [p7ZsBPK656s].mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)