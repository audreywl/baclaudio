"""This is the development file for creating the visulization. It uses pygame 
to make a visual representation using 2 values - BPM and 'mood'(key). It also 
displys the current sentiment of lyrics, and the pyrics themselves. It calls 
the functions in audio.py and lyrics.py by providing the current time stamp.


NOTE FROM BECCA AND CECILIA ON 04-04-16:
    Opens a pygame window and draws a polygon. Contains basic outline of the code.  
    We assumed a form for recieving data.  Need to confirm with team.

    For basic sentiment inputs, we plan to implement 
    (major, slow)= (lots of sides, small), (major, fast)= (lots of sides, big)
    (minor, slow)= (few sides, small), (minor fast)= (few sides, big)

"""

import pygame
# import pygame.mixer
from pygame.locals import QUIT, KEYDOWN, KEYUP, MOUSEMOTION
import time
# from random import choice
import math

#set up the visualizer view
class View(object):
    """brings up the game in a pygame window"""
    def __init__(self, model, size):
        """initialize the view with specific model and screen dimensions"""
        self.model= model
        self.screen= pygame.display.set_mode(size)
    def draw(self):
        """draws the visualizer on the screen"""
        #background color
        self.screen.fill(pygame.Color('black'))
        #this is where we put the polygon  
        #rectangle
        # pygame.draw.polygon(self.screen, pygame.Color('white'), 
        #     [(300,200),(300,400),(600,400),(600,200)])  
        #star  
        pygame.draw.polygon(self.screen, pygame.Color('yellow'), 
            [(300,100),(600,100),(200,350), (700,350)])     #    (450,500),
        #refreshes the screen
        pygame.display.update()

# #obtain the data for visualization
# class Fake_Data(object):
#     """fake data lists to test visualizer with"""
#     def __init__(self):
#         #[(time, sentiment)]
#         audio_sentiment= [(1, .7),(2, .8),(3, .6),(4, .5),(5, .7),(6, .9),(7, .8),
#                         (8, .6),(9, .5),(10, .6),(11, .7),(12, .7),(13, .8),
#                         (14, .7),(15, .7),(16, .6)]
#         #[(time, [nuetral, polar, positive, negative])] 
#         lyric_sentiment= [(3, [1,2,3,4]),(6, [5,6,7,8]),(9, [9,10,11,12]),
#                         (12, [13,14,15,16]),(15, [17,18,19,20]),(16, [21,22,23,24])]

# #create the visual element pieces
# class Blob(object):
#     """initializes the number and size of the sides. will be used in the model."""      
#     def __init__(self, number, size):
#         self.number= 12
#         self.size= 40
#         #eventully, size should be the 'diameter', and we will do math to find side
#         #length to allow for nicer phases

#create the visualizer model
class Model(object):
    """stores the current state for the current time in player music"""
    def __init__(self, width, height):
        """arranges the elements on the screen"""
        #set up screen (values in if __name__= 'main')
        self.width= width
        self.height= height
        
    def update(self):
        """ Update the model state based on the sentiments"""

if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    # setup mixer to avoid sound lag
    # pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.init()
    #select screen size
    size= (950, 650)
    #(640,480) 
    #(950, 650)
     
    model= Model(size[0], size[1])
    view= View(model, size)
    running= True
    #checks if the user closes the window   
    while running:
        for event in pygame.event.get():
            if event.type== QUIT:
                running= False 
        model.update()
        view.draw()
        time.sleep(.001)          