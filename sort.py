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
		print("text", text.mode)
		if text.mode in usefulMode:
			modeList[text.mode].append(text)

	return modeList

def filterByTime(currMode):
	#for currMode in modeList:
	d = dict()
	for text in currMode:
		if text.getDay() not in d:
			d[text.getDay()] = [text]
		else:
			d[text.getDay()].append(text)

	return d

def filterBySortingBot(d, sortedTag):
	newDict = dict()
	print("original")
	print(d)
	for key in d:
		for text in d[key]:
			if text.sort in sortedTag:
				d[key].remove(text)
				
	print("newDict")
	print(d)
	return d
