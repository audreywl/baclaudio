#Technical Review 2 Reflection
####Becca Patterson, Audrey Lewis, Cecilia Diehl, Liz Sundsmo


##Beat Analysis  Feedback and Decision:

The beat analysis advice is less relevant with our current conception of the visualizer. We will look into potentially removing elements from the dictionary after we call them, which would fix the double-calling error the same way that traversing an ordered dictionary would.

##Visualization Advice Feedback and Decision: 

We asked for advice on how to make pygame pretty so that our visualizer can be less rudimentary.  There were mixed responses (most other teams have chosen to move away from pygame because of this problem).  Claire did say that simply adding a background could work wonders.  We specifically asked for feedback on the idea of using a fractal instead of our mashed-up polygons, and people seemed interested in the idea.  Claire suggested implementing a recursive function that could have the level depth specified by an input. It was also more generally suggested that our beat visualization pulse larger the gradually shrink. 

Since the technical review, we have started seriously exploring the use of fractals for our visualizer.  We have already found some code examples where people created fractal images in pygame, so we are working to understand how they are drawn.
    
Ideally, we would find a way to increase or decrease the number of levels of the fractal in response to the sentiments we are pulling out of the song.  Once we figure out how best to generate a fractal image, we will have a better idea of how feasible it is to have the fractal change in response to the sentiment.  In the event that we decide it is out of scope, we may still choose to draw a fractal and choose other elements of the image to vary (eg. have multiple colors, introduce simple shapes that move across the screen, etc.).

##Key Advice Feedback and Decision:

We may average the chords across measures, but due to the fact that we don’t even know how to detect measure or phrase bounds at this point, we doubt that will happen. The major/minor distinction we had been making is probably completely inaccurate anyway, so we wouldn’t gain a lot from averaging (even our averages would be incorrect). Instead, we plan to detect and yrepresent changes in chords.

##Storage Advice Feedback and Decision:

We are going to look into implementing a storage folder system that exists with the code files to store files and analyzed song data. Paul suggested that we use the standard protocols for creating a folder for new music and accessing it. There would be a little bit of backend work regarding creating new files in the proper manner and using the correct file types which we would include in the ReadMe.  Sam suggested that we look into using SH Utils, but we will likely forgo that in favor of standard protocols due to the time required to process the amount of documentation and implementation that goes with SH Utils.

In our discussion of this question we realized that our libraries can handle .wav or .mp3 and .lrc or .txt file types, so we are also looking at building type flexibility into our code.

##Review Process Reflection:

We didn’t practice what we were going to say for this Technical Review and we think it showed quite a bit in our presentation. While we were able to provide an accurate and appropriate contextual set up for the class, we ended up fumbling a little as we moved on to asking questions and attempting to get feedback. The first main pitfall we encountered was when we asked a very detailed code specific question. It was something that we were looking for help with but a better option might have been talking to a ninja or professor instead of expecting the class to be able to jump right into our code with enough understanding to give constructive advice. Unfortunately, we were also at a point in our project where the main thing we needed to do was code, resulting in the majority of our naturally surfacing questions being code-based. We weren’t at a point in our project where we had that many things we wanted feedback on which caused us to look for things to present that maybe we didn’t have to.  

Something that did go well was our more general question about visualization. By asking the class what kinds of things they would visually prefer we got a better idea of which portions of the visualization we should spend more or less time on.   
While we did get some reasonable and useful feedback to our main questions for our next presentation we would like to be more prepared on our side. 
