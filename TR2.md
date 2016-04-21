#BACLaudio Framing - Technical Review 2
####Becca Patterson, Audrey Lewis, Cecilia Diehl, Liz Sundsmo
##Background and Context
###General:
For this project we are creating song/music sentiment detector with a large visual component. We break the song into its instrumental and lyrical components to determine the sentiment of both sections (considering major/minor key, beat, and lyrics) and then have a visual representation for the different emotions. The visual component of this project is a colorful shape. The instrumental components (key, beat) determine the shape while the sentiment of the lyrics is represented by a changing color gradient. At this time the size of the shape pulses larger on each beat, and contracts between them.

Our program will pre-analyze the music in chunks, and create the visualization while the program analyzes the next part of the song. We are working on storing the song data during the first run to avoid loading the song / pinging the API the next time the same song is played. Our MVP would be a program that listens to a song and produces a sentiment-based visualization of some sort.

###Beat Analysis:
In order to visualize the beat we have the shape expand and then quickly contract. The event dictionary is created by making a key(value True) every time there is a beat and a key(value false) at the beat time plus a time delta of .1. Currently we tell the shape to change the radius when the event dictionary key matches the current run time. When the value is True the shape radius expands. Then when the value is False the shape contracts. For the most part this works, however during our debugging we discovered that the time delta being used is not the same as the time delta we set as .1.   

###Channel Class:
Our channel class is simply the class that controls the format of the data passed from the analysis functions to the visualizer. Each analysis that we do, to locate the beats, to split up the lyrics into lines and figure out where they are, and to locate the chords, produces a channel. Then, when we run the visualizer, it iterates through all the channels according to time. The main feature of a channel is an “events” dictionary, of which the keys are times and the values are what’s happening (beats are true/false, lyrics are the lyric themselves, etc).

###LibROSA Tonnetz:
To determine major/minor key, we use the libROSA tonnetz function, which returns the values of a “tonnetz” over time. A tonnetz is a representation of key that shows it along 6 axes corresponding to 3 intervals: fifth x, fifth y, major 3rd x, major 3rd y, minor 3rd x, and minor 3rd y. We weigh the major and minor 3rd x axes against each other to determine the chord at a given time.

##Key Questions:
###Beat Analysis:
* Why isn’t the time increasing by 0.1?

###Pygame Visualization
* Currently our visualization is fairly rudimentary, how can we make it prettier/intriguing? We were thinking implementing the shape outlines as a changing fractal could be cool? Then as far as coloring the shape, does a color gradient from positive to negative that keeps account of the past sentiment sound appealing? Or would you rather see a color change every time the sentiment changes? 

###Key Analysis
* We are currently doing a chord analysis using the librosa tonnetz function. This is returning a major/minor response every time it thinks the chord changes, but doesn’t seem to be particularly accurate. We might be able to filter out erroneous chords by taking the average over each measure, but we don’t know if accuracy or a more dynamic visualization is preferred. What do you think?
* Also, there is a small possibility that we are simply not interpreting the tonnetz correctly, which actually returns 6 values. If anyone is familiar with the tonnetz interpretation of key structure, we would appreciate some help.

##Agenda
###Intro(5 min):
Who are we and what are we working on
Brief explanation of code’s current state

###Discussion Time!(20 min):
We have three main questions that we would like to cover in this review
1. Beat Analysis
2. Pygame Visualization
3. Key Analysis 

If there is time at the end we will talk a bit about storing channel data and accessing it easily later to increase code flexibility. We want to group and store a song’s .mp3 file, .txt or .lrc file, and the song attributes and channels created in the first analysis of the song.
