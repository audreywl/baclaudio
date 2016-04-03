#BACLaudio Framing - Technical Review 1
####Becca Patterson, Audrey Lewis, Cecilia Diehl, Liz Sundsmo
##Background and Context
The main idea for this project is a song/music sentiment detector with a large visual component. We would like to break a song into its musical and lyrical components to determine the sentiment of both sections (considering notes, tone, tempo, and words) and then have a visual representation for the different emotions. For example, the visual component of this project could be a colorful shape. The sentiment of the music (key, tempo) would determine the shape while the sentiment of the lyrics might be represented by different colors. The shape could also swell in size on each beat, and contract between them.
We would like our program to be at least partially real-time: we don’t want to have to pre-analyze each song before playing, but are willing to have the visualization start part of the way into the song (similar to how Shazam has a small loading time to find the song and start displaying lyrics). We could then store the song data to avoid loading it next time.
![Image of UML](https://raw.githubusercontent.com/audreywl/baclaudio/master/UML1.jpg)
##Agenda and Key Questions
**Intro (5 min) :** 
* Who are we and what are we working on
* Brief explanation of our computer architecture
  
**Discussion Time! (~20min) :**
We have two main questions that we would like to use to lead this discussion.
* Computer Architecture:
  * Is there anything that we have discussed that confuses you?
  * What do you consider as the good/bad parts?
  * How would you make it better?
* Syncing Text and Audio:
  * Currently we are using LRC files (Line up time steps with stanzas of lyrics) 
  * Do you have suggestions of other files or methods we could use?
  * We are trying to focus on ease of use and versatility.
* Other questions:
  * Just in case we get through the above topics really quickly we have some more questions for you! 
  * Sound sentiment 2X2 (figure in presentation)
  * Music sentiment knowledge/tips
