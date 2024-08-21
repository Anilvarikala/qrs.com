
# DOCUMENTATION SECTION
''' 
   DATE : 06/07/2024
   NAME : VARIKALA ANIL,VALA KARTHIK
   PROJECT-TITLE : QRS (QUICK REVIEW SYSTEM)
   LANGUAGE : PYTHON
'''

#importing all the packages and modules 
from tkinter import *
import tkinter
from tkinter.ttk import Style
import cv2
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import imutils
import time

#Controlling the video
stream = cv2.VideoCapture("run out video.mp4")

#Using boolean variable for control of my text
flag = True

#Control my video using play function
def play(speed):

    global flag
    print(f"You cliked on play.speed is {speed}")
   
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame = stream.read()
     
    #come out from the video.
    if not grabbed:
        exit()

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(120,25,fill="black",font="Times 20 italic bold",text="Decision Pending")
    flag = not flag


#function for out
def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print('Player is out')

#function for not_out
def not_out():
    thread = threading.Thread(target=pending,args=("not_out",))
    thread.daemon = 1
    thread.start()
    print('Player is not out')

#function for Decision pending
def pending(decision):
    
    #Decison pending image
    frame = cv2.cvtColor(cv2.imread("decision_pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =  frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    
    #waiting for 2 seconds
    time.sleep(2)
    
    #Displaying the images of out or not_out based on the conditons 
    if decision == 'out':
        decision_Image = "out.png"
    else:
        decision_Image = "not_out.png"

    #Displaying the final result  
    frame = cv2.cvtColor(cv2.imread(decision_Image),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =  frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    print("Pending!")

#Adjustiong widths ans heigths of the Images
SET_WIDTH = 650
SET_HEIGHT = 380

#Creating a window object
window = tkinter.Tk()

#TItle of my web-page
window.title("QUICK REVIEW SYSTEM")

#Initial Image
cv_img = cv2.cvtColor(cv2.imread("drs.png"), cv2.COLOR_BGR2RGB)
cv_img = imutils.resize(cv_img,width=SET_WIDTH,height=SET_HEIGHT)
canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


btn = tkinter.Button(window,text = "<< Previous (fast)",width=50,command=partial(play,-3))
btn.pack()

btn = tkinter.Button(window,text = "<< Previous (slow)",width=50,command=partial(play,1))
btn.pack()

btn = tkinter.Button(window,text = "Next (slow) >>",width=50,command=partial(play,0.5))
btn.pack()

btn = tkinter.Button(window,text = "Next (fast) >>",width=50,command = partial(play,15))
btn.pack()

btn = tkinter.Button(window,text = " Give out",width=50,command=out)
btn.pack()

btn = tkinter.Button(window,text = " Give not out",width=50,command=not_out)
btn.pack()

#Run my application.
window.mainloop()

