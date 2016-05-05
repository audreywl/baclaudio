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
	"""Takes a user inputed path and checks if it's valid. If not, it calls itself again."""
	path = raw_input('Please enter the path the files. For example "/home/audrey/Music/"')
	if not os.path.isdir(path):
		print 'Please enter the name of a valid path'
		path = find_new_path()
	return path

def find_directory():
	"""Prompts the user to identify the directory where the audio and lyric files are stored (first assumes the working directory is the one)"""
	yes = ['yes','y', 'ye', '']
	no = ['no','n']
	prompt = 'Where can I find the lrc and mp3 file for this song? In the folder below?(Y/n)' + '\n' +os.getcwd() + '\n'
	choice = raw_input(prompt).lower()
	if choice in yes:
		path = os.getcwd()
	elif choice in no:
		path = find_new_path()
	else:
   		print "Please respond with 'yes' or 'no'"
   		find_directory()
   	return path

def file_choice(display_files, type_of_file):
	"""Prompts the user to choose a file from a list. If they choose none of the above, it returns None."""
	prompt = 'Which of these files contains the {}? Please enter its number.'.format(type_of_file)
	try:
		choice = int(raw_input(prompt))
		if choice > len(display_files):
			raise ValueError
	except ValueError:
		print 'Please enter one of the file numbers'
		return file_choice(display_files, type_of_file)
	if choice == len(display_files):
		return None
	else:
		return choice-1
		

def find_files(path, track):
	"""Given a new directroy, prompts the user to identify the audio and lyric files in the folder, and returns them and their file types"""
	#Walks through the directory and uses the track name to try to find potential files related to the song
	identifiers = []
	for word in track.split():
		identifiers.append(word)
	for (dirpath, dirnames, filenames) in os.walk(path):
		file_list = filenames
		break
	potential_files = []
	for file_name in file_list:
		for word in identifiers:
			if word.lower() in file_name.lower() and file_name not in potential_files: #makes it not case-sensitive, and avoids adding the same file more than once.
				potential_files.append(file_name)
	if len(potential_files) == 0: #if none of the files look right, it assumes all of them are potentially right
		potential_files = file_list
	potential_files.append('None of the above')
	#display potential files for the user and ask them to choose
	display_files = [str(i+1)+': '+potential_files[i] for i in range(len(potential_files))]
	for file_name in display_files:
		print file_name
	choice = file_choice(display_files, 'song')
	#if they choose none of the above, give them the option to change directories
	if choice == None:
		path = find_directory()
		return find_files(path, track)
	#repeat for lyrics
	choice2 = file_choice(display_files, 'lyrics')
	if choice2 == None:
		path = find_directory()
		return find_files(path, track)
	#create full file paths
	song_path = path + '/' + potential_files[choice]
	lyric_path = path + '/' + potential_files[choice2]
	#figure out file type
	file_type_list1 = potential_files[choice].split('.')
	file_type_list2 = potential_files[choice2].split('.')
	return [song_path, lyric_path, file_type_list1[1], file_type_list2[1]]

def move_files(current_path, new_path, folder_name, track):
	"""moves an audio and a lyric file from a given location to a new one, names them appropriately, and preseves the file type"""
	[song_path, lyric_path, file_type_music, file_type_lyrics] = find_files(current_path, track)
	new_song_path = new_path + '/' + folder_name + '.' + file_type_music
	new_lyric_path = new_path + '/' + folder_name + '.'+ file_type_lyrics
	os.rename(song_path, new_song_path)
	os.rename(lyric_path, new_lyric_path)
	return [new_song_path, new_lyric_path]

if __name__ == '__main__':
	#prompt for song details
	track = raw_input('What is the name of the song?')
	artist = raw_input('What is the name of the artist?')
	folder_name = track.replace(' ','_') + '_'+artist.replace(' ','_')
	#check if song folder exists, and mp3 and txt files are in it
	if os.path.exists(folder_name) and os.path.isdir(folder_name):
		os.chdir(folder_name)
		path = os.getcwd()
		song_path = path + '/' + folder_name + '.mp3'
		lyric_path = path + '/' + folder_name + '.txt'
		if not os.path.exists(song_path) or os.path.exists(lyric_path):
			print "I'm having trouble finding the required files."
			new_path = os.getcwd()
			path = find_directory()
			[new_song_path, new_lyric_path] = move_files(path, new_path, folder_name, track)
	#if not, go through file-finding process
	else:
		os.makedirs(folder_name)
		os.chdir(folder_name)
		new_path = os.getcwd()
		path = find_directory()
		[new_song_path, new_lyric_path] = move_files(path, new_path, folder_name, track)
	#check if the song has been pickled
	pickle_name = folder_name+'.pkl'
	if not os.path.exists(pickle_name):
		song = audio.Song(new_song_path, new_lyric_path,track,artist) #create song object
		run_analyses(song)
		pkl_file = open(pickle_name, 'wb')
		pickle.dump(song, pkl_file)
		pkl_file.close()
	#if it has been pickled, load
	else:
		pkl_file = open(pickle_name, 'rb')
		song = pickle.load(pkl_file)
		pkl_file.close()
	#start pygame
	pygame.init()
	size= (950, 650)
	model= squiggle.Model(song, size[0], size[1])
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