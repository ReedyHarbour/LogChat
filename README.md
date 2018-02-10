# logchat
Repository for our tartanhacks 2018 project logchat, a new chat easy for groupwork
## Contributors
  Anita Li, Michelle Ma, Hesper Yin, Rebacca Pei
## Description
https://youtu.be/y3u6zWmh7q4
  Our project is a chat platform designed for group of co-workers. Log Chat combines chat room and markdown editor. When wokers are chatting, their progress reports and notes are recorded can be maked down
  
  It uses socket to connect users, and users put in their id and name to enter the same chat room. 
  The main feature of this chat platform is that it can organize useful messages into work log or notes based on customized mode and time. To prevent irrelevant messages from distracting co-workers, we applied Microsoft Azure LUIS and used machine learning to train the bot so that it can filter out irrelavent information, like food, entertainment and sleep or rest discussions. When the log or working notes are exported in either txt or pdf form, the filtered information won't appear on the log. To export logs in PDF form, we used a library called report la. Also, we used Microsoft Azure Storage(Blob Storage) to enable file transfer among users, and create a clear file lists on the interface to make file downloads convenient. The interface is based on Tkinter, and we used Pillow to process images on it. We've designed our app logo ourselves.
## Installation
  Developed by Python 3
  Requried modules: Microsoft Azure, sockets, requests, pillow, reportlab, tkinter
## Run
  __init__.py
## Screenshot
  check screenshot.jpg
