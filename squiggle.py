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
        self.screen.fill(pygame.Color('white'))
        #draw function paths in the background
        for path in self.model.paths.paths:
            pygame.draw.lines(self.screen, pygame.Color('gray'), False, path,2)

        #draw dots
        for dot in self.model.dots:           
            coordinate= (int(dot.center_x), int(dot.center_y))

            pygame.draw.circle(self.screen, dot.color,
                coordinate, self.model.DOT_RADIUS)

        #refreshes the screen
        pygame.display.update()

class Dot(object):
    """represents the dot"""
    def __init__(self, center_x, center_y, radius, color, func, screen_width):
        """initializing the circles that will be released on the beats. needs xy locations, 
        and radius"""
        # inputs for dots
        self.center_x= center_x
        self.center_y= center_y
        self.radius= radius
        #sets the color for the dot
        self.color= color
        #starts increment for dot's horizontal progression
        self.i= self.radius 
        #the function path the dot will follow-- IS A LAMBDA FUNCTION
        self.func=func
        #so the dot knows when to stop moving
        self.screen_width= screen_width
        #controls the speed of the horizontal progression of the dot
        self.inc= 0.2
        
    def update(self):
        """updates the increment for moving horizontally acrosee the screen"""
        if self.center_x+self.radius< self.screen_width:#self.width:
            #if the dot has not reached the end of the window, it keep moving on
            #it's function path
            self.center_x= self.i
            self.center_y= self.func(self.center_x)            
            self.i+=self.inc

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
        color_dict = {1:(231,3,3), 
                     .9:(222,85,4), 
                     .8:(213,160,5), 
                     .7:(179,204,5),
                     .6:(101,195,5),
                     .5:(29,186,6),
                     .4:(6,177,47),
                     .3:(6,168,106),
                     .2:(6,159,157),
                     .1:(6,97,150),
                     0:(7,42,141)}
        
        # if round_sent in color_dict:
        #     self.color = color_dict[round_sent]
        # else:
        #     self.color = (251, 242, 35)
        if percentNeu >= .7:
            self.color = (128, 128, 128)
        elif percentPos in color_dict:
            self.color = color_dict[percentPos]
        else:
            self.color = (79, 244, 129)
        #self.color = (148*percentPos, 
        #              145*percentPos, 
        #              142*percentNeg)
        #self.color = (251, 242, 35) #YELLOW
        #self.color = (46, 49, 250) #BLUE      

class Functions(object): 
    """Holds all of the paths for the dots as lambda functions."""
    def __init__(self, key): #key is identified by number 0-11, the mirrored functions are 12-23
        self.key= key
        self.functions= [ lambda x: 320*math.sin((math.pi*x)/(950)) +325,
                          lambda x: 220*math.sin((math.pi*x)/(950)) +325,
                          lambda x: 160*math.sin((math.pi*x*3)/(950)) +325,
                          lambda x:  80*math.sin((math.pi*x*9)/(950)) +325,

                          lambda x:  40*math.sin((math.pi*x*3)/(950)) -(235*x)/950 +325,
                          lambda x:  40*math.sin((math.pi*x*3)/(950)) -(155*x)/950 +325,
                          lambda x:  40*math.sin((math.pi*x*3)/(950)) -(85*x)/950 +325,

                          lambda x:  -(275*x)/950 +325,
                          lambda x:  -(195*x)/950 +325,
                          lambda x:  -(115*x)/950 +325,
                          ###
                          lambda x: x+325,
                          lambda x: x+325,
                          ###
                          lambda x: -(320*math.sin((math.pi*x)/(950))) +325,
                          lambda x: -(220*math.sin((math.pi*x)/(950))) +325,
                          lambda x: -(160*math.sin((math.pi*x*3)/(950))) +325,
                          lambda x:  -(80*math.sin((math.pi*x*9)/(950))) +325,

                          lambda x:  -(40*math.sin((math.pi*x*3)/(950)) -(235*x)/950) +325,
                          lambda x:  -(40*math.sin((math.pi*x*3)/(950)) -(155*x)/950) +325,
                          lambda x:  -(40*math.sin((math.pi*x*3)/(950)) -(85*x)/950) +325,

                          lambda x:  (275*x)/950 +325,
                          lambda x:  (195*x)/950 +325,
                          lambda x:  (115*x)/950 +325,
                          ### 
                          lambda x: -x+325,
                          lambda x: -x+325
                          ###                       
                          ]

        self.func= self.functions[self.key]

#ADDING######################################################    
class Paths(object): 
    """for drawing the function paths in the background"""
    
    def __init__(self, screen_width):
        self.screen_width= screen_width
        self.i=0

        self.path0= []
        self.path1= []
        self.path2= []
        self.path3= []
        self.path4= []
        self.path5= []
        self.path6= []
        self.path7= []
        self.path8= []
        self.path9= []
        self.path10=[]
        self.path11=[]
        self.path12= []
        self.path13= []
        self.path14= []
        self.path15= []
        self.path16= []
        self.path17= []
        self.path18= []
        self.path19= []
        self.path20= []
        self.path21= []
        self.path22= []
        self.path23= []     

        #list of paths to be drawn
        self.paths= [self.path0, self.path1, self.path2, self.path3, self.path4, self.path5, 
                    self.path6, self.path7, self.path8, self.path9, self.path10, self.path11,
                    self.path12, self.path13, self.path14, self.path15, self.path16, self.path17, 
                    self.path18, self.path19, self.path20, self.path21, self.path22, self.path23 ]

        self.zero=       Functions(0)
        self.one=        Functions(1)
        self.two=        Functions(2)
        self.three=      Functions(3)
        self.four=       Functions(4)
        self.five=       Functions(5)
        self.six=        Functions(6)
        self.seven=      Functions(7)
        self.eight=      Functions(8)
        self.nine=       Functions(9)
        self.ten=        Functions(10)
        self.eleven=     Functions(11)
        self.twelve=     Functions(12)
        self.thirteen=   Functions(13)
        self.fourteen=   Functions(14)
        self.fifteen=    Functions(15)
        self.sixteen=    Functions(16)
        self.seventeen=  Functions(17)
        self.eighteen=   Functions(18)
        self.nineteen=   Functions(19) 
        self.twenty=     Functions(20)
        self.twentyone=  Functions(21)
        self.twentytwo=  Functions(22)
        self.twentythree=Functions(23)     

        while self.i <= self.screen_width:
            self.path0.append((self.i, self.zero.func(self.i)))
            self.path1.append((self.i, self.one.func(self.i)))
            self.path2.append((self.i, self.two.func(self.i)))
            self.path3.append((self.i, self.three.func(self.i)))
            self.path4.append((self.i, self.four.func(self.i)))
            self.path5.append((self.i, self.five.func(self.i)))
            self.path6.append((self.i, self.six.func(self.i)))
            self.path7.append((self.i, self.seven.func(self.i)))
            self.path8.append((self.i, self.eight.func(self.i)))
            self.path9.append((self.i, self.nine.func(self.i)))
            self.path10.append((self.i, self.ten.func(self.i)))
            self.path11.append((self.i, self.eleven.func(self.i)))
            self.path12.append((self.i, self.twelve.func(self.i)))
            self.path13.append((self.i, self.thirteen.func(self.i)))
            self.path14.append((self.i, self.fourteen.func(self.i)))
            self.path15.append((self.i, self.fifteen.func(self.i)))
            self.path16.append((self.i, self.sixteen.func(self.i)))
            self.path17.append((self.i, self.seventeen.func(self.i)))
            self.path18.append((self.i, self.eighteen.func(self.i)))
            self.path19.append((self.i, self.nineteen.func(self.i)))
            self.path20.append((self.i, self.twenty.func(self.i)))
            self.path21.append((self.i, self.twentyone.func(self.i)))
            self.path22.append((self.i, self.twentytwo.func(self.i)))
            self.path23.append((self.i, self.twentythree.func(self.i)))

            self.i+=10

#ADDING######################################################        


class Model(object):
    """stores the current state for the current time in player music"""
###REAL
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
        #set nuetral color for when there are no lyrics (see Color_Gradient for more info)
        self.sent= [0, 0, 0.7]
        #to be used for drawing the paths
        self.paths= Paths(self.width)
###REAL

# ###TESTING
#     def __init__(self, width, height):
#         """arranges the elements on the screen"""
#         #set up screen (values in if __name__= 'main')
#         self.width= width
#         self.height= height
#         #set constants
#         self.DOT_RADIUS= 10
#         #list of dots that will be drawn in view
#         self.dots=[]
#         #list that will hold lists of points to draw functions
# ###OUT        # self.rays= []
#         #starting point for all dots---- SETTING 2 BECUSE DRAWING LINES NEED 2+ POINTS
#         self.starting_point= [(self.DOT_RADIUS/2, self.height/2), (self.DOT_RADIUS/2, self.height/2)]
#         self.counter=0
#         #to be used for drawing the paths
#         self.paths= Paths(self.width)
# ###TESTING         

#TESTING CODE###############################################################

#     def update(self):
#         """updates the visualizer state"""    
#         #THIS WILL BE ALTERED FOR BEATS.      
#         if self.counter==1 or self.counter==1000 or self.counter==2000 or self.counter==3000:
#             #THIS WILL BE ALTERED FOR CURRENT SENTIMENT
#             if self.counter==1 or self.counter== 2000:
#                 sent = [0.3, 0.7, 0.6]
#             else:
#                 sent= [0.7,0.3,0.6]        
#             self.color= Color_Gradient(sent)

#             #THIS WILL BE ALTERED FOR CURRENT KEY
#             key=0
#             self.func= Functions(key)
#             self.func_mirror= Functions(key+12)

#             self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
#                             self.starting_point, self.color.color, self.func.func,
#                             self.func.inc, self.width))
#             self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
#                             self.starting_point, self.color.color, self.func_mirror.func,
#                             self.func_mirror.inc, self.width))

# ###OUT            self.rays.append(self.starting_point)

#         for dot in self.dots:
#             dot.update()

#         self.counter+=1 
#TESTING CODE###############################################################
#REAL CODE##############################################################   

    def update(self, time_difference):
        """updates the visualizer state"""    
        #initializes a dot when there is a beat

        #check if there are lyrics at this time, if there are, the color will
        #reflect them
        if time_difference in self.song.lyrics_sentiment.events:
            self.sent= self.song.lyrics_sentiment.events[time_difference]  
        self.color= Color_Gradient(self.sent)

        #release two dots (on mirrored functions) on each beat
        if time_difference in self.song.beat_channel.events: 

            self.key=self.song.chord_channel.events[time_difference]            
            self.func= Functions(self.key)
            self.func_mirror= Functions(self.key+12)

            #create a dot that corresponds to current sentiment
            self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
                            self.color.color, self.func.func, self.width))
            self.dots.append(Dot(self.DOT_RADIUS/2, self.height/2, self.DOT_RADIUS, 
                            self.color.color, self.func_mirror.func, self.width))
       
        for dot in self.dots:
            dot.update()
#REAL CODE##############################################################

#REAL CODE##############################################################
if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    pygame.init()
    #initialize the song, and run the analysis
    pygame.mixer.music.load('Bad_Reputation.mp3')
    song= audio.Song('Bad_Reputation.mp3', 'Bad Reputation')
    song.beat_analysis()
    song.lyric_sentiment()
    song.chord_analysis()

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
        time_difference=datetime.datetime.now()-start
        rounded_time=round(time_difference.total_seconds(),1)
        time_difference=datetime.timedelta(0,rounded_time)        
        #if the window is open, do these things
        model.update(time_difference)
        view.draw()
        time.sleep(.001)
#REAL CODE##############################################################

# #TESTING CODE###############################################################
# if __name__=='__main__':
#     """When the code is ran, the visualizer sets up as specified"""
#     pygame.init()
#     #select screen size
#     size= (950, 650)

#     model= Model(size[0], size[1])
#     view= View(model, size)
#     running= True
#     #checks if the user closes the window   
#     while running:
#         for event in pygame.event.get():
#             if event.type== QUIT:
#                 running= False
#         #if the window is open, do these things
#         model.update()
#         view.draw()
#         time.sleep(.001)
