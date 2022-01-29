import random
import time

note = input("note ( type 0 to read notes ) : ") + ","
if note == "0,":
    noteOpenEarly = open("note.txt", "r")
    lines = noteOpenEarly.readlines()
   
    for line in lines:
     print(line, end="")
  # noteOpenEarly.close
    quit()
if note != "0,":
    
   
    noteFile  = open("note.txt", "r+")
    if noteFile == "":
        writeNote = noteFile.write(note)
        quit()
    for line in noteFile:
        print(line, end="")
        writeNote = noteFile.write(note)
        
    quit()

    print("read all notes : //1")
    readLines = input(": ")
    if readLines == "//1":
        lines = noteFile.readlines()
        print(lines)
