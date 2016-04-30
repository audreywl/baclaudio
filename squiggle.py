"""BECCA WANTS TO MAKE A FRACTAL/PRETTY PICTURE/SQUIGGLY LINE IN PYGAME"""

import time
import numpy
import pygame.mixer
import matplotlib
import datetime
import math
from pygame import QUIT

#set up the visualizer view
class View(object):
    """brings up the pygame window"""
    def __init__(self, model, size):
        """initialize the view with specific model and screen dimensions"""
        self.model= model
        self.screen= pygame.display.set_mode(size)

    def draw(self):
        """draws the visualizer on the screen"""
        #background color
        self.screen.fill(pygame.Color('black'))

        #what to draw    
        # print len(self.model.functions)
        # for function in self.model.functions:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, function, 3)

        # i=len(self.model.functions)
        # if i==1:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, self.model.functions[0], 3)
        # if i== 2:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, self.model.functions[0], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('blue'),
        #         False, self.model.functions[1], 3)
        # if i== 3:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, self.model.functions[0], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('blue'),
        #         False, self.model.functions[1], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('purple'),
        #         False, self.model.functions[2], 3) 
        # if i== 4:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, self.model.functions[0], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('blue'),
        #         False, self.model.functions[1], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('purple'),
        #         False, self.model.functions[2], 3)
        #     pygame.draw.lines(self.screen, pygame.Color('orange'),
        #         False, self.model.functions[3], 3)         

        for dot in self.model.dots:
            coordinate= (int(dot.center_x), int(dot.center_y))

            pygame.draw.circle(self.screen, pygame.Color('green'),
                coordinate, self.model.DOT_RADIUS)
            # pygame.draw.circle(self.screen, pygame.Color('green'), 
            #     (int(self.model.dot.center_x), int(self.model.dot.center_y)),
            #     self.model.DOT_RADIUS)

        #refreshes the screen
        pygame.display.update()


class Dot(object):
    """represents the ball, which moves wrt time"""
    def __init__(self, center_x, center_y, radius, line_point):
        """initializing the circles that will be released on the beats. needs xy locations, 
        and radius"""
        # inputs for dots
        self.center_x= center_x
        self.center_y= center_y
        self.radius= radius
        #start list of points that will be used to draw function shape
        #line point is already a list
        self.line_points= line_point
        #starts increment for dot's horizontal progression
        self.i= self.radius
        
    def update(self):
        """updates the increment for moving horizontally acrosee the screen"""
        if self.center_x+self.radius< 950:#self.width:
            #if the dot has not reached the end of the window, it keep moving on
            #it's function path
            self.center_x= self.i
            self.center_y= (math.sin(math.pi*self.center_x*.005)+1)*300
            #add current location to list for drawing
            self.line_points.append((self.center_x, self.center_y))
            self.i+=.08 #what's a reasonable rate for the dot to move at? make sure it's slow enough

        else:  
            #stop the dot from moving when it reaches the end of the window
            self.center_x= self.center_x
            self.center_y= self.center_y

class Functions(object): 
    """holds the function options for the dot."""
    #this might eventually work like the channel class to create "unique" functions
    #for each dot.

    #actually have no idea why this exists
    pass

class Model(object):
    """stores the current state for the current time in player music"""

    def __init__(self, width, height):
        """arranges the elements on the screen"""
        #set up screen (values in if __name__= 'main')
        self.width= width
        self.height= height
        #set constants
        self.DOT_RADIUS= 10
        #list of dots that will be drawn in view
        self.dots=[]
        #list that will hold lists of points to draw functions
        self.functions= []
        #starting point for all dots---- SETTING 2 BECUSE DRAWING LINES NEED 2+ POINTS
        self.starting_point= [(self.DOT_RADIUS/2, self.height/2), (self.DOT_RADIUS/2, self.height/2)]
        self.counter=0

    def update(self):
        """updates the visualizer state"""
        #initializes a dot. this is what we will alter for beats.      
        if self.counter==1 or self.counter==1000 or self.counter==2000 or self.counter==3000:
            #set release point for dot
            self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
                            self.starting_point))
            self.functions.append(self.starting_point)

        for dot in self.dots:
            dot.update()

        self.counter+=1    

if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    pygame.init()
    #select screen size
    size= (950, 650)

    model= Model(size[0], size[1])
    view= View(model, size)
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