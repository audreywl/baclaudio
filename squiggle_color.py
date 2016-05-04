"""BECCA WANTS TO MAKE A FRACTAL/PRETTY PICTURE/SQUIGGLY LINE IN PYGAME"""

import time
import numpy
import pygame.mixer
import matplotlib
import datetime
import math
from pygame import QUIT

sent = [1, 
        0.7, 
        0.5]

#set up the visualizer view
class Color_Gradient(object):
    def __init__(self,sent):
        percentPos = round(sent[0], 1)
        percentNeg = round(sent[1], 1)
        percentNeu = round(sent[2], 1)
        color_dict = {1:(231,3,3), 
                     0.9:(222,85,4), 
                     0.8:(213,160,5), 
                     0.7:(179,204,5),
                     0.6:(101,195,5),
                     0.5:(29,186,6),
                     0.4:(6,177,47),
                     0.3:(6,168,106),
                     0.2:(6,159,157),
                     0.1:(6,97,150),
                     0.0:(7,42,141)}

        if percentNeu >= .7:
            self.color = (0, 0, 0)
            print percentNeu
        elif percentPos in color_dict:
            self.color = color_dict[percentPos]
        else:
            self.color = (79, 244, 129)
        #self.color = (148*percentPos, 
        #              145*percentPos, 
        #              142*percentNeg)
        #self.color = (251, 242, 35) #YELLOW
        #self.color = (46, 49, 250) #BLUE

class View(object):
    """brings up the pygame window"""
    def __init__(self, model, size, Color_Gradient):
        """initialize the view with specific model and screen dimensions"""
        self.model= model
        self.screen= pygame.display.set_mode(size)
        self.Color_Gradient = color

    def draw(self):
        """draws the visualizer on the screen"""
        #background color
        self.screen.fill(pygame.Color('black'))

        #this is where we put the polygon(s)
        #cicle ([center], radius)
        pygame.draw.circle(self.screen, self.Color_Gradient.color, 
            (int(self.model.dot.center_x), int(self.model.dot.center_y)),
            self.model.DOT_RADIUS)

        #this method of drawing the function slows down the computation
        pygame.draw.lines(self.screen, self.Color_Gradient.color,
            False, self.model.line_points, 3)

        #refreshes the screen
        pygame.display.update()


class Dot(object):
    """represents the ball, which moves wrt time"""
    def __init__(self, center_x, center_y, radius):
        """initializing the circles that will be released on the beats"""
        # circle(Surface, color, pos, radius, width=0)
        self.center_x= center_x
        self.center_y= center_y
        self.radius= radius
    def update(self):
        """might be needed for moving the dots according to function"""
        pass

class Functions(object): 
    """holds the function options for the dot."""
    #this might eventually work like the channel class to create "unique" functions
    #for each dot.

    #actually have no idea why this exists
    pass
    # def __init__(self, i):
    #     #x is an input, y is the output
    #     self.i= self.i
    #     self.y= (math.sin(math.pi*self.x)+1)*300


class Model(object):
    """stores the current state for the current time in player music"""

    def __init__(self, width, height):
        """arranges the elements on the screen"""
        #set up screen (values in if __name__= 'main')
        self.width= width
        self.height= height
        #set constants
        self.DOT_RADIUS= 10
        #starts increment for dot's horizontal progression
        #not sure how to handle once there are multiple dots
        self.i= self.DOT_RADIUS

        #start list of points that will be used to draw function shape
        self.line_points= [(self.DOT_RADIUS/2, self.height/2)]

        #set release point of all the dots (for now just one)
        self.dot= Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS)

    def update(self):
        """updates the visualizer state"""
        #maybe move all of this into the Functions (or Functions_update?)class, use 
        #if statements for each dot to choose the function there, then here use 
        #these if statements to decide whether to update or stop moving

        if self.dot.center_x+self.DOT_RADIUS< self.width:
            #if the dot has not reached the end of the window, it keep moving on
            #it's function path
            self.dot.center_x= self.i
            self.dot.center_y= (math.sin(math.pi*self.dot.center_x*.005)+1)*300
            self.line_points.append((self.dot.center_x, self.dot.center_y))
            self.i+=.08 #what's a reasonable rate for the dot to move at? make sure it's slow enough

        else:   #elif int(self.dot.center_x-self.DOT_RADIUS)== self.width:
            #stop the dot from moving when it reached the end of the window
            #make the locations equal themselves so they are constant?
            self.dot.center_x= self.dot.center_x
            self.dot.center_y= self.dot.center_y


if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    pygame.init()
    #select screen size
    size= (950, 650)
    color = Color_Gradient(sent)

    model= Model(size[0], size[1])
    view= View(model, size, color)
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