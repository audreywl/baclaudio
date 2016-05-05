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
import Image
import cStringIO
from pprint import pprint

class Channel(object):
	"""This is the class that controls the format for visualizer inputs"""
	def __init__(self,channel_type,first_value=None,time_start=None):
		"""Intializes the channel class. If time_start=None, the time starts at 00:00:00"""
		self.channel_type=channel_type
		self.events={}
		if first_value != None:
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
	def __init__(self, filename, lyric_file, name='Untitled Song', artist="Unknown Artist"):
		self.filename=filename
		self.name=name
		self.waveform, self.sample_rate = librosa.load(self.filename)
		self.artist = artist
		self.lyric_file = lyric_file

	def __str__(self):
		return self.name

	def get_album_art(self):
		"""gets album art and saves it. the filename is located at self.art_filename"""
		api_key = '4b5d51107ac168e9406935bbbcadf721'
		url = 'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={}&artist={}&track={}&format=json'
		url = url.format(api_key,self.artist,self.name)
		api_location = urllib2.urlopen(url)
		response_text = api_location.read()
		response_data = json.loads(response_text)
		track_dictionary = response_data['track']
		album_dictionary = track_dictionary['album']
		image_list = album_dictionary['image']
		large_image_dictionary = image_list[3]
		image_url = large_image_dictionary['#text']
		image_location=urllib2.urlopen(image_url)
		image_data = image_location.read()
		image = Image.open(cStringIO.StringIO(image_data))
		self.image_filename = self.name.replace(' ','_') + '_'+self.artist.replace(' ','_') + '.png'
		image.save(self.image_filename)

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

	# def chord_analysis(self):
	#     """runs the analysis on the song to determine when the chords are major and minor"""
	#     self.harmonic_waveform = librosa.effects.harmonic(self.waveform)
	#     self.tonnetz = librosa.feature.tonnetz(self.harmonic_waveform,self.sample_rate)
	#     numpy.delete(self.tonnetz, [0,1,3,5], 1)
	#     #after this step, it's just a column vector with 0s for frames with minor and 1 for major
	#     major_frames = numpy.argmax(self.tonnetz, 0)
	#     frames = [i for i in range(len(major_frames))]
	#     self.frame_times = librosa.frames_to_time(frames, self.sample_rate)
	#     self.chord_channel=Channel('Chords: Major or Minor','Major')
	#     for i in frames:
	#         #rounds time to 1/10 of a second
	#         second = self.frame_times[i]
	#         second = round(second, 1)
	#         # next_second = second + .1
	#         time=datetime.timedelta(0,second)
	#         #saves beat in channel
	#         self.chord_channel.update(time, major_frames[i])
	#         #self.beat_channel.update(next_time, False)

	def chord_analysis(self):
		"""runs the analysis on the song to determine what the chord is"""
		self.harmonic_waveform = librosa.effects.harmonic(self.waveform)
		self.chroma = librosa.feature.chroma_cqt(self.harmonic_waveform,self.sample_rate)
		major_frames = numpy.argmax(self.chroma, 0)
		frames = [i for i in range(len(major_frames))] #LOOK AT THAT LIST COMPREHENSION
		major_frames = [major_frames[i] for i in range(len(major_frames))] #AND THAT ONE
		keys = [major_frames.count(i) for i in range(0,12)]
		sort_keys = sorted(keys, reverse = True)
		self.key_mode = keys.index(sort_keys[0])
		self.frame_times = librosa.frames_to_time(frames, self.sample_rate)
		self.chord_channel=Channel('Chords: C-B')
		for i in frames:
			#rounds time to 1/10 of a second
			second = self.frame_times[i]
			second = round(second, 1)
			time=datetime.timedelta(0,second)
			#saves beat in channel
			self.chord_channel.update(time, major_frames[i])
			

	def lyric_lines(self, song, times):
		"""Takes the list created from the .txt song file and puts into Channel.
			NEEDS UPDATE: currently list OP, be smarter about breakdown to increase processing speed!"""
		if '[0' in song[0] and ']' in song[0]:
			times.append(song[0])
			self.lyric_lines(song[1:], times)
		else:
			line = ""
			for i in range(len(song)): #i is the index number of the current word/timestamp
				try:
					if '[' in song[i]:
						self.lyric_lines(song[i+1:], [song[i]])
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
				self.lyrics.update(line_time,line)

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
		self.lyrics = Channel("Lyrics", "start lyrics:")
		# Create readable file of lyrics (.LRC file saved as .txt)
		f= open(self.lyric_file, 'r')
		song= f.read()
		f.close

		# revise text formating to use a single .split() to get timestamp and line breakdown
		# will use % as split key
		song = song.replace(']', ']%')
		song = song.replace('\n', '')
		song = song.replace('\r', '%')
		# List of time stamp and lyric elements
		song = song.split('%')

		#Identify the first time element and start of song
		#this formatting is needed for self.lyric_lines function
		for i in range(len(song)):
			if '[0' in song[i] and ']' in song[i]:
				#the first time stamp of the first line; list type
				time_start = [song[i]]
				#the indexes after (post) the time_start index
				post_start_song = song[i+1:]
				break

		# print song, time_start
		#call lyric_line function (recursive) to obtain needed output format of song text
		self.lyric_lines(song, time_start)

		#create new attribute in Song to hold onto timestamp Keys
		self.line_time = self.lyrics.events.keys()

		# Create lyrics sentiment channel
		self.lyrics_sentiment = Channel("Lyrics Sentiment", "start:")
		url = "http://text-processing.com/api/sentiment/"
		
		#populate lyrics_sentiment Channel with respect to line_time
		for a_time in self.line_time:
			# print "timestamp={} text={}".format(a_time, self.lyrics.events[a_time])

			try:
				sentiment = urllib2.urlopen(url, "text={}".format(self.lyrics.events[a_time]))
				response_text = sentiment.read()
				response_data = json.loads(response_text)
				# pprint(response_data)

				# Pull out the probability dictionary
				probability_dict = response_data["probability"]
			 
				# Put the probability values into a list for use in Visualization
				probability_values = [probability_dict["pos"], probability_dict["neg"], probability_dict["neutral"]]
				# pprint(probability_values)

				# create a sentiment entry for the given time (time corresponds to line)
				self.lyrics_sentiment.update(a_time, probability_values)
			except urllib2.HTTPError:
				# this error will occur if empty text is sent to the api, which is a
				# common occurance of the first line due to filtering
				print "API error! (It's probably OK, check documentation for more info)"

if __name__ == '__main__':
	#loads the song and runs analysis
	bad_rep=Song('All_Star_Smash_Mouth.mp3','All_Star_Smash_Mouth.txt', 'All Star', 'Smash Mouth')
	bad_rep.get_album_art()
	bad_rep.beat_analysis()
	bad_rep.chord_analysis()
	bad_rep.lyric_sentiment()
	pprint(bad_rep.lyrics.events)
	#starts pygame
	pygame.init()
	pygame.display.set_mode((200,100))
	pygame.mixer.music.load('All_Star_Smash_Mouth.mp3')
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

		# #checks if the current time is a beat
		# if time_difference in bad_rep.beat_channel.events:
		#     print 'beat'
		bad_rep.chord_channel.events[time_difference]
		clock.tick(10)