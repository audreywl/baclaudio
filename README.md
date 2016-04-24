# BACLaudio
BACLaudio is an auditory and visual experience generator. Taking in a variety of songs (but mostly from the Shrek soundtrack), BACLaudio generates a visualization of the lyirical and instrumental sentiment. In the form of a continuously changing shape the visualization depicts the instrumental sentiment based on chords and key. Meanwhile, the color of the shape is determined by the sentiment of the song lyrics as determined by language processing. 
### Getting Started
The main external library that we are using to do analysis is called libROSA. libROSA has a ton of dependencies, which can be obtained by executing
```
$ sudo apt-get install python-numpy python-matplotlib python-scipy libpng12-dev libfreetype6-dev libav-tools libsamplerate0-dev
```
at the command line. Then install libROSA and one more dependency with
```
$ sudo pip install scikits.samplerate
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


### Usage
In its current iteration, BACLaudio pulses to the beat of Bad Reputation by Joan Jett. In the future, users will be able to add songs to BACLaudio by putting a .mp3 (music) and .lrc (lyrics) file in the code's directory, and it will prompt them for which to play.

When BACLaudio starts, it loads the song, opens a pygame window, and takes about 5 seconds to analyze the song before playing it and starting the visualizer. In future builds, this wait time may be decreased by processing and playing the song in parallel.
### Attribution
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

