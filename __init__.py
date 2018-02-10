# events-example0.py
# Barebones timer, mouse, and keyboard events


from tkinter import *

from tkinter import filedialog

import user

import string

import time

from PIL import ImageTk, Image

import os





import socket

import sys

import threading

import export

import sort

import Sortingbot

import updownload


from queue import Queue

import test



HOST = "128.237.194.62"

PORT = 50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))

print("connected to server")



name = "Lucy"



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



    

    data.name = name 

    

    data.modeColor = ["#96ceb4","#ffcc5c","#ff6f69"]

    #screen mode

    data.screenMode=0

    data.typingName=''

    

    #######

    #added

    #######

    data.mouseX = 0

    data.mouseY = 0

    data.mousePosition = ""

    #######

    #added by Hang Yin

    #######

    data.mousejustchanged=False

    data.cursorIndex=0

    data.fileList = []

    #######

    data.server = server

    data.serverMsg = serverMsg

    #######



def mousePressed(event, data):

    # use event.x and event.y



    #splash screen

    if data.screenMode==1:

        if event.x>250 and event.x<450 and event.y> 530 and event.y<560:

            data.screenMode=2

            data.myname=data.typingName

            data.name=data.name





    #chating mode

    elif data.screenMode==2:

        #select line

        for i in range(len(data.text)-2, -1, -1):

            currText=data.text[i]

            y0 = currText.y0

            y1 = currText.y1

            if y0<0:

                break

            if data.mouseX>=200 and data.mouseX<=700 and data.mouseY<=y1 and data.mouseY>=y0:

                if currText.selected == True:

                    currText.selected = False

                else:

                    currText.selected = True

            

            

        if data.mouseX >260 and data.mouseX < 700 and data.mouseY<700 and data.mouseY>600:

            data.mousejustchanged=True

        elif data.mousePosition == "filemode0":

            filename, filepath = data.fileList[0]

            dir_path = os.path.dirname(os.path.realpath(__file__))

            dir_path = dir_path+"/"+filename

            updownload.download(filename, dir_path)

        elif data.mousePosition == "filemode1":

            filename, filepath = data.fileList[1]

            dir_path = os.path.dirname(os.path.realpath(__file__))

            dir_path = dir_path+"/"+filename

            updownload.download(filename, dir_path)

        elif data.mousePosition == "filemode2":

            filename, filepath = data.fileList[2]

            dir_path = os.path.dirname(os.path.realpath(__file__))

            dir_path = dir_path+"/"+filename

            updownload.download(filename, dir_path)

        elif data.mousePosition == "textmode0":

            print("trash")

            data.currentMode = 0

            for i in range(len(data.text)-2, -1, -1):

                currText=data.text[i]

                if currText.selected == True:

                    currText.mode = data.currentMode

        elif data.mousePosition == "textmode1":

            print("report")

            data.currentMode = 1

            for i in range(len(data.text)-2, -1, -1):

                currText=data.text[i]

                if currText.selected == True:

                    currText.mode = data.currentMode

        elif data.mousePosition == "textmode2":

            print("note")

            data.currentMode = 2

            for i in range(len(data.text)-2, -1, -1):

                currText=data.text[i]

                if currText.selected == True:

                    currText.mode = data.currentMode

 
        elif data.mousePosition == "exportNotestxt":

            print("exportTXT")

            newTxtString = export.export(data.text)

            export.exportToTxt(newTxtString)

        elif data.mousePosition == "exportNotespdf":

            print("exportPDF")

            test.exportToPDF(data.text)

        elif data.mousePosition == "uploadFile":

            print("click uploadFile")

            filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            print(filename)

            name = filename.split("/")[-1]

            print(name)

            if len(filename) >0 and len(name) > 0:

                

                data.fileList.append((name, filename))

                updownload.upload(name,filename)
                
                msg = ""
                msg = "newFile %s \n" % (name)
                print ("sending: ", msg,)
                data.server.send(msg.encode())

            

        if data.mousePosition == "mode":

            print("mode")


######

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
                otherMessage = otherMessage.replace("@@", "\n")

                newText=user.Text(otherUser, otherMessage)

                data.text.append(newText)
            elif (command == "newFile"):
                PID = msg[1]
                fileName = msg[2]
                data.fileList.append((fileName, "empty"))

        except:

            print("failed")

        serverMsg.task_done()



#######

        

            

def orderByText(data):

    pass



def drawBackground(canvas, data):

    canvas.create_rectangle(-5,-5,200,710, width = 0, fill = "#E0E0E0")

    

def drawMainButton(canvas, y, t):

    canvas.create_rectangle(30, y-30, 170, y, width = 0, fill = "#282828")

    canvas.create_polygon(30, y-30,15, y-15,30,y, width = 0, fill = "#282828")

    canvas.create_polygon(170, y-30,185,y-15,170,y, width = 0, fill = "#282828")

    canvas.create_text(100, y-12, text = t, fill = "white", font = "Courier 15")



def drawLargeButton(canvas, y, t):

    canvas.create_rectangle(25, y-35, 175, y+5, width = 0, fill = "#282828")

    canvas.create_polygon(25, y-35, 10, y-15, 25, y+5,width = 0, fill = "#282828")

    canvas.create_polygon(175, y-35, 190, y-15, 175, y+5,width = 0, fill = "#282828")

    canvas.create_text(100, y-15, text = t, fill = "white", font = "Courier 20")


def drawLine(canvas, y):

    canvas.create_line(30,y,170,y,width = 1, fill = "#707070")

    

def drawUserProfile(data, canvas, x, y, name):

    if name == data.myname:

        color = "#fff9ae"

    else:

        color = "#E0E0E0"

    canvas.create_oval(x-10, y-10, x+10, y+10, fill = color, width = 1)

    canvas.create_text(x,y, text = name[0], fill = "#686868", font = "Courier 18 bold")

    

def redrawAll(canvas, data):

    if data.screenMode==0:

        im = Image.open("start.jpeg")

        canvas.image=ImageTk.PhotoImage(im)

        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

    elif data.screenMode==1:

        im = Image.open("name.jpeg")

        canvas.image=ImageTk.PhotoImage(im)

        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

        canvas.create_rectangle(250,500,500,525,fill='white', outline='steelblue',width=3)

        canvas.create_text(255,515, text=data.typingName,font="Courier 15",anchor=W,fill='steelblue')

        canvas.create_rectangle(250,530,450,560, fill='steelblue',width=0)

        canvas.create_text(350,545, text="Start Working!!",font="Courier 20",fill='mistyrose')

        canvas.create_rectangle(200,500,250,525, fill='steelblue',width=3,outline='steelblue')

        canvas.create_text(225,512.5,text="name",font="Courier 20",fill='mistyrose')

    elif data.screenMode==2:

        drawBackground(canvas, data)

        drawMainButton(canvas, 60,"FILE LIST")

        

        

        drawLine(canvas, 90)

        drawLine(canvas, 120)

        drawLine(canvas, 150)

        

        y = 90

        for i in range(3):

            drawLine(canvas, y)

            if i<len(data.fileList):

                

                filename, filepath = data.fileList[i]

                if data.mousePosition == "filemode%d"%(i):

                    canvas.create_text(100, y-11, text = filename, fill = "#282828", font = "Courier 15")

                else:

                    canvas.create_text(100, y-9, text = filename, fill = "#282828", font = "Courier 12")

            y+=30

        #exprot txt and pdf
        #"EXPORT NOTES"
        canvas.create_rectangle(30, 180, 170, 200, width = 0, fill = "#282828")
        canvas.create_polygon(30, 180,15, 190,30,200, width = 0, fill = "#282828")
        canvas.create_polygon(170, 180,185,190,170,200, width = 0, fill = "#282828")
        canvas.create_text(100, 190, text = "EXPORT NOTES (pdf)", fill = "white", font = "Courier 12")
        
        canvas.create_rectangle(30, 210, 170, 230, width = 0, fill = "#282828")
        canvas.create_polygon(30, 210,15, 220,30,230, width = 0, fill = "#282828")
        canvas.create_polygon(170, 210,185,220,170,230, width = 0, fill = "#282828")
        canvas.create_text(100, 220, text = "EXPORT NOTES (txt)", fill = "white", font = "Courier 12")
        



        #+30 = 240

        drawMainButton(canvas, 270, "MODE")

        y = 300

        for i in range(6):

            drawLine(canvas, y)

            if i<len(data.mode):

                

                t = "#"+data.mode[i]

                if data.mousePosition == "textmode%d"%(i):

                    canvas.create_text(100, y-11, text = t, fill = "#282828", font = "Courier 15")

                else:

                    canvas.create_text(100, y-9, text = t, fill = "#282828", font = "Courier 12")

                if data.currentMode == i:

                    canvas.create_oval(179, y-14, 180+6,y-14+7, fill = data.modeColor[i], width = 1)

                else:

                    canvas.create_oval(180, y-12, 180+5,y-12+5, fill = "#E0E0E0", width = 1)



            y+=30



        drawMainButton(canvas, 480, "ADD MODE")

        drawMainButton(canvas, 540, "UPLOAD FILE")

        

        if data.mousePosition == "mode":

            drawLargeButton(canvas, 270, "MODE")

        elif data.mousePosition == "exportNotespdf":
            canvas.create_rectangle(25, 200-35, 175, 200+5, width = 0, fill = "#282828")
            canvas.create_polygon(25, 200-35, 10, 200-15, 25, 200+5,width = 0, fill = "#282828")
            canvas.create_polygon(175, 200-35, 190, 200-15, 175, 200+5,width = 0, fill = "#282828")
            canvas.create_text(100, 200-15, text = "EXPORT NOTES (pdf)", fill = "white", font = "Courier 15")
        elif data.mousePosition == "exportNotestxt":
            canvas.create_rectangle(25, 230-35, 175, 230+5, width = 0, fill = "#282828")
            canvas.create_polygon(25, 230-35, 10, 230-15, 25, 230+5,width = 0, fill = "#282828")
            canvas.create_polygon(175, 230-35, 190, 230-15, 175, 230+5,width = 0, fill = "#282828")
            canvas.create_text(100, 230-15, text = "EXPORT NOTES (txt)", fill = "white", font = "Courier 15")
            

        elif data.mousePosition == "fileList":

            drawLargeButton(canvas, 60, "FILE LIST")

        elif data.mousePosition == "uploadFile":

            drawLargeButton(canvas, 540, "UPLOAD FILE")

            

        #orderByTime(data)



        if data.text !=[]:

            drawText(canvas,data)

        drawEntryBox(canvas,data)

        

    

        

def motion(event, data):

    data.mouseX, data.mouseY = event.x, event.y

    
    if 30<=data.mouseX<=170 and 180<=data.mouseY<=200:
        data.mousePosition = "exportNotespdf"
    
    elif 30<=data.mouseX<=170 and 210<=data.mouseY<=230:
        data.mousePosition = "exportNotestxt"
        

    elif 30<=data.mouseX<=170 and 270-30<=data.mouseY<=270:

        data.mousePosition = "mode"

        print(data.mousePosition)

    elif 30<=data.mouseX<=170 and 60-30<=data.mouseY<=60:

        data.mousePosition = "fileList"

    elif 30<=data.mouseX<=170 and 540-30<=data.mouseY<=540:

        data.mousePosition = "uploadFile"

        print(data.mousePosition)

    else:

        y = 300

        for i in range(6):

            if i<len(data.mode):

                if 30<=data.mouseX<=170 and y-30<=data.mouseY<=y:

                    data.mousePosition = "textmode%d"%(i)

                    print(data.mousePosition)

                    return None 

            y+=30

        y = 90

        for i in range(3):

            if i<len(data.fileList):

                if 30<=data.mouseX<=170 and y-30<=data.mouseY<=y:

                    data.mousePosition = "filemode%d"%(i)

                    print(data.mousePosition)

                    return None 

            y+=30

        data.mousePosition = ""

    

        

    return None



######

#added by Yin Hang

######

def keyPressed(event, data):

    # use event.char and event.keysym

    if data.screenMode ==0:

        data.screenMode=1

    elif data.screenMode==1:

        if event.char in string.printable and event.keysym!='??':

            data.typingName += event.char

        elif event.keysym=="BackSpace":

            data.typingName=data.typingName[:-1]

    elif data.screenMode==2:

        if event.keysym=="Return":

            data.typingText+="\n"

            data.cursorIndex+=1

            newText=user.Text(data.myname,data.typingText)
            newText.mode=data.currentMode

            data.text.append(newText)

            print(newText.content)

            

            

            msg = ""

            sendText = data.typingText.replace(" ","~")
            sendText = sendText.replace("\n", "@@")

            msg = "newMessage %s %s \n" % (data.myname, sendText)

            print ("sending: ", msg,)

            data.server.send(msg.encode())

        

            data.typingText=''

            

        elif event.char in string.printable and event.keysym!='??':

            data.typingText=data.typingText[:data.cursorIndex]+event.char+data.typingText[data.cursorIndex:]

            data.cursorIndex +=1

            if len(data.typingText.splitlines()[-1])%44==0 and len(data.typingText)!=0:

                data.typingText += "\n"

                data.cursorIndex +=1

            print(data.typingText)

            print(repr(data.typingText))





        elif event.keysym=="BackSpace":

            data.typingText=data.typingText[:-1]

            data.cursorIndex -=1



def rearrange(aText):

    charMaxLen=(660-260)/9

    lineNum=len(aText)//charMaxLen +1

    newText=''

    count=0

    lastLine=aText.splitlines()[-1]

    prevs=aText.splitlines()[:-1]

    for i in range(len(lastLine)):

        c=lastLine[i]

        count +=1



        if i % int(charMaxLen) ==0 and i!=0:

            c="\n"+lastLine[i]

        newText += c

    allLines=prevs+[newText]

    return "\n".join(allLines)



def drawEntryBox(canvas,data):

    #draw entry box

    canvas.create_rectangle(250, 600, 700, 700, width = 0, fill = "#E0E0E0")

    content=canvas.create_text(260,605,text=data.typingText, anchor=NW,

        font ='Courier 15')



    #manage cursor

    canvas.focus_set()

    canvas.focus(content)

    if data.mousejustchanged==True:

        i=canvas.index(content,'@'+str(data.mouseX)+','+str(data.mouseY))

        data.cursorIndex=i

        data.mousejustchanged=False

    canvas.icursor(content,data.cursorIndex)



def drawText(canvas,data):

    #draw upper text

    xLeft=260

    xRight=660

    charMaxLen=(xRight-xLeft)/9

    yBottom=590

    yTop=50





    #draw the text at the bottom

    baseText=data.text[-1]

    lineNum=len(baseText.content)//charMaxLen +1  #for name display

    #"draw text"

    canvas.create_text(xLeft, yBottom - 3 -lineNum*16 , text=rearrange(baseText.content),

                     font='Courier 15',anchor=NW)

    #draw time

    canvas.create_text(xRight, yBottom - 3 -lineNum*16 , text=baseText.getActualTime(),

                                font="Courier 10", anchor=SE)

    #draw name

    canvas.create_text(xLeft,  yBottom - 3 -lineNum*16-16, text=baseText.user,

                     font='Courier 15 bold',anchor=NW)

    #draw profile

    drawUserProfile(data, canvas, 225, yBottom - 3 -lineNum*16-5, baseText.user)

    #draw button 

    if data.mouseX>= 200 and data.mouseX<=700 and data.mouseY<=yBottom and data.mouseY>=yBottom - 3 -lineNum*16-16:

        data.mousePosition = "textHightlight%d"%(len(data.text)-1)

    if data.mousePosition == "textHightlight%d"%(len(data.text)-1):

        canvas.create_oval(690-2, yBottom - 3 -lineNum*16-5-2, 690+6+2,2+yBottom - 3 -lineNum*16-5+7, fill = data.modeColor[baseText.mode], width = 1)

    else:

        canvas.create_oval(690, yBottom - 3 -lineNum*16-5, 690+6,yBottom - 3 -lineNum*16-5+7, fill = data.modeColor[baseText.mode], width = 1)

            



    if len(data.text)==1:

        canvas.create_text((xLeft+xRight)/2, yBottom - 3 -lineNum*16-16, text=baseText.getDay(),

                     font='Courier 15')



    yBottom= yBottom - 3 -lineNum*16-16

    

    lastDay=baseText.getDay()

    lastTime=baseText.getActualTime()





    for i in range(len(data.text)-2, -1, -1):

        

        currText=data.text[i]

        currActualTime=currText.getActualTime()

        currDay=currText.getDay()

        

        #mark highlighted/mouse position

        if data.mouseX>= 200 and data.mouseX<=700 and data.mouseY<=yBottom and data.mouseY>=yBottom - 3 -lineNum*16-16:

            data.mousePosition = "textHightlight%d"%(i)

        #pass in check points of y0 and y1 to text object

        currText.y1 = yBottom

        currText.y0 = yBottom - 3 -lineNum*16-16



        baseText=data.text[-1]

        lineNum=len(currText.content)//charMaxLen +1  #for name display

        #"draw text"

        canvas.create_text(xLeft, yBottom - 3 -lineNum*16 , text=rearrange(currText.content),

                     font='Courier 15',anchor=NW)

        #draw time

        canvas.create_text(xRight, yBottom - 3 -lineNum*16 , text=currText.getActualTime(),

                                font="Courier 10", anchor=SE)

        #draw name

        canvas.create_text(xLeft,  yBottom - 3 -lineNum*16-16, text=currText.user,

                     font='Courier 15 bold',anchor=NW)

        #draw Profile

        drawUserProfile(data, canvas, 225, yBottom - 3 -lineNum*16-5, currText.user)

        #draw Mode Circle

        if currText.selected == True:

            canvas.create_oval(690-4, yBottom - 3 -lineNum*16-5-4, 690+6+4,4+yBottom - 3 -lineNum*16-5+7, fill = None, width = 1)

        if data.mousePosition == "textHightlight%d"%(i):

            canvas.create_oval(690-2, yBottom - 3 -lineNum*16-5-2, 690+6+2,2+yBottom - 3 -lineNum*16-5+7, fill = data.modeColor[currText.mode], width = 1)

        else:

            canvas.create_oval(690, yBottom - 3 -lineNum*16-5, 690+6,yBottom - 3 -lineNum*16-5+7, fill = data.modeColor[currText.mode], width = 1)



        #canvas.create_oval(180, y-12, 180+5,y-12+5, fill = "#E0E0E0", width = 1)



        yBottom= yBottom - 3 -lineNum*16-16



        if currDay != lastDay or i==0:

            #draw last day and last time

            canvas.create_text((xLeft+xRight)/2, yBottom, text=lastDay,

                     font='Courier 15')

            lastDay=currDay

            yBottom -= 18

        if yBottom<yTop:

            break


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

    root.bind('<Motion>', lambda event:

                            motion(event, data))

    

    timerFiredWrapper(canvas, data)


    # and launch the app

    root.mainloop()  # blocks until window is closed

    print("bye!")



serverMsg = Queue(100)

threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()





run(width=700, height=700)

