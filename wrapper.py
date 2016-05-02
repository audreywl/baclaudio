"""This is the main code. Run it to start the visualizer. It SOOOOO doesn't work right now"""
import time
import numpy
import pygame.mixer
import librosa
import matplotlib
import datetime
from pygame import QUIT
import urllib2, json
from pprint import pprint
import Image
import audio
#import squiggle
import os

def run_analyses(song):
	"""processes the song - if there is chunk implementation, it would be here"""
	song.get_album_art()
	song.beat_analysis()
	song.chord_analysis()
	song.lyric_sentiment()

def new_path():
	path = raw_input('Please enter the path the files. For example "/home/mymusic/song/"')
	if not os.path.isdir(path):
		print 'Please enter the name of a valid path'
		path = new_path()
	return path

def find_directory():
	yes = ['yes','y', 'ye', '']
	no = ['no','n']
	choice = raw_input('Where can I find the lrc and mp3 file for this song? In this folder?(Y/n)').lower()
	if choice in yes:
		path = os.getcwd()
	elif choice in no:
		path = new_path()
	else:
   		print "Please respond with 'yes' or 'no'"
   		find_directory()
   	return path

def find_files(path, track):
	identifiers = []
	for word in track.split():
		identifiers.append(word)
	for (dirpath, dirnames, filenames) in os.walk(path):
		file_list = filenames
		break
	potential_files = []
	for file_name in file_list:
		for word in identifiers:
			if word in file_name:
				potential_files.append(file_name)
	if len(potential_files) == 0:
		potential_files = file_list
	print potential_files
	choice = int(raw_input('Which of these files is the song? Please enter its index number, starting from 0.'))
	choice2 = int(raw_input('Which contains the lyrics?'))
	song_path = path + '/' + potential_files[choice]
	lyric_path = path + '/' + potential_files[choice2]
	return [song_path, lyric_path]

track = raw_input('What is the name of the song?')
artist = raw_input('What is the name of the artist?')
folder_name = track.replace(' ','_') + '_'+artist.replace(' ','_')
mp3_name = folder_name + '.mp3'
wav_name = folder_name + '.wav'
lrc_name = folder_name + '.lrc'
txt_name = folder_name + '.txt'
if os.path.exists(folder_name) and os.path.isdir(folder_name):
	os.chdir(folder_name)
else:
	path = find_directory()
	find_files(path, track)
#This is where Liz's code about the folders and where stuff is located goes, and it determines filename
#TODO: Add Liz's stuff
song = audio.Song(filename,track,artist)
if song.analyzed == False: #this is fake. it's a standin for if the song has already been done and pickled TODO: make this not fake
	run_analyses(song)


pygame.init()
#select screen size
size= (950, 650)
model= squiggle.Model(song, size[0], size[1]) #TODO: pass song to model
view= squiggle.View(model, size)
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