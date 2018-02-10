import tkinter
import threading
import time
from Sortingbot import *

mode = ["trash", "report", "note","","",""]
modeColor = ["orange", "pink", "purple","","",""]

# Max mode number = 3
def defineMode(name, color, index=3):
	if index == 6:
		print("index out of range!")
		return
	if (mode[index] == ""):
		mode[index] = name
		modeColor = color
		return
	else:
		index += 1
		defineMode(name, color, index)

class User(object):
	def __init__(self, name=None):
		self.name = name
		# string type
		self.defaultPhoto = name[0]
		# picture
		self.selfPhoto = None

	def addPhoto(self):
		pass

	def setName(name):
		self.name = name
		
	def __repr__(self):
		return "this is a user"
	
	def __hash__(self):
		return hash((self.name, self.defaultPhoto, self.selfPhoto))
	def __eq__(self, other):
		return self.name == other.name

class Text(object):
	def __init__(self, user, content, time=time.localtime(), rank=None, mode=0):
		# User type
		self.user = user
		self.content = content
		self.time = time
		self.rank = rank
		self.mode = mode
		
		self.y0 = 0
		self.y1 = 0
		self.selected = False
		self.sort = getSort(content)["topScoringIntent"]["intent"]
	def getTime(self):
		return self.time

	def getDay(self):
		ti = self.time
		return (ti.tm_year, ti.tm_mon, ti.tm_mday)

	def getActualTime(self):
		ti = self.time
		return "%d:%d" % (ti.tm_hour, ti.tm_min)

	def setMode(currMode):
		self.mode = currMode

	def defineMode(newMode):
		self.mode = newMode
	
	def __hash__(self):
		return hash((self.user, self.content, self.time, self.rank, self.mode))
	
	def __repr__(self):
		return "this is a text"
	def __eq__(self, other):
		return (self.user == other.user and self.content == other.content and self.time == other.time and self.mode == other.mode)

class File(object):
	def __init__(self, user, content, time):
		# User type
		self.user = user
		self.content = content
		self.time = self.getTime()

	def getTime(self):
		return time.time()
	
	def __hash__(self):
		return hash((self.user, self.content, self.time))
	
	def __repr__(self):
		return "this is a file"

