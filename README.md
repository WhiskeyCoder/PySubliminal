# PySubliminal
A set and forget player for subliminal audio playing that can be run from a RaspberryPi to run your loops, wrote for Subliminal Club content

## What is it 
A set and forget player for subliminal audio playing that can be run from a RaspberryPi to run your loops. Can be used for other types of Audio like maybe a music playlist for a shop or more.


## Why...
I am someone who was a spektic of Subliminals for a long time until a friend prompted me to try it for dealing with and over comming past traumas. Like others I have had some successes and brake throughs using them, but 1 Thing I noticed to get the full effect of these Subliminals you need to have the play on a shedual. for eample 2 loops of this and 2 loops of that. This can be tough to keep up with for many so I wrote this small script to keep track for me. The Idea is a set and forget raspberry pi or other device in your house hooked up to speakers in everyroom or your in house sounds systems, its up to you. 


## My Setup
my usage behind it is simple I have speakers in all the rooms I work in during the days, I have this script running on a RapsberyPi hooked up to the chain of speakers in the rooms i'll be in, and while I am working away without promtes it will play the subliminal stacks at the time I set. My program uses 3 different audio tracks over 5, for 2 loops a day, each audio track is 1 hour long.


## Requirements
- pip install playsound==1.2.2
- Replace the X with your audio file name no need for file extension
- change the timing in the while statement that best suits your requirements, can be overnight if wanted
- RaspberryPI or Always on system that can run python and has storage for your audio files
- Place the Audio tracks in the same folder as the script with same names used in the code
