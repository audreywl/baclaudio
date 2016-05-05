# BACLaudio
BACLaudio is an auditory and visual experience generator. Taking in a variety of songs (we've chosen to theme this iteration on the Shrek soundtrack), BACLaudio generates a visualization of the lyrical and instrumental sentiment. In the form of a series of dots and functions, the continuously running patterns depict the instrumental sentiment based on chords and beat. Meanwhile, the color of the dots is determined by the sentiment of the song lyrics as determined by language processing. 
### Getting Started

Of course, the first thing to do to get started running libROSA on your own is the clone the BACLaudio project at https://github.com/audreywl/baclaudio

The main external library that we are using to do analysis is called libROSA. libROSA has a ton of dependencies, which can be obtained by executing
```
$ sudo apt-get install python-numpy python-matplotlib python-scipy libpng12-dev libfreetype6-dev libav-tools libsamplerate0-dev
```
at the command line. Then install libROSA and one more dependency with
```
$ sudo pip install scikits.samplerate

$ sudo pip install librosa
```
To start the visualizer, simply run wrapper.py. 
```
$ python wrapper.py
```
It will prompt the user with what song they want to visualize. If you haven't downloaded a lyric and audio file for yourself, try Hallelujah by Rufus Wainwright, Bad Reputation by Joan Jett, or The Best Years Of Our Lives by Baha Men, which come with the repo.

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


### Usage
In this iteration when BACLaudio starts, it loads the song, opens a pygame window, and takes about 20 seconds to analyze the song before playing it and starting the visualizer. BACLaudio releases a dot when a beat occurs in the song. The dot follows the path related to the chord playing at the time of release, while the color of the dot is determined by the sentiment of the section of lyrics analyzed directly before the release. 

Using our wrapper, users are able to add songs to BACLaudio by finding .mp3 (music) and .lrc (lyrics) files for their desired songs (assuming they already exist on the users filesystem), which BACLaudio will relocate to its own directory. If users don't have their own mp3 and lrc files, they can play Bad Reputation by Joan Jett or All Star by Smash Mouth right out of the box.


### Attribution

Time   -   Reading, checking timestamps, timing

Numpy   -  Math

Librosa  - Obtaining beats, music chord changes

Datetime - Timestamping events for channel classes

Pygame.mixer - Use of music with Pygame

Urllib2, json   -   Interaction with Natural Language 
   		    Toolkit (NLTK) text sentiment API


#### Authors:
Becca Patterson......rebeccapatterson

Audrey Lewis.........audreywl

Cecilia Diehl........diehlc1 

Liz Sundsmo..........esundsmo

#### Thanks to:

The libROSA development team

Instructors and NINJAs

###License
The creators of BACLaudio have made it open for use by the public. 

