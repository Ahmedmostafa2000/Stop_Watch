from tkinter import *
from time import time,sleep
import datetime




def calc_time(start,end,pause_time):
	time_form = [0,0,0]
	t = end-start-pause_time
	time_form[0] = t%60
	time_form[1] = t//60
	time_form[2] = t//3600
	return time_form

def save_res():
	with open("1.txt","a") as f:
		today=str(datetime.date.today())
		f.write(f"\n{today}, {t}")

def pause():
	global run, pause_time
	run = False
	pause_time = time()

def starting():
	global run, pause_time
	run = True
	

def reset():
	global start
	start = time()

root = Tk()
run = False
start = time()
label = None
pause_time = time()
t = ""
save = Button(root,anchor = "ne", text = "Save result", command=save_res, bg = "black",fg = "white") 
save.pack()

pause_button = Button(root, text = "Pause", command=pause, bg = "black",fg = "white")
pause_button.pack()

con_button = Button(root, text = "Start", command=starting, bg = "black",fg = "white") 
con_button.pack()
t = "0 : 0 : 0"

while 1:
	if run:
		end = time()
		t = calc_time(start,end,pause_time)
		t = f"{int(t[2])} : {int(t[1])} : {int(t[0])}"
	if label:
		label.destroy()

	label = Label(root,text= f"{t}",padx = 200,pady = 100,bg = "black",fg = "white")
	label.config(font=("Consolas", 50))
	label.pack()


	root.update()