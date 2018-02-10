import tkinter
import threading
import time
import user


# Get all text from another file
# Delete after
allText = []

# Return useful modes
def filterByMode(allText, usefulMode=[1,2]):
	# usefulMode is an int list
	modeList = [[] for i in range(6)]

	for text in allText:

		if text.mode in usefulMode:
			modeList[text.mode].append(text)

	return modeList

# Return dictionary by current day
def filterByTime(currMode):
	#for currMode in modeList:
	d = dict()
	for text in currMode:
		if text.getDay() not in d:
			d[text.getDay()] = [text]
		else:
			d[text.getDay()].append(text)

	return d

# Lose trash identified by sorting bot
def filterBySortingBot(d, sortedTag):
	newDict = dict()
	for key in d:
		for text in d[key]:
			if text.sort in sortedTag:
				d[key].remove(text)
				
	return d
