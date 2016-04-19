"""This is the development file for the lyrics processing. It finds the lyrics using a web API. It processes them chunk by chunk using the sentiment API. When called by the visualization, it provides chunk data including where each line of lyrics starts, the sentiment of each line in comparison to the previous ones, and the text itself."""
import time
import numpy
import librosa
import matplotlib
import datetime
from pygame import QUIT
# from audio.py import Channel
import urllib2, json
from pprint import pprint

class Channel(object):
    """This is the class that controls the format for visualizer inputs"""
    def __init__(self,channel_type,first_value,time_start=None):
        """Intializes the channel class. If time_start=None, the time starts at 00:00:00"""
        self.channel_type=channel_type
        self.events={}
        if time_start==None:
            time_start=datetime.timedelta()
        elif type(time_start)!=datetime.timedelta:
            raise TypeError('Must start with a time object')
        self.events[time_start]=first_value
        self.previous_value=first_value
    def __str__(self):
        return self.channel_type
    def update(self, time, new_value):
        self.events[time]=new_value
        if type(time)!=datetime.timedelta:
            raise TypeError('Time argument must be a timedelta object')
        previous_value=new_value


# Create lyrics channel
lyrics = Channel("Lyrics", "start lyrics:")

# Create readable file of lyrics (.LRC file saved as .txt)
f= open("bad_reputation.txt", 'r')
song= f.read()
f.close

# List of time stamp and lyric elements
song = song.replace(']', '] ')
song = song.split()

def lyric_lines(song, times):
    """Takes the list created from the .txt song file and puts into Channel.
        NEEDS UPDATE: currently list OP, be smarter about breakdown to increase processing speed!
    """
    if '[0' in song[0] and ']' in song[0]:
        times.append(song[0])
        lyric_lines(song[1:], times)
    else:
        line = ""
        for i in range(len(song)): #i is the index number of the current word/timestamp
            try:
                if '[' in song[i]:
                    lyric_lines(song[i+1:], [song[i]])
                    break
            except IndexError():
                break
            line+= " "+ song[i]
        for time in times: 
            if len(time) != 10:
                continue
            minutes = float(time[1:3]) #non inclusive of last index
            seconds = float(time[4:9])
            line_time = datetime.timedelta(00,seconds, 00, 00, 00, minutes)
            lyrics.update(line_time,line)
                
for i in range(len(song)):
    if '[0' in song[i] and ']' in song[i]:
        time_start = list(song[i])
        post_start_song = song[i+1:]
        break

lyric_lines(post_start_song, time_start)


# pprint(lyrics.events)

"""Save .LRC as .txt and sort by timestamp into channel."""

"""Use time to identify a stanza and send the whole stanza to the NLTK sentiment API.
    http://text-processing.com/docs/sentiment.html
    API Requirements: 1000 calls per day per IP
                      < 80,000 characters of text
    Responses:
        200 OK (JSON object):
             {
                "label": "pos",
                "probability": {
                    "pos": 0.85,
                    "neg": 0.15,
                    "neutral": 0.4
                }
             }
        400 Bad Request: Either no value for text provided or text exceeds character limit.
        503 Throttled: Daily request limit reached. Try https://market.mashape.com//japerk/text-processing/Pricing
"""
url = "http://text-processing.com/api/sentiment/"
sentiment = urllib2.urlopen(url, "text={}".format(lyrics.events[datetime.timedelta()]))

response_text = sentiment.read()
response_data = json.loads(response_text)
# pprint(response_data)

""" API returns a dictionary that contains two keys (label, probability). 
    The value of the probability key is another dictionary with the keys (pos, neg, neutral)
"""
# Pull out the probability dictionary
probability_dict = response_data["probability"]
# Put the probability values into a list for use in Visualization
probability_values = [probability_dict["pos"], probability_dict["neg"], probability_dict["neutral"]]

# Check output
pprint(probability_values)

"""how to make values useable-- return? channel?--> lyric_analysis function that creates channel in the Song class"""