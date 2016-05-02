

# save file as "{}_channels".format(filename)

#Ask user what they would like to play
next_song = raw_input("Please enter the filename of the song you would like to play:")

#Check that folder exists in the location code is stored, if DNE then create it
bacl_dir = os.getcwd()
bacl_dir_storage = "{}/bacl_storage".format(bacl_dir)
os.chdir(bacl_dir_storage)

#If song exists, pull out the song specific analysis into visualizer useable names
try:
    song_file = next_song #mp3 in folder

    lyric_file = next_song.replace(".mp3", ".txt") #txt in folder
    lyric_file = next_song.replace(".wav", ".txt") 

    lyric_file = next_song.replace(".mp3", ".lrc") #multiple tries because multiple
    lyric_file = next_song.replace(".wav", ".lrc") #possible file types

    # beat_channel = 
    # lyric_sentiment = 

#If it doesn't exist ask  if the user would like to create an entry
else:
    create_song = raw_input("Song isn't in storage. Would you like to create an entry? y/n:")
    #If the user wants to create an entry asks for content
    if create_song == y:
        create_song_entry()

#Return to code directory (should be one file level up from inside storage folder)
os.chdir(bacl_dir)

def create_song_entry()
        song_audio = raw_input("Where is the song located? (.mp3 or .wav) (ex. user/file1/songname.filetype):")
        song_text = raw_input("Where is the lyric text located? (.lrc or .txt):"
#Attempts to find content. If success, moves into folder and proceeds. If fails throws error..
    try:
        find the song_file
        find the song_text

        if doesnt work notify user and break or throw error
        place files in folder to be used in visualization script
    open storage folder
    put things in folder