"""This is the main code. Run it to start the visualizer"""
import time
import numpy
import pygame.mixer
import librosa
import matplotlib
import datetime
from pygame import QUIT
import urllib2, json
from pprint import pprint
import Image
import audio
import squiggle

pygame.init()
#select screen size
size= (950, 650)
model= squiggle.Model(size[0], size[1])
view= squiggle.View(model, size)
running= True
#checks if the user closes the window   
while running:
    for event in pygame.event.get():
        if event.type== QUIT:
            running= False
    #if the window is open, do these things
    model.update()
    view.draw()
    time.sleep(.001)