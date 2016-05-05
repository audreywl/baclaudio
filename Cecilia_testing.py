"""This is the development file for processing and playing back the audio. It is called from the visualization file using the current time stamp, and provides a value for bpm, mood (key), and where the timestamp is in relation to the beats."""
import time
import numpy
import pygame.mixer
import librosa
import matplotlib
import datetime
import math
from pygame import QUIT

class Channel(object):
    """This is the class that controls the format for visualizer inputs"""
    def __init__(self,channel_type,first_value,time_start=None):
        """Intializes the channel class. If time_start=None, the time starts at 00:00:00"""
        self.channel_type=channel_type
        self.events={}
        if time_start==None:
            time_start=datetime.timedelta()
        elif type(time_start)!=datetime.timedelta:
            raise TypeError('Must start with a time object')
        self.events[time_start]=first_value
        self.previous_value=first_value
    def __str__(self):
        return self.channel_type
    def update(self, time, new_value):
        self.events[time]=new_value
        if type(time)!=datetime.timedelta:
            raise TypeError('Time argument must be a timedelta object')
        previous_value=new_value        

class Song(object):
    """Stores song metadata and analysis functions"""
    def __init__(self, filename, name='Untitled Song'):
        self.filename=filename
        self.name=name
        self.waveform, self.sample_rate = librosa.load(self.filename)

    def __str__(self):
        return self.name
    def beat_analysis(self):
        """runs the analysis on the song to determine where the beats are, and adds a beat channel"""
        self.tempo, self.beat_frames = librosa.beat.beat_track(self.waveform,self.sample_rate)
        self.beat_times = librosa.frames_to_time(self.beat_frames, self.sample_rate)
        self.beat_channel=Channel('Beat',False)
        for second in self.beat_times:
            #rounds time to 1/10 of a second
            second = round(second, 1)
            time=datetime.timedelta(0,second)
            #saves beat in channel
            self.beat_channel.update(time, True)

#set up the visualizer view
class View(object):
    """brings up the game in a pygame window"""
    def __init__(self, model, size):
        """initialize the view with specific model and screen dimensions"""
        self.model= model
        self.screen= pygame.display.set_mode(size)
        #specified the song to use in Song class
        self.bad_rep=Song('Bad_Reputation.mp3','Bad Reputation')
        #identifies when beats happen
        self.bad_rep.beat_analysis()
        #starts playing the music
        pygame.mixer.music.play(0)
        #starts the clock
        self.start=datetime.datetime.now()
        #keeps the clock in realtime
        self.clock = pygame.time.Clock()
        self.clock.tick(10)

    def beat_visual(self):
        """loads the song and runs analysis"""
        #figures out how long it's been since the song started and rounds the value
        time_difference=datetime.datetime.now()-self.start
        rounded_time=round(time_difference.total_seconds(),1)
        time_difference=datetime.timedelta(0,rounded_time)
        #checks if the current time is a beat- if yes, radius expands
        if time_difference in self.bad_rep.beat_channel.events:
            if self.bad_rep.beat_channel.events[time_difference]:
                self.model.update_expand()
                print "grow" 
            elif self.bad_rep.beat_channel.events[time_difference] == False:
                self.model.update_contract()
                print "smaller"



     #    if time_difference in self.bad_rep.lyric_sentiment_channel.event:
        #   current_sentiment = self.bad_rep.lyric_sentiment_channel.event
     #      positive= current_sentiment[0]
     #      negative= current_sentiment[1]
     #      neutral= current_sentiment[2]
     #      self.model.update_color(positive, negative, neutral)
        # else:
        #   print "no color change"
        self.clock.tick(10)


    def draw(self):
        """draws the visualizer on the screen"""
        #background color
        self.screen.fill(pygame.Color('black'))

        #this is where we put the polygon(s)
        #cicle ([center], radius)
        center_x= self.model.width/2
        center_y= self.model.height/2
        
        pygame.draw.circle(self.screen, pygame.Color('blue'),
            [center_x,center_y], self.model.r_cirle)    
        
        #square, starts bottom left, clockwise
        pygame.draw.polygon(self.screen, pygame.Color('green'),
            [(center_x-self.model.r_square*math.cos(math.pi/4), center_y+self.model.r_square*math.sin(math.pi/4)),
            (center_x-self.model.r_square*math.cos(math.pi/4), center_y-self.model.r_square*math.sin(math.pi/4)),
            (center_x+self.model.r_square*math.cos(math.pi/4), center_y-self.model.r_square*math.sin(math.pi/4)),
            (center_x+self.model.r_square*math.cos(math.pi/4), center_y+self.model.r_square*math.sin(math.pi/4))])
        
        #rhombus, starts bottom, clockwise
        pygame.draw.polygon(self.screen, pygame.Color('blue'),
            [(center_x, center_y+self.model.r_rhombus),(center_x-self.model.r_rhombus, center_y),
            (center_x, center_y-self.model.r_rhombus),(center_x+self.model.r_rhombus, center_y)])

        #refreshes the screen
        pygame.display.update()

#create the visualizer model
class Model(object):
    """stores the current state for the current time in player music"""

    def __init__(self, width, height):
        """arranges the elements on the screen"""
        #set up screen (values in if __name__= 'main')
        self.width= width
        self.height= height
        self.r_cirle= 100
        self.r_square= 100
        self.r_rhombus= 100
        self.r_octogon= 100
        self.beat_expansion= 50
        self.color= (75, 1, 130)

    # def update_color(self,pos,neg,neutral):
    #   """updates the rgb values based off of the lyric sentiment"""
    #   self.color= (75*pos, 1*neg, 130*nuetral)
    def update_expand(self):
        """updates model state"""
        #initializing shape radii
        #need to set an expansion variable for easier flexibility, use current+=expansion

        self.r_cirle+= self.beat_expansion
        self.r_square+= self.beat_expansion
        self.r_rhombus+= self.beat_expansion
        self.r_octogon+= self.beat_expansion


    def update_contract(self):
        #resets radii
        #need to use an expansion variable to return to previous radii size
        self.r_cirle-= self.beat_expansion
        self.r_square-= self.beat_expansion
        self.r_rhombus-= self.beat_expansion
        self.r_octogon-= self.beat_expansion


if __name__=='__main__':
    """When the code is ran, the visualizer sets up as specified"""
    # setup mixer to avoid sound lag
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
    
    pygame.init()
    #select screen size
    size= (950, 650)
    #set up the music
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('Bad_Reputation.mp3')
   
    model= Model(size[0], size[1])
    view= View(model, size)
    running= True
    #checks if the user closes the window   
    while running:
        for event in pygame.event.get():
            if event.type== QUIT:
                running= False
        #if the window is open, do these things
        view.draw()
        view.beat_visual()
        time.sleep(.001)
             