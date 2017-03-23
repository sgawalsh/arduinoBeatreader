# arduinoBeatreader

The goal of this project was to provide a user with a simple means of writing a 4 track beat, saving that info, and playing the beat on an Arduino microcontroller.

First, the user writes their beat in the 'notes.txt' file using the keys found in the beatReader.py file. The user can then run the beatReader.py file which will convert the contents of "notes.txt" to an instance of the beat class, and save it with other beats in "jsonBeats.txt".

The user can then run the "jsonToSerial.py" file communicating with an arduino using the "beatReader.ino" file in order to play that beat on the microcontroller.
