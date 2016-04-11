"""This is the development file for processing and playing back the audio. It is called from the visualization file using the current time stamp, and provides a value for bpm, mood (key), and where the timestamp is in relation to the beats."""
import time
import numpy
import pygame.mixer
import librosa
import matplotlib
import datetime
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
		"""doesn't store anything in non-beat time for now"""
		self.tempo, self.beat_frames = librosa.beat.beat_track(self.waveform,self.sample_rate)
		self.beat_times = librosa.frames_to_time(self.beat_frames, self.sample_rate)
		self.beat_channel=Channel('Beat',False)
		for second in self.beat_times:
			#rounds time to 1/10 of a second
			second = round(second, 1)
			time=datetime.timedelta(0,second)
			#saves beat in channel
			self.beat_channel.update(time, True)

#loads the song and runs analysis
bad_rep=Song('Bad_Reputation.mp3','Bad Reputation')
bad_rep.beat_analysis()
#starts pygame
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('Bad_Reputation.mp3')
#starts playing music and starts the clock
pygame.mixer.music.play(0)
start=datetime.datetime.now()
pygame.mixer.music.set_volume(0.5)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	#figures out how long it's been since the song started and rounds
	time_difference=datetime.datetime.now()-start
	rounded_time=round(time_difference.total_seconds(),1)
	time_difference=datetime.timedelta(0,rounded_time)
	#checks if the current time is a beat
	if time_difference in bad_rep.beat_channel.events:
		print 'beat'
	clock.tick(10)
