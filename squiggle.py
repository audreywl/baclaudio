"""BECCA WANTS TO MAKE A FRACTAL/PRETTY PICTURE/SQUIGGLY LINE IN PYGAME"""

import time
import numpy
import pygame.mixer
import matplotlib
import datetime
import math
from pygame import QUIT
import audio

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
        
#DEBUGGING THE FUNCTION LINES. FIRST IS CONSICE, SECOND IS FOR UNDERSTANDING THE PROBLEM.
        #what to draw    
        # print len(self.model.functions)
        # for function in self.model.functions:
        #     pygame.draw.lines(self.screen, pygame.Color('green'),
        #         False, function, 3)    

        for dot in self.model.dots:
            coordinate= (int(dot.center_x), int(dot.center_y))

            pygame.draw.circle(self.screen, dot.color,
                coordinate, self.model.DOT_RADIUS)

        #refreshes the screen
        pygame.display.update()


class Dot(object):
    """represents the dot"""
    def __init__(self, center_x, center_y, radius, line_point, color, func, inc):
        """initializing the circles that will be released on the beats. needs xy locations, 
        and radius"""
        # inputs for dots
        self.center_x= center_x
        self.center_y= center_y
        self.radius= radius
        #start list of points that will be used to draw function shape
        #line point is already a list
        self.line_points= line_point
        #sets the color for the dot
        self.color= color
        #starts increment for dot's horizontal progression
        self.i= self.radius 
        #the function path the dot will follow-- IS A LAMBDA FUNCTION
        self.func=func
        #controls the speed of the horizontal progression of the dot
        self.inc= inc
        
    def update(self):
        """updates the increment for moving horizontally acrosee the screen"""
        if self.center_x+self.radius< 950:#self.width:
            #if the dot has not reached the end of the window, it keep moving on
            #it's function path
            self.center_x= self.i
            self.center_y= self.func(self.center_x)            
            #add current location to list for drawing
            self.line_points.append((self.center_x, self.center_y))
            self.i+=self.inc #what's a reasonable rate for the dot to move at? make sure it's slow enough

        else:  
            #stop the dot from moving when it reaches the end of the window
            self.center_x= self.center_x
            self.center_y= self.center_y

class Color_Gradient(object):
    def __init__(self,sent):
        round_sent = round(sent[0], 1)
        percentPos = sent[0]
        percentNeg = sent[1]
        percentNeu = sent[2]
        color_dict = {1:(77, 138, 240), 
                     .9:(78, 182, 240), 
                     .8:(78, 226, 241), 
                     .7:(78, 242, 214),
                     .6:(79, 243, 172),
                     .5:(79, 244, 129),
                     .4:(79, 246, 86),
                     .3:(117, 247, 80),
                     .2:(162, 248, 80),
                     .1:(207, 249, 80),
                     0:(250, 248, 81)}
        
        if round_sent in color_dict:
            self.color = color_dict[round_sent]
        else:
            self.color = (251, 242, 35)
        #self.color = (148*percentPos, 
        #              145*percentPos, 
        #              142*percentNeg)
        #self.color = (251, 242, 35) #YELLOW
        #self.color = (46, 49, 250) #BLUE      

class Functions(object): 
    """Holds all of the paths for the dots as lambda functions."""
    def __init__(self, key): #key is identified by number 0-11
        self.key= key
        self.functions= [lambda x: (math.sin(math.pi*x/75) +1)*325,  
                         lambda x: (math.sin(math.pi*x*.005)+1)*300,
                         lambda x: (math.cos(math.pi*x/90) +3)*100,
                         lambda x: (math.cos(math.pi*x*.0011)+1)*300,
                         lambda x: (math.sin(math.pi*x/80) +1.5)*200,
                         lambda x: (math.sin(2*math.sin(2*math.sin(2*math.sin(x*0.02))))+1)*300,
                         lambda x: (50*math.sin(2*math.pi*x/300)+0.5*x),
                         lambda x: (-0.2*x +325),
                         lambda x: (50*math.sin(2*math.pi/50*x))+250*math.sin(math.pi/250*x)+325,
                         lambda x: -(50*math.sin(2*math.pi*x/300)+0.5*x)+650,
                         lambda x: -(math.sin(2*math.sin(2*math.sin(2*math.sin(x*0.02))))-1)*300,
                         lambda x: (0.2*x +325)]
        self.func= self.functions[self.key]

        #increments maps with functions, controls speeds
        self.increment= [0.08,
                        0.1, 
                        0.4, 
                        0.2, 
                        0.1, 
                        0.08, 
                        0.2, 
                        0.2,
                        0.08,
                        0.2,
                        0.08,
                        0.2 ]
        self.inc= self.increment[self.key]

class Model(object):
    """stores the current state for the current time in player music"""

    def __init__(self, width, height, song):
        """arranges the elements on the screen"""
        #set up screen (values in if __name__= 'main')
        self.width= width
        self.height= height
        #set song
        self.song= song
        #set constants
        self.DOT_RADIUS= 10
        #list of dots that will be drawn in view
        self.dots=[]
        #list that will hold lists of points to draw functions
        self.functions= []
        #starting point for all dots---- SETTING 2 BECUSE DRAWING LINES NEED 2+ POINTS
        self.starting_point= [(self.DOT_RADIUS/2, self.height/2), (self.DOT_RADIUS/2, self.height/2)]
###        # self.counter=0

    def update(self, time_difference):
        """updates the visualizer state"""
        #initializes a dot when there is a beat
###        #THIS WILL BE ALTERED FOR BEATS.
###        # if self.counter==1 or self.counter==1000 or self.counter==2000 or self.counter==3000:
            #THIS WILL BE ALTERED FOR CURRENT KEY
            # if self.counter==1:
            #     key=9
            # elif self.counter==2000:
            #     key=9   
            # else:
            #     key=9 
            #chooses the function path based on the current chord
        if time_difference in self.song.beat_channel.events:       
            self.key=self.song.chord_channel.events[time_difference]            
            self.func= Functions(self.key)

###            #THIS WILL BE ALTERED FOR CURRENT SENTIMENT
            # if self.counter==1 or self.counter== 2000:
            #     sent = [0.3, 0.7, 0.6]
            # else:
            #     sent= [0.7,0.3,0.6]

            #set nuetral color for when there are no lyrics
            self.sent= [0.5, 0.5, 0.5]
            #check if there are lyrics at this time, if there are, the color will
            #reflect them
            if time_difference in self.song.lyric_sentiment.events:
                self.sent= self.song.lyric_sentiment[time_difference]
            self.color= Color_Gradient(self.sent)

            #create a dot that corresponds to current sentiment
            self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
                            self.starting_point, self.color.color, self.func.func,
                            self.func.inc))
            self.functions.append(self.starting_point)

        for dot in self.dots:
            dot.update()

###        # self.counter+=1    

if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    pygame.init()
    #initialize the song, and run the analysis
    pygame.mixer.music.load('Bad_Reputation.mp3')
    song= audio.Song('Bad_Reputation.mp3', 'Bad Reputation')
    song.beat_analysis()
    song.lyric_sentiment()

    #select screen size
    size= (950, 650)
    
    model= Model(size[0], size[1], song)
    view= View(model, size)

    #start playing the music, start the clock
    pygame.mixer.music.play(0)
    start= datetime.datetime.now()
    pygame.mixer.music.set_volume(0.5)
    clock= pygame.time.Clock()
    clock.tick(10)

    running= True
    #checks if the user closes the window   
    while running:
        for event in pygame.event.get():
            if event.type== QUIT:
                running= False
        #determine how long it's been since the song started
        time_difference=datetime.datetime.now()-self.start
        rounded_time=round(time_difference.total_seconds(),1)
        time_difference=datetime.timedelta(0,rounded_time)        
        #if the window is open, do these things
        model.update(time_difference)
        view.draw()
        time.sleep(.001)