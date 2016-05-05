---
title: How To Use
layout: template
filename: howtouse
--- 
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
