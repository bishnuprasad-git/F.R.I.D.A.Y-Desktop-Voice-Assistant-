import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser	
import os
import plyer
import time
import datetime
import random
import pyglet
import win32api
import fnmatch,re
import pafy
import vlc
# import easygui
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
import threading
from tkinter import *
from tkinter import messagebox
import PIL.Image,PIL.ImageTk
from threading import *
import requests
from bs4 import BeautifulSoup
import tkinter

def wish():
	hr=datetime.datetime.now().hour
	min=datetime.datetime.now().hour
	if hr<12:
		msg="Good Morning"
	elif hr>=12 and hr<15:
		msg="Good Noon"
	elif hr>=15 and hr<17:
		msg="Good Afternoon"
	elif hr>=17 and hr<19:
		msg="Good Evening"
	else:
		msg="Good Night" 
	# print(msg," Mr. Bishnu")
	return msg

engine=pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
#drives
msg=wish()

def speak(audio):
	global engine
	engine.say(audio)
	engine.runAndWait()


# result = []
def find(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            # name=name.lower()
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result



def startNotification():
	msg=wish()
	plyer.notification.notify(
		title="F.R.I.D.A.Y",
		message=f"Hii...Bishnu {msg}\nF.R.I.D.A.Y program is Listening You...\nPlease say something...",
		timeout=10,
		app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
		)
	tt=f"Hii...Mr.Bishnu\n{msg}\nFRIDAY program is Listening You...\nPlease say something..."
	speak(tt)

def endNotification():
	msg=wish()
	plyer.notification.notify(
		title="F.R.I.D.A.Y",
		message=f"Hey Bishnu {msg}\nThanks for using...F.R.I.D.A.Y.\nI am grateful to Mr. Bishnu Prasad Behera",
		timeout=2,
		app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
		)


def doExit():
	endNotification()
	global p,computer
	speak("Thanks Bishnu...I am always with you")
	computer.config(text="Thanks Bishnu...I am always with you")
	p.quit()
	exit(1)

def selection():
	drive=str(radio.get())
	print(drive)

# def tkin():

# global drives
drives = win32api.GetLogicalDriveStrings()
# print(drives)
drives = drives.split('\000')[:-1]
p=Tk()
p.geometry("700x650")
im=PIL.Image.open('ironman.jpg')
img = im.resize((700,650),PIL.Image.ANTIALIAS)
img.save('pre.png')
background_image=PhotoImage(file='pre.png')
background_label =Label(p, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
p.title("F.R.I.D.A.Y (Made by BISHNU)")
p.resizable(0,0)
p.iconbitmap('Aha-Soft-Iron-Man-Tony-Stark.ico')
os.remove('pre.png')
com_img_open=PIL.Image.open('computer.png')
com_img=com_img_open.resize((100,100),PIL.Image.ANTIALIAS)
com_img=PIL.ImageTk.PhotoImage(com_img)
computer_img=Label(p,image=com_img)
computer_img.place(x=20,y=20)
computer=Label(p,text=f"Hii...Mr.Bishnu {msg}.",fg='red',wraplength=200)
computer.place(x=130,y=20)
computer.config(height=7,width=40)
user_img_open=PIL.Image.open('user.png')
user_img=user_img_open.resize((100,100),PIL.Image.ANTIALIAS)
user_img=PIL.ImageTk.PhotoImage(user_img)
use_img=Label(p,image=user_img)
use_img.place(x=20,y=150)
green=Label(p,width=3,height=2,bg="green")
green.place(x=330,y=275)
user_s=Label(p)
user_s.place(x=130,y=160)
exitButton = Button(p,text='stop program',command=doExit)
exitButton.place(x=20,y=260)
direc=Label(p,text="choose drive to search media file",fg='red')
x1=20
y1=330
rad=""
drive=""
inte=0
for i in drives:
	rad="rad"+str(inte)
	# print(rad)
	rad=Radiobutton(p, text=i, value=inte,command=selection).place(x=x1,y=y1)
	x1+=50
	inte+=1
direc.place(x=20,y=302)






# def tkin():
# 	global p;
# 	global computer
# 	global green;
# 	global user_s;
# 	global drives;
	
	

def takeCommand():
	global green,user_s,red
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		# red.place(x=20,y=40)
		green.place_forget()
		user_s.place_forget()
		r.pause_threshold=1
		audio=r.listen(source)
	try:
		print("Recognizing...")
		green.place(x=330,y=275)
		# red.place_forget()
		user_s.place_forget()
		query=r.recognize_google(audio,language='en-in')
		print(f"User said : {query}\n")
		user_s.place(x=130,y=160)
		user_s.config(text=f"User : {query}")
		# red.place_forget()
		green.place_forget()
		# lis.config(text="")
		# lik.config(text="")
		# la2=Label(p,text=f"User said : {query}")
		# la2.pack()
	except:
		print("say again. Please...")
		return "None"
	return query


# def radioButton():
# 	global rad
# 	global drives
# 	global p
# 	# radio = IntVar()
# 	x1=20
# 	y1=330
# 	rad=""
# 	drive=""
# 	inte=0
# 	for i in drives:
# 		rad="rad"+str(inte)
# 		print(rad)
# 		rad=Radiobutton(p, text=i, value=inte,command=selection).place(x=x1,y=y1)
# 		x1+=50
# 		inte+=1
# 	p.mainloop()


def comp_main():
	global tt,computer,p,drives,user_s
	tt=f"Hii...Mr.Bishnu\n{wish()}\nFRIDAY program is Listening You...\nPlease say something..."
	# speak(tt)
	print('comp_main')
	loop=True
	while loop:
		# p.update()
		query=takeCommand().lower()
		print(query)
		if "exit program" in query:
			endNotification()
			user_s.config(text="exit program")
			computer.config(text="Thanks Bishnu...I am always with you")
			speak("Thanks Bishnu...I am always with you")
			p.quit()
			loop=False
			exit(1)
		# speak(query)
		elif "letter" in query and len(list(query.split()))==2:
			li=list(query.split())
			d=li[1]
			count=0
			for i in drives:
				if d==i[0].lower():
					# print("rad"+str(count))
					# k="rad"+str(count)
					# k.select()
					rad0.select()
					break
		elif "calculate" in query:
			st=list(query.split())
			try:
				if st[1].__contains__('.')==False:
					a=int(st[1])
					b=int(st[3])
				else:
					a=float(st[1])
					b=float(st[3])
				op=st[2]
				if op=="+":
					tt=a+b
					print(tt)
					user_s.config(text=f"calculate {a} + {b} ")
					computer.config(text=tt)
					speak(tt)
				elif op=="-":
					tt=a-b
					print(tt)
					user_s.config(text=f"calculate {a} - {b} ")
					computer.config(text=tt)
					speak(tt)
				elif op=="multiply":
					tt=a*b
					print(tt)
					user_s.config(text=f"calculate {a} * {b} ")
					computer.config(text=tt)
					speak(tt)
				elif op=="divide":
					tt=a/b
					print(tt)
					user_s.config(text=f"calculate {a} / {b} ")
					computer.config(text=tt)
					speak(tt)
				elif op=="modulus":
					tt=a%b
					print(tt)
					user_s.config(text=f"calculate {a} % {b} ")
					computer.config(text=tt)
					speak(tt)
			except:
				print("error")
				tt='Please Say Again...Bishnu'
				computer.config(tt)
				speak(tt)
		elif "find binary of" in query:
			st=list(query.split())
			try:
				num=int(st[3])
				tt=bin(num)
				print(tt[2:])
				speak(tt[2:])
			except:
				tt="sorry!Bishnu I can't find"
				print(tt)
				speak(tt)
		elif "open amazon" in query:
			webbrowser.open("amazon.com")
		elif ("play music" in query) and len(list(query.split()))>=2:
			part=query[11:]
			print(part)
			for i in drives:
				if i=="H:\\":
					find(f'*{part}*.mp3',i)
			# print('files are -->')
			print(result)
			if len(result)==0:
				print("No match found")
			elif len(result)==1:
				player=vlc.MediaPlayer(result[0])
				plyer.notification.notify(
					title="Bishnu Prasad",
					message=f"Playing...{result[0]}",
					timeout=10,
					app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
					)
				player.play()
				result.clear()
				while True:
					break
			elif len(result)>1:
				for i in range(len(result)):
					print('option '+chr(ord(str(i))+49), "--", result[i])
				speak("choose option from above")
				print("choose option from above")
		elif "search" in query and len(query)>=2:
			try:
				userq=query[6:]
				speak("searching for you Bishnu")
				tt=wikipedia.summary(userq,sentences=2)
				speak(tt)
			except:
				tt="Sorry ! , No information found for you Bishnu... I am soooo sorry"
				speak(tt)
				computer.config(text=tt)
		elif "the time" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")  
			tt=f"Bishnu, the time is {strTime}"
			computer.config(text=tt) 
			speak(tt)
			# print(f"Sir, the time is {strTime}")
		elif "option" in query and len(list(query.split()))==2:
			st=list(query.split())
			doMatch=ord(st[1])-97
			for i in range(len(result)):
				if doMatch==i:
					player=vlc.MediaPlayer(result[i])
					plyer.notification.notify(
					title="Audio is Playing...",
					message=f"{result[0]}",
					timeout=10,
					app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
					)
					player.play()
					tt="Playing...music for you Bishnu"
					computer.config(text=tt)
					speak(tt)
					result.clear()
					break
		elif "play video" in query and len(list(query.split()))>2:
			part=query[11:]
			print(part)
			for i in drives:
				if i=='H:\\':
					find(f'*{part}*.mp4',i)
			# print('files are -->')
			print(result)
			if len(result)==0:
				print("No match found")
			elif len(result)==1:
				player=vlc.MediaPlayer(result[0])
				plyer.notification.notify(
					title="Video is Playing...",
					message=f"{result[0]}",
					timeout=10,
					app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
					)
				# instance = vlc.Instance()
				# player = instance.media_player_new()
				# player.set_mrl(result[0])
				player.play()
				# player.play()
				# Instance = vlc.Instance()
				# player = Instance.media_player_new()
				# Media = Instance.media_new(result[0])
				# Media.get_mrl()
				# player.set_media(Media)
				# player.play()
				while True:
					break
				# Instance = vlc.Instance()
				# player = Instance.media_player_new()
				# Media = Instance.media_new(result[0])
				# Media.get_mrl()
				# player.set_media(Media)
				# player.play()
				# while player.get_state() !=6:
				#     continue
				tt="Now Playing - ",result[0]
				computer.config(text=tt)
				speak(tt)
				result.clear()
			elif len(result)>1:
				for i in range(len(result)):
					print('option '+chr(ord(str(i))+49), "--", result[i])
				speak("choose option from above")
				print("choose option from above")
		elif "stop program" in query:
			tt="stop program"
			user_s.config(text=tt)
			tt="Thanks Bishnu...I am always with you"
			computer.config(text=tt)
			speak(tt)
			print("Thanks Bishnu...I am always with you")
			endNotification()
			loop=False
			exit(1)
			p.quit()
		elif "pause media" in query:
			tt="pause media"
			user_s.config(text=tt)
			tt="media paused Bishnu"
			computer.config(text=tt)
			speak(tt)
			try:
				player.pause()
			except:			
				print("exception in pause")
				speak("No media found")
				print("No media found")
		elif "play media" in query:
			tt="play media"
			user_s.config(text=tt)
			try:
				player.play()
			except:
				print("exception in play")
				speak("No media found")
				print("No media found")
		elif "stop media" in query:
			tt="stop media"
			user_s.config(text=tt)
			tt="media stopped Bishnu"
			computer.config(text=tt)
			speak(tt)
			try:
				player.stop()
			except:
				print("exception in stop")
				speak("No media found")
				print("No media found")
		elif "play" in query:
			# re=YoutubeSearch('code with harry',max_results=10).to_json()
			print("Searching from Internet...")
			search=query[5:]
			print(search)
			try:
				txt="Playing Video for you Bishnu"
				computer.config(text=txt)
				speak(txt)
				# re=YoutubeSearch(search,max_results=10).to_dict()
				# print(re[0].get('channel_link'))
				videosSearch = VideosSearch(search, limit = 4)
				url=videosSearch.result()['result'][0]['link']
				# print(url)
				tt="Video is loading..."
				computer.config(text=tt)
				speak(tt)
				# url="https://www.youtube.com/"+re[0].get('channel_link')
				video=pafy.new(url)
				best=video.getbest()
				player=vlc.MediaPlayer(best.url)
				player.play()
				txt=f"Now Playing - {video.title}"
				computer.config(text=txt)
				plyer.notification.notify(
					title="Bishnu Prasad",
					message=f"Playing...{video.title}",
					timeout=10,
					app_icon='Aha-Soft-Iron-Man-Tony-Stark.ico'
					)
				pass
			except:
				txt="while searching video from internet some error occured... i am so sorry Bishnu"
				print(txt)
				speak(txt)
		# elif "coronavirus update india" in query:
		# 	cp=soup.find_all('div',class_='iblock_text')
		# 	st=""
		# 	for i in cp:
		# 		p1=i.find('div',class_='info_label')
		# 		p2=i.find('span',class_='icount')
		# 		st=st+p1.get_text()+' - '+p2.get_text()+'\n'
		# 	computer.config(text=st)
		# 	speak(st)
		# elif "coronavirus update" in query:
		# 	cp=soup.find_all('div',class_='views-row')
		# 	ust=list(query.split())
		# 	if len(ust)==3:
		# 		state=ust[2]
		# 	else:
		# 		state=ust[2]+" "+ust[3]
		# 	emptyst=""
		# 	for i in cp:
		# 		if i.find('span',class_='st_name').get_text().lower() == state:
		# 			p3=i.find('div',class_='st_all_counts').find_all('div')
		# 			for j in p3:
		# 				emptyst=emptyst+' - '+j.get_text()+'\n'
		# 			print(emptyst)
		# 			computer.config(text=emptyst)
		# 			speak(emptyst)

# if __name__=='__main__':

result=[]
startNotification()
t2=threading.Thread(target=comp_main)
t2.start()
p.mainloop()