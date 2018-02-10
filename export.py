import tkinter
import threading
import time
import user
from sort import *
import os 

# sorted tag we use for sortingbot
sortedTag = ["sleep, rest","greetings", "food, eat", "entertainment", "dirty langueas"]

# cited from 15112 website
def writeFile(path, contents):
	with open(path, "wt") as f:
		f.write(contents)

def format(d):
	result = ""
	for day in sorted(d.keys()):
		result += "\n\t%d-%d-%d" % (day[1], day[2], day[0]) + "\n"
		for text in d[day]:
			result += "\t- "+text.getActualTime()+"-"+text.user+": "+text.content+"\n"
	return result

def export(alltext):
	# write a file
	result = ""
	modeList = filterByMode(alltext, [0,1,2])
	print(modeList)
	for i in range(len(modeList)):
		d = filterByTime(modeList[i])
		newDict = filterBySortingBot(d, sortedTag)
		result += "%s" % user.mode[i]
		result += format(newDict)
		result += "\n"
	return result

def exportToTxt(result,path="Work.txt"):
	writeFile(path, result)

