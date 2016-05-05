---
title: About Our Project
layout: template
filename: aboutourproject
--- 
# What is BACLaudio?
BACLaudio is an auditory and visual experience generator. Taking in a variety of songs (we've chosen to theme this iteration on the Shrek soundtrack), BACLaudio generates a visualization of the lyrical and instrumental sentiment. In the form of a series of dots and functions, the continuously running patterns depict the instrumental sentiment based on chords and beat. Meanwhile, the color of the dots is determined by the sentiment of the song lyrics as determined by language processing. 

## Why?
We decided to pursue this project because we had all fallen victim to rocking out to happy tunes, only to be struck by the later realization that the lyrics were really negative, changing our entire perception of the song.  We were curious about creating a visualizer that would allow us to see these discrepancies in mood.

## What are the Features?
To analyze the piece of music we look at the chords, bpm, and lyrics. To represent these three values, a dot is released on the beat. The color of this dot represents the lyric sentiment, red/orange if positive and blue if negative with a gradient between the two. If the lyrics are completely neutral the dot is colored grey. The dot follows a path across the screen representing the key of the song that the dot was released on. Since there are twelve possible chords there are twelve unique functions. Each dot and function is produced with a mirrored duplicate to improve visual appearance.  

The song itself is determined by the user. Our wrapper allows the user to determine what song they wish to analyze as long as they have access to the correct files. After the song is analyzed and played once it is pickled into a folder with the other necessary files and saved. This means that if the same song is played more than once the analysis does not need to occur again. 
