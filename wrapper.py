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
import pickle
#import squiggle
import os

def run_analyses(song):
	"""processes the song - if there is chunk implementation, it would be here"""
	song.get_album_art()
	song.beat_analysis()
	song.chord_analysis()
	song.lyric_sentiment()

def find_new_path():
	path = raw_input('Please enter the path the files. For example "/home/audrey/Music/"')
	if not os.path.isdir(path):
		print 'Please enter the name of a valid path'
		path = find_new_path()
	return path

def find_directory():
	yes = ['yes','y', 'ye', '']
	no = ['no','n']
	choice = raw_input('Where can I find the lrc and mp3 file for this song? In this folder?(Y/n)').lower()
	if choice in yes:
		path = os.getcwd()
	elif choice in no:
		path = find_new_path()
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
			if word.lower() in file_name.lower() and file_name not in potential_files:
				potential_files.append(file_name)
	if len(potential_files) == 0:
		potential_files = file_list
	print potential_files
	choice = raw_input('Which of these files is the song? Please enter its index number, starting from 0. If the song is not in this directory, enter "none".')
	if choice == 'none':
		path = find_directory()
		return find_files(path, track)
	else:
		choice = int(choice)
		choice2 = int(raw_input('Which contains the lyrics?'))
	song_path = path + '/' + potential_files[choice]
	lyric_path = path + '/' + potential_files[choice2]
	file_type_list1 = potential_files[choice].split('.')
	file_type_list2 = potential_files[choice2].split('.')
	return [song_path, lyric_path, file_type_list1[1], file_type_list2[1]]


track = raw_input('What is the name of the song?')
artist = raw_input('What is the name of the artist?')
folder_name = track.replace(' ','_') + '_'+artist.replace(' ','_')
if os.path.exists(folder_name) and os.path.isdir(folder_name):
	os.chdir(folder_name)
	path = os.getcwd()
	new_song_path = path + '/' + folder_name + '.mp3'
	new_lyric_path = path + '/' + folder_name + '.txt'
	if not os.path.exists(new_song_path) or os.path.exists(new_lyric_path):
		print "I'm having trouble finding the required files."
		new_path = os.getcwd()
		[song_path, lyric_path, file_type_music, file_type_lyrics] = find_files(path, track)
		new_song_path = new_path + '/' + folder_name + '.' + file_type_music
		new_lyric_path = new_path + '/' + folder_name + '.'+ file_type_lyrics
		os.rename(song_path, new_song_path)
		os.rename(lyric_path, new_lyric_path)
else:
	os.makedirs(folder_name)
	os.chdir(folder_name)
	new_path = os.getcwd()
	path = find_directory()
	[song_path, lyric_path, file_type_music, file_type_lyrics] = find_files(path, track)
	new_song_path = new_path + '/' + folder_name + '.' + file_type_music
	new_lyric_path = new_path + '/' + folder_name + '.'+ file_type_lyrics
	os.rename(song_path, new_song_path)
	os.rename(lyric_path, new_lyric_path)


pickle_name = folder_name+'.pkl'
if not os.path.exists(pickle_name): #this is fake. it's a standin for if the song has already been done and pickled TODO: make this not fake
	song = audio.Song(new_song_path, new_lyric_path,track,artist)
	run_analyses(song)
	pkl_file = open(pickle_name, 'wb')
	pickle.dump(song, pkl_file)
	pkl_file.close()
else:
	pkl_file = open(pickle_name, 'rb')
	song = pickle.load(pkl_file)
	print song
	pkl_file.close()




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