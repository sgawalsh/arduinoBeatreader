import json

beatDic = {
"tn":"1100",
"sn":"100",
"en":"110000",
"qn":"111000000000",
"hn":"111111000000000000000000",
"fn":"111111111111000000000000000000000000000000000000",
"tr":"0000",
"sr":"000",
"er":"000000",
"qr":"000000000000",
"hr":"000000000000000000000000",
"fr":"000000000000000000000000000000000000000000000000",
}

class beat:
	def __init__(self,bpm,beatTracks):
		self.bpm = bpm
		self.beatTracks = beatTracks

	def toJson(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#with open(input("which file?\n> ")) as fh:
	#lines = list(fh)

with open("notes.txt") as f:
	lines = list(f)

outLines = []

for line in lines:
	thisLine = ''
	noteString = ''
	for note in line:
		if note == ' ' or note == '|':
			if noteString:
				print("File is not correctly formatted, please check that all note keys are complete.")
				quit()
			continue
		else:
			noteString += note
			if len(noteString) >= 2:
				if noteString in beatDic:
					thisLine += beatDic[noteString]
					noteString = ''
				else:
					print("'%s' is not a valid note, please check file." %noteString)
					quit()
	outLines.append(thisLine)

lineLen = len(outLines[0])

for i in range(1,len(outLines)):
	if len(outLines[i]) != lineLen:
		print("Line lengths are unequal, line 0 has length {0} and line {1} has length {2}".format(lineLen, i, len(outLines[i])))

bpm = int(input("bpm pls\n> "))
name = input("beat name pls\n> ")

with open("jsonBeats.txt", "r") as f:
	beatsDic = json.load(f)

while True:
	if name in beatsDic:
		name = input("Name taken, please choose another names for this beat.\n> ")
	else: break

beatsDic[name] = {"bpm": bpm, "trackNum": len(outLines), "tracks": outLines}

with open("jsonBeats.txt", "w") as f:
	json.dump(beatsDic, f)
