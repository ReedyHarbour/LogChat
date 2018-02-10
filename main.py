# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import user
import string
import time




import socket
import sys
import threading
from queue import Queue

HOST = "128.237.194.62"
PORT = 50003
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST,PORT))
print("connected to server")
name = "Rebecca"

# taken from 15112 course website
def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")


####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.text=[]
    data.typingText=''
    data.mode=["trash", "report","note"]
    data.currentMode=0
    data.selfDefinedMode=[]
    data.myname=name
    
    data.server = server
    data.serverMsg = serverMsg
    
    data.name = name  



def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym=="Return":
        newText=user.Text(data.myname,data.typingText)
        data.text.append(newText)
        
        
        msg = ""
        sendText = data.typingText.replace(" ","~")
        msg = "newMessage %s %s \n" % (data.myname, sendText)
        print ("sending: ", msg,)
        data.server.send(msg.encode())
        
        
        
        data.typingText=''
        for currText in data.text:
            print(currText.content)
        
    elif event.char in string.printable and event.keysym!='??':
        data.typingText += event.char
        print(data.typingText)
    elif event.keysym=="BackSpace":
        data.typingText=data.typingText[:-1]




def timerFired(data):
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        try:
            print("received: ", msg, "\n")
            msg = msg.split()
            command = msg[0]
            if (command == "myIDis"):
                myPID = msg[1]
            elif (command == "newPerson"):
                newPID = msg[1]
            elif (command == "newMessage"):
                PID = msg[1]
                otherUser = msg[2]
                otherMessage = msg[3]
                otherMessage = otherMessage.replace("~", " ")
                newText=user.Text(otherUser, otherMessage)
                data.text.append(newText)
        except:
            print("failed")
        serverMsg.task_done()
        
            
def orderByText(data):
    pass

def drawBackground(canvas, data):
    canvas.create_rectangle(-5,-5,200,710, fill = "darkGreen")
    
def redrawAll(canvas, data):
    drawBackground(canvas, data)
    #orderByTime(data)
    i = 0
    for currText in data.text:
        canvas.create_text(50,50+i,text=currText.user)
        canvas.create_text(100,50+i,text=currText.content)
        i+=20

    

####################################
# use the run function as-is
####################################

def run(width=700, height=700):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run(width=700, height=700)
