"""This is the development file for processing and playing back the audio. 
	It is called from the visualization file using the current time stamp, 
	and provides a value for bpm, mood (key), and where the timestamp is 
	in relation to the beats."""
import time
import numpy
import pygame.mixer
import librosa
import matplotlib
import datetime
from pygame import QUIT
import urllib2, json
from pprint import pprint

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
		self.line_time = self.lyrics.events.keys()

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
			next_second = second + .1
			time=datetime.timedelta(0,second)
			next_time= datetime.timedelta(0, next_second)
			#saves beat in channel
			self.beat_channel.update(time, True)
			self.beat_channel.update(next_time, False)

	def chord_analysis(self):
		"""runs the analysis on the song to determine when the chords are major and minor"""
		self.harmonic_waveform = librosa.effects.harmonic(self.waveform)
		self.tonnetz = librosa.feature.tonnetz(self.harmonic_waveform,self.sample_rate)
		numpy.delete(self.tonnetz, [0,1,3,5], 1)
		#after this step, it's just a column vector with 0s for frames with minor and 1 for major
		major_frames = numpy.argmax(self.tonnetz, 0)
		self.beat_times = librosa.frames_to_time(self.beat_frames, self.sample_rate)
		self.chord_channel=Channel('Chords: Major, Minor, Augmented, or Diminished','Major')
		for second in self.beat_times:
			#rounds time to 1/10 of a second
			second = round(second, 1)
			next_second = second + .1
			time=datetime.timedelta(0,second)
			next_time= datetime.timedelta(0, next_second)
			#saves beat in channel
			self.beat_channel.update(time, True)
			self.beat_channel.update(next_time, False)

	def lyric_lines(song, times):
		"""Takes the list created from the .txt song file and puts into Channel.
			NEEDS UPDATE: currently list OP, be smarter about breakdown to increase processing speed!"""

		if '[0' in song[0] and ']' in song[0]:
			times.append(song[0])
			lyric_lines(song[1:], times)
		else:
			line = ""
			for i in range(len(song)): #i is the index number of the current word/timestamp
				try:
					if '[' in song[i]:
						lyric_lines(song[i+1:], [song[i]])
						break
				except IndexError():
					break
				line+= " "+ song[i]
			for time in times: 
				if len(time) != 10:
					continue
				minutes = float(time[1:3]) #non inclusive of last index
				seconds = float(time[4:9])
				line_time = datetime.timedelta(00,seconds, 00, 00, 00, minutes)
				lyrics.update(line_time,line)

	def lyric_sentiment(self):
		"""Use time to identify a stanza and send the whole stanza to the NLTK sentiment API.
		http://text-processing.com/docs/sentiment.html
		API Requirements: 1000 calls per day per IP
						  < 80,000 characters of text
		Responses:
			200 OK (JSON object):
				 {
					"label": "pos",
					"probability": {
						"pos": 0.85,
						"neg": 0.15,
						"neutral": 0.4
					}
				 }
			400 Bad Request: Either no value for text provided or text exceeds character limit.
			503 Throttled: Daily request limit reached. Try https://market.mashape.com//japerk/text-processing/Pricing
	
		API returns a dictionary that contains two keys (label, probability). 
		The value of the probability key is another dictionary with the keys (pos, neg, neutral)"""

		# Create lyrics channel
		lyrics = Channel("Lyrics", "start lyrics:")
		# Create readable file of lyrics (.LRC file saved as .txt)
		f= open("bad_reputation.txt", 'r')
		song= f.read()
		f.close
		# List of time stamp and lyric elements
		song = song.replace(']', '] ')
		song = song.split()

		for i in range(len(song)):
			if '[0' in song[i] and ']' in song[i]:
				time_start = list(song[i])
				post_start_song = song[i+1:]
				break

		#call lyric_line function (recursive) to obtain needed output format of song text
		lyric_lines(song, time_start)

		#create new attribute in Song to hold onto timestamp Keys
		self.line_time = self.lyrics.events.keys()

		# Create lyrics sentiment channel
		self.lyrics_sentiment = Channel("Lyrics Sentiment", "start:")
		url = "http://text-processing.com/api/sentiment/"
		
		#populate lyrics_sentiment Channel with respect to line_time
		for a_time in self.line_time:
			sentiment = urllib2.urlopen(url, "text={}".format(lyrics.events[a_time]))

			response_text = sentiment.read()
			response_data = json.loads(response_text)
			# pprint(response_data)

			# Pull out the probability dictionary
			probability_dict = response_data["probability"]
		 
			# Put the probability values into a list for use in Visualization
			probability_values = [probability_dict["pos"], probability_dict["neg"], probability_dict["neutral"]]
			# pprint(probability_values)

			# create a sentiment entry for the given time (time corresponds to line)
			lyrics_sentiment.update(a_time, probability_values)


#loads the song and runs analysis
bad_rep=Song('Bad_Reputation.mp3','Bad Reputation')
bad_rep.beat_analysis()

bad_rep.lyric_sentiment()
print bad_rep.lyrics_sentiment

# #starts pygame
# pygame.init()
# pygame.display.set_mode((200,100))
# pygame.mixer.music.load('Bad_Reputation.mp3')
# #starts playing music and starts the clock
# pygame.mixer.music.play(0)
# start=datetime.datetime.now()
# pygame.mixer.music.set_volume(0.5)
# clock = pygame.time.Clock()
# clock.tick(10)
# while pygame.mixer.music.get_busy():
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#     #figures out how long it's been since the song started and rounds
#     time_difference=datetime.datetime.now()-start
#     rounded_time=round(time_difference.total_seconds(),1)
#     time_difference=datetime.timedelta(0,rounded_time)
#     #checks if the current time is a beat
#     if time_difference in bad_rep.beat_channel.events:
#         print 'beat'
#     clock.tick(10)
