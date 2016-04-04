"""This is the development file for creating the visulization. It uses pygame 
to make a visual representation using 2 values - BPM and 'mood'(key). It also 
displys the current sentiment of lyrics, and the pyrics themselves. It calls 
the functions in audio.py and lyrics.py by providing the current time stamp.


NOTE FROM BECCA AND CECILIA ON 04-04-16:
	Not functional yet. Contains basic outline of the code.  We assumed a form for recieving data.  Need to confirm
	with team.

	For basic sentiment inputs, we plan to implement 
	(major, slow)= (lots of sides, small), (major, fast)= (lots of sides, big)
	(minor, slow)= (few sides, small), (minor fast)= (few sides, big)

"""



import pygame
import math
import time

class View(object):
	"""brings up the viuslizer in a pygame window"""
	def __init__(self, model, size):
		"""initialize the view with the specific model and screen dimensions"""
		self.model= model
		self.screen= pygame.display.set_mode(size)
	def draw(self):
		"""draws the game on thee screen"""	
		#background color
		self.screen.fill(pygame.Color('black'))
		#make sure to include the update screen

class Fake_Data(object):
	"""fake data lists to test visualizer with"""
	def __init__(self):
		#[(time, sentiment)]
		audio_sentiment= [(1, .7),(2, .8),(3, .6),(4, .5),(5, .7),(6, .9),(7, .8),
						(8, .6),(9, .5),(10, .6),(11, .7),(12, .7),(13, .8),
						(14, .7),(15, .7),(16, .6)]
		#[(time, [nuetral, polar, positive, negative])]	
		lyric_sentiment= [(3, [1,2,3,4]),(6, [5,6,7,8]),(9, [9,10,11,12]),
						(12, [13,14,15,16]),(15, [17,18,19,20]),(16, [21,22,23,24])]

class Blob(object):
	"""initializes the number and size of the sides. will be used in the model."""		
	def __init__(self, number, size):
		self.number= 12
		self.size= 40
		#eventully, size should be the 'diameter', and we will do math to find side
		#length to allow for nicer phases

class Model(object):
	"""stores our model state for the current time in playing music"""
	def __init__(self, width, height):
		#set up screen (make a variable later)
		self.width= 950
		self.height= 650
		self.
	
	def update(self):
		"update the model state based on the sentiments"
