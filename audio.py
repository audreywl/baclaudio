"""This is the development file for processing and playing back the audio. It is called from the visualization file using the current time stamp, and provides a value for bpm, mood (key), and where the timestamp is in relation to the beats."""
import alsaaudio
import audioop
import wave
import time
import numpy
import pygame.mixer
import librosa
import matplotlib

class Channel(object):
	"""This is the class that controls the format for visualizer inputs"""
	def __init__(self,channel_type,first_value,time_start=None):
		"""Intializes the channel class. If time_start=None, the time starts at 00:00:00"""
		self.channel_type=channel_type
		self.events={}
		if time_start==None:
			blank_time=(0,0,0,0,0,0,0,0,0)
			time_start=time.struct_time(blank_time)
		elif type(time_start)!=time.struct_time:
			raise TypeError('Must start with a time object')
		self.events[time_start]=first_value
		self.previous_value=first_value
	def __str__(self):
		return self.channel_type
	def update(self, time, new_value):
		self.events[time]=new_value
		previous_value=new_value

#Beat tracking example from librosa
# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y,sr)

print 'Estimated tempo: {:.2f} beats per minute'.format(tempo)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr)

print 'Saving output to beat_times.csv'
librosa.output.times_csv('beat_times.csv', beat_times)


bloop_channel=Channel('bloops',3)
print bloop_channel
print bloop_channel.events

# pygame.init()
# pygame.display.set_mode((200,100))
# pygame.mixer.music.load('Bad_Reputation.mp3')
# pygame.mixer.music.play(0)
# pygame.mixer.music.set_volume(0.5)
# clock = pygame.time.Clock()
# clock.tick(10)
# while pygame.mixer.music.get_busy():
# 	pygame.event.poll()
# 	clock.tick(10)
