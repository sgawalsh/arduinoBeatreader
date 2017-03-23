import serial
import json
from time import sleep

with open("jsonBeats.txt", "r") as f: # select beat from 'jsonBeats.txt'
	beat = json.load(f)
	beatName = input("which beat?\n Beats: {0}\n> ".format(str(list(beat.keys()))))
	while True:
		if beatName in beat:
			beat = beat[beatName]
			break
		else:
			beatName = input("Name doesn't exist, please choose from existing names: \n {0}\n> ".format(str(beat.keys())))

del (beatName)

sleepyTime = 5 / beat["bpm"] # = 60 / (bpm * 12) - set sleep between each write cycle
beat = beat["tracks"]

ser = serial.Serial("/dev/ttyACM0", 9600) #open connection with arduino
ser.open()

print("waiting for arduino")
serin = ser.read()
print("go!")

for element in range(len(beat[0]) - 1):
	for track in beat:
		ser.write(str.encode(track[element]))
	sleep(sleepyTime)

print("done.")
