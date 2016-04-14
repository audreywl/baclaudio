## BACLaudio
BACLaudio is an auditory and visual experience generator. Inputting songs from the Shrek sound track, BACLaudio generates a visualization of the lyirical and instrumental sentiment. In the form of a continuously changing shape the visualization depicts the instrumental sentiment on a scale of ________, ________, ________, and _______. Meanwhile, the color of the shape is determined by the sentiment of the song lyrics on a scale of _______, ________, _______, and _______.   
# Install
The main external library that we are using to do analysis is called _librosa_. _librosa_ has a ton of dependencies, which can be obtained by executing
```
$ sudo apt-get install python-numpy python-matplotlib python-scipy libpng12-dev libfreetype6-dev libav-tools libsamplerate0
```
at the command line. Then install _librosa_ with
```
$ sudo pip install librosa
```
It is highly likely that you will get the following error every time you run the code:
```
	/usr/local/lib/python2.7/dist-packages/matplotlib/font_manager.py:273: 
	UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
```
To fix this, in the python interpreter, run
```
	import matplotlib as mpl
        font_cache_path = mpl.get_cachedir() + '/fontList.cache'
        %rm $font_cache_path
```
The first time the code is run, the error may return, but it should not from then on.


# Code Example
	
# How to Use
	
# Contributers
Becca Patterson......

Audrey Lewis.........audreywl

Cecilia Diehl........diehlc1 

Liz Sundsmo..........

The creators or BACLaudio have made it open for use by the public. 

