#BACLaudio Reflection - Technical Review 1
####Becca Patterson, Audrey Lewis, Cecilia Diehl, Liz Sundsmo
##Key Questions Feedback:

**1. Feedback and decisions:**      
* _Computer Architecture:_
  * _Is there anything that we have discussed that confuses you?_
  * _What do you consider as the good/bad parts?_
  * _How would you make it better?_

  There was little confusion of our basic code architecture and nothing was identified by our peers as a particularly bad coding design move. It was suggested by Paul that we include more attributes in Song so that we have channels to track audio analysis, lyric analysis, tempo, etc. This would allow us to update the visualization portion more succinctly and clearly because we could pull an analyzed potion out of Song rather than pulling a piece of the audio out and then needing to do further analysis to tempo. 


* _Syncing Text and Audio:_
  * _Currently we are using LRC files (Line up time steps with stanzas of lyrics)_ 
  * _Do you have suggestions of other files or methods we could use?_
  * _We are trying to focus on ease of use and versatility._

  Our audience generally were as lost about this as we are - turns out it’s a really hard problem to solve. Suggestions included using analysis to find instrumental breaks and splitting the lyrics evenly among the rest, linking syllables with beats, and generating our own LRC files ahead of time. Paul expressed that we should just use LRC files and “hack it together” in the first iteration of our code, and then try to figure out better syncing later.


* _Other questions:_
  * _Just in case we get through the above topics really quickly we have some more questions for you!_ 
  * _Sound sentiment 2X2 (figure in presentation)_
  * _Music sentiment knowledge/tips_

  Most people agreed that the way we broke down the sentiments into four quadrants would work, but it was noted that we would be leaving out a wide range of emotions by simplifying it so much.  Some thought that we shouldn’t even label the emotions at all. Claire advised us to consider time signatures because time signatures and their implementation make a big difference to the sound and mood of a piece.  She also questioned how we plan to determine the key of a song, because we could run into some problems by going note by note because you could find chords that fit into multiple keys.  People were also curious about how we could validate our findings, and recommended taking a survey to check for people’s emotions while listening to a song and seeing if our findings match.

**2. Incorporation and Other Questions:**

  Most of the feedback we got during this review was really helpful and we plan on incorporating it in a few different ways. We will likely directly incorporate Paul’s feedback to break down the Song attributes even further so we can directly access the analysis for audio, lyrics, tempo/bpm, volume, key, etc with respect to time. Claire’s music theory feedback regarding different chords will likely be incorporated in our 2nd and 3rd iteration.   Her advice about time signatures effects on mood was interesting, but is more relevant to orchestral music, so it may not be implemented for this project.  As for our final validation, we really like the idea of using human response to verify the logic we use for our analysis. We will need to put a bit more thought into how we do this-- written recollection of emotions, videos of people’ faces, etc.



##Review process reflection:

Overall we think that the design review went really well, we were able to concisely summarize our overall project then move into more detailed discussion questions. We planned to guide the group through a discussion about what they know and think about music sentiment as well as their thoughts on our code architecture plan. One of the most important decisions we also wanted them to address was the synchronization of the music and lyrics. While we did get some great feedback one thing that took less time than we expected was the discussion about code architecture. Because no one spotted any particularly weak points in our current plan there didn’t need to be as much discussion as we had expected. This was both bad and good, good because it meant our current plan made sense (yay!) bad because we could have maybe asked some more pointed/specific questions to get even more feedback. Good thing we had included other a time buffer in the form of other questions that were less important to us but still relevant and good to receive feedback on!   
    
Next time we would like to have more specific/pointed questions that we could get specific responses and feedback on, we are thinking that these questions will arise as our project evolves and becomes more specific. We would also like to show some form of live demo of our visualization. The point of this would be to gain the responses of the viewer. A large portion of our project is that it is visually appealing to those who are interacting with it!     
