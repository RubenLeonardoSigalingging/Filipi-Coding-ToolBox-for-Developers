#!/usr/bin/env python3


# Filipi 4:6
# Janganlah hendaknya kamu kuatir tentang apa pun juga, tetapi nyatakanlah dalam segala hal keinginanmu kepada Allah dalam doa dan permohonan dengan ucapan syukur.
# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: 22 Juli, 2022, Pukul 22:19 PM.
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10
# Tipe Program: GUI (graphical user interface)
# Tetap Semangat dan Jangan Menyerah :)


# Import semua module Python yang diperlukan.
import os
from os import system
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("cls")
	os.system("pip install tk")
	os.system("pip install pycryptodome")
	os.system("pip install requests")
	os.system("pip install pywhatkit")
	os.system("pip install pytube")
	os.system("pip install instaloader")
	os.system("pip install wikipedia")
	os.system("pip install tqdm")
	os.system("pip install phonenumbers")
	os.system("pip install pyfiglet")
	os.system("pip install base10")
	os.system("pip install base91")
	os.system("pip install base45")
	os.system("pip install pybase62")
	os.system("pip install rsa")
	os.system("pip install gTTS")
	os.system("pip install moviepy")
	os.system("pip install python3-nmap")
	os.system("pip install stegano")
	os.system("pip install bs4")
	os.system("pip install Faker")
	os.system("pip install py-cpuinfo")
	os.system("pip install psutil")
	os.system("pip install cowsay")
	os.system("pip install pyttsx3")
	os.system("pip install PyAutoGUI")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("pip install tk")
	os.system("pip install pycryptodome")
	os.system("pip install requests")
	os.system("pip install pywhatkit")
	os.system("pip install pytube")
	os.system("pip install instaloader")
	os.system("pip install wikipedia")
	os.system("pip install tqdm")
	os.system("pip install phonenumbers")
	os.system("pip install pyfiglet")
	os.system("pip install base10")
	os.system("pip install base91")
	os.system("pip install base45")
	os.system("pip install pybase62")
	os.system("pip install rsa")
	os.system("pip install gTTS")
	os.system("pip install moviepy")
	os.system("pip install python3-nmap")
	os.system("pip install stegano")
	os.system("pip install bs4")
	os.system("pip install Faker")
	os.system("pip install py-cpuinfo")
	os.system("pip install psutil")
	os.system("pip install cowsay")
	os.system("pip install pyttsx3")
	os.system("pip install PyAutoGUI")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("clear")
import time
import re
import webbrowser
import datetime
import tkinter
from tkinter import *
import requests
import json
import urllib
import base64
import base45
import base10
import base91
import base62
import pyfiglet
import cpuinfo
import psutil
import platform
import rsa
import marshal
import hashlib
import pyttsx3
import gtts
import phonenumbers
import bs4
import moviepy.editor
import socket
import stegano
import faker
import wikipedia
import pytube
import instaloader
import tqdm
import tkinter
from tkinter import *
import tkinter.ttk
import pyautogui
import random
import subprocess
import urllib.parse
from urllib.parse import *
import string


# Python - Tkinter Cursors
Python_Tkinter_Cursors=["arrow","circle","clock",
"cross","dotbox","exchange","fleur","heart","man",
"mouse","pirate","plus","shuttle","sizing","spider",
"spraycan","star","target","tcross","trek",
"watch"]


# Kita buat fungsi untuk menampung Tkinter
def Filipi(Created_By="Ruben Leonardo Sigalingging"):
	import pywhatkit
	# Buat fungsi tkinter terlebih dahulu, Dengan metode Tk()
	Fungsi_Utama_Tkinter=Tk()
	# Kita buat ukuran GUI nya, dengan metode .Geometry
	Fungsi_Utama_Tkinter.geometry("500x500")
	# Buat Judul atau Title program.
	Fungsi_Utama_Tkinter.title("Filipi - Coding ToolBox for Developers")
	# Kita atur warna latar belakang atau background. dengan metode .configure
	Fungsi_Utama_Tkinter.configure(background="#000000",cursor="crosshair")


	# Buat frame untuk NavBar
	Fungsi_NavBar=Frame(Fungsi_Utama_Tkinter,bg="#008b8b",cursor="pirate",height=2,relief=FLAT,width=25)
	Fungsi_NavBar.pack(expand=False,fill=BOTH,side="top")


	# Buat label lalu bungkus kedalam Fungsi NavBar.
	Fungsi_Label=Label(Fungsi_NavBar,anchor="center",bg="#008b8b",cursor="pirate",
		font=("Ubuntu",25),fg="#ffffff",height=3,justify="center",
		padx=25,pady=0,relief=FLAT,text="Filipi - Coding ToolBox for Developers",width=25)
	Fungsi_Label.pack(expand=False,fill=BOTH,side="top")


	# Buat fungsi frame yang akan berada di sisi kiri.
	Fungsi_Frame_Kiri=Frame(Fungsi_Utama_Tkinter,bg="#ffffff",bd=0,cursor="crosshair",
		relief=FLAT)
	Fungsi_Frame_Kiri.pack(expand=False,fill=BOTH,side=LEFT)


	Fungsi_Frame_Tengah=Frame(Fungsi_Utama_Tkinter,bg="#ffffff",
		bd=0)
	Fungsi_Frame_Tengah.pack(expand=False,fill=X,side="top")


	def Home_Navbar():
		quit()


	Home_Function=Button(Fungsi_Frame_Kiri,activebackground="#ffffff"
		,activeforeground="#008b8b",bg="#008b8b",
		bd=1,cursor="pirate",font=("Ubuntu",15),fg="#ffffff",
		justify="center",text="Back To Terminal",
		command=Home_Navbar)
	Home_Function.pack(expand=False,side="top",padx=15,pady=15)


	def Program_Jam_GUI():
		Fungsi_Waktu_Python=time.strftime("%Y : %B : %A : %H : %M : %S %p")
		Label_Jam_GUI.config(text=Fungsi_Waktu_Python)
		Label_Jam_GUI.after(1253,Program_Jam_GUI)

	Label_Jam_GUI=Label(Fungsi_Frame_Tengah,font=("Times New Roman",18),
		bg="#ffffff",fg="#008b8b")
	Label_Jam_GUI.pack()
	Program_Jam_GUI()


	# Buka GitHub
	def My_GitHub():
		webbrowser.open("https://github.com/RubenLeonardoSigalingging")


	GitHub=Button(Fungsi_Frame_Kiri,text="See Me On GitHub",activebackground="#ffffff",
		activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",
		font=("Ubuntu",15),justify="center",bd=1,cursor="pirate",
		command=My_GitHub)
	GitHub.pack(expand=False,side=TOP,padx=15,pady=15)


	def PyWhatKit_Tools(Created_By="Ruben Leonardo Sigalingging"):
		import tkinter
		import pywhatkit
		PyWhatKit=Tk()
		PyWhatKit.title("PyWhatKit")
		PyWhatKit.geometry("500x500")
		PyWhatKit.configure(bg="#000000",cursor="crosshair")
		PyWhatKit_Label=Label(PyWhatKit,text="PyWhatKit",
			font=("Times",25,"bold"),bg="#4C4E52",fg="#00A8C9",
			pady=25)
		PyWhatKit_Label.pack(expand=False,side="top",fill="both")


		Nomor_Telepon=Label(PyWhatKit,text="Input Phone Number Of Target With Country Code",
			bg="#008b8b",cursor="crosshair",font=("Ubuntu",15),
			fg="#ffffff",justify=CENTER)
		Nomor_Telepon.pack(expand=False,fill=BOTH,side="top")

		# TOMBOL INPUT Phone number of target with country code.
		Tombol_Input_Nomor_Telepon=Entry(PyWhatKit,bg="#ffffff",
			bd=1,cursor="pirate",font=("Times",15),fg="#008b8b",
			justify=CENTER,width=15)
		Tombol_Input_Nomor_Telepon.pack(expand=False,
			side="top")


		# Message that you want to sendwhatmsg.
		Message=Label(PyWhatKit,text="Input Message That You Want To Send",
			anchor="center",bg="#008b8b",bd=1,cursor="crosshair",
			font=("Ubuntu",15),fg="#ffffff",justify="center",
			padx=1,pady=1,relief="flat",width=15)
		Message.pack(expand=False,fill=BOTH,side="top")

		Tombol_Input_Pesan=Entry(PyWhatKit,bg="#ffffff",
			fg="#008b8b",bd=1,
			cursor="pirate",font=("Times",15),justify="center",
			width=15)
		Tombol_Input_Pesan.pack(expand=False,side="top")


		Hours=Label(PyWhatKit,text="Hours At Which You Want To Send Message In 24 Hour Format",
			anchor="center",bg="#008b8b",bd=1,cursor="crosshair",
			font=("Ubuntu",15),fg="#ffffff",justify="center",
			padx=1,pady=1,relief="flat",width=15)
		Hours.pack(expand=False,fill=BOTH,side="top")

		Tombol_Input_Hours=Entry(PyWhatKit,bg="#ffffff",
			fg="#008b8b",bd=1,
			cursor="pirate",font=("Times",15),justify="center",
			width=15)
		Tombol_Input_Hours.pack(expand=False,side="top")


		Minutes=Label(PyWhatKit,text="Minutes At Which You Want To Send Message",
			anchor="center",bg="#008b8b",bd=1,cursor="crosshair",
			font=("Ubuntu",15),fg="#ffffff",justify="center",
			padx=1,pady=1,relief="flat",width=15)
		Minutes.pack(expand=False,fill=BOTH,side="top")

		Tombol_Input_Minutes=Entry(PyWhatKit,bg="#ffffff",
			fg="#008b8b",bd=1,
			cursor="pirate",font=("Times",15),justify="center",
			width=15)
		Tombol_Input_Minutes.pack(expand=False,side="top")


		String_Var=tkinter.StringVar()
		String_Var.set("~> Send WhatsApp Message!")

		Jam=tkinter.IntVar()
		Jam.set("~> Jam!")

		Menit=tkinter.IntVar()
		Menit.set("~> Menit!")


		def Tombol_Pemroses():
			import tkinter
			import pywhatkit
			Var_Phone_Number=Tombol_Input_Nomor_Telepon.get()
			Var_Phone_Number=str(Var_Phone_Number)

			Var_Message=Tombol_Input_Pesan.get()
			Var_Message=str(Var_Message)

			Var_Hours=Tombol_Input_Hours.get()
			Var_Hours=int(Var_Hours)

			Var_Minutes=Tombol_Input_Minutes.get()
			Var_Minutes=int(Var_Minutes)

			String_Var.set(Var_Phone_Number)
			String_Var.set(Var_Message)
			String_Var.set(int(Var_Hours))
			String_Var.set(int(Var_Minutes))

			send_WhatsApp_message=pywhatkit.sendwhatmsg(Var_Phone_Number,Var_Message,Var_Hours,Var_Minutes)


			Tombol_Input_Nomor_Telepon.config(text=send_WhatsApp_message)
			Tombol_Input_Pesan.config(text=send_WhatsApp_message)
			Tombol_Input_Hours.config(text=send_WhatsApp_message)
			Tombol_Input_Minutes.config(text=send_WhatsApp_message)


			import pyautogui
			send_WhatsApp_message=pyautogui.press("enter")


		def Exit_Program(Created_By="Ruben Leonardo Sigalingging"):
			quit()


		Send_WhatsApp_Message=Button(PyWhatKit,text="Send WhatsApp Message!",
			bd=2,bg="#008b8b",fg="#ffffff",activebackground="#ffffff",
			activeforeground="#008b8b",font=("Ubuntu",15),
			justify="center",command=Tombol_Pemroses)
		Send_WhatsApp_Message.pack(expand=False,fill=BOTH,
			side="top")


		Exit=Button(PyWhatKit,text="Exit Program!",bd=2,bg="#008b8b",
			fg="#ffffff",activebackground="#ffffff",
			activeforeground="#008b8b",font=("Ubuntu",15),justify=CENTER,command=Exit_Program)
		Exit.pack(expand=False,fill="both",side=TOP,pady=30)


	PyWhatKit=Button(Fungsi_Frame_Kiri,text="PyWhatKit Tool",activebackground="#ffffff",
		activeforeground="#008b8b",bd=1,bg="#008b8b",fg="#ffffff",
		font=("Ubuntu",15),justify="center",cursor="pirate",
		command=PyWhatKit_Tools)
	PyWhatKit.pack(expand=False,side="top",padx=15,pady=15)


	def Video_On_YouTube():
		Fungsi_Utama_Playonyt=Tk()
		Fungsi_Utama_Playonyt.title("Search And Play Particular Videos On YouTube")
		Fungsi_Utama_Playonyt.geometry("500x500")
		Fungsi_Utama_Playonyt.configure(bg="#000000",cursor="crosshair")


		Label_YouTube=Label(Fungsi_Utama_Playonyt,text="Play On YouTube",
			font=("Ubuntu",15),cursor="crosshair",bd=1,bg="#008b8b",
			fg="#ffffff",justify="center")
		Label_YouTube.pack(expand=False,fill=BOTH,side="top")


		String_Var=tkinter.StringVar()
		String_Var.set("~> Search And Play A Particular Video On YouTube!")


		Tombol_PlayOnYouTube=Entry(Fungsi_Utama_Playonyt,bg="#ffffff",
			bd=1,cursor="pirate",exportselection=False,fg="#008b8b",
			justify="center",selectbackground="#008b8b",selectforeground="#ffffff",
			width=15,textvariable=String_Var)
		Tombol_PlayOnYouTube.pack(expand=False,side="top",padx=25,pady=25)


		def Tombol_Pemroses_Play_Video_On_YouTube(Created_By="Ruben Leonardo Sigalingging"):
			import pywhatkit
			import pyautogui
			Var_YouTube=Tombol_PlayOnYouTube.get()
			Var_YouTube=str(Var_YouTube)

			String_Var.set(Var_YouTube)

			YouTube=pywhatkit.playonyt(Var_YouTube)

			Tombol_PlayOnYouTube.config(text=YouTube)

			YouTube=pyautogui.press("enter")


		def Exit_Program_Play_On_YouTube(Created_By="Ruben Leonardo Sigalingging"):
				quit()


		Tombol_Button_PlayOnYouTube=Button(Fungsi_Utama_Playonyt,text="Let's Play Video On YouTube!",
			activebackground="#ffffff",activeforeground="#008b8b",bd=1,
			bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),
			justify="center",width=25,command=Tombol_Pemroses_Play_Video_On_YouTube)
		Tombol_Button_PlayOnYouTube.pack(expand=False,side="top",padx=25,pady=25)


		Exit_Program=Button(Fungsi_Utama_Playonyt,text="Exit Program",
			font=("Ubuntu",12),bg="#008b8b",fg="#ffffff",activebackground="#ffffff",
			activeforeground="#008b8b",bd=1,justify="center",width=12,
			command=Exit_Program_Play_On_YouTube)
		Exit_Program.pack(expand=False,side="top",padx=25,pady=25)



	PlayOnYt=Button(Fungsi_Frame_Kiri,text="Play On YouTube",activebackground="#ffffff",
		activeforeground="#008b8b",bd=1,bg="#008b8b",fg="#ffffff",
		font=("Ubuntu",15),justify="center",cursor="pirate",
		command=Video_On_YouTube)
	PlayOnYt.pack(expand=False,side="top",padx=15,pady=15)


	# Google Search Tool


	def Google_Search(Created_By="Ruben Leonardo Sigalingging"):
		Fungsi_Utama_Google_Search_Tool=Tk()
		Fungsi_Utama_Google_Search_Tool.title("Google Search Tool")
		Fungsi_Utama_Google_Search_Tool.geometry("500x500")
		Fungsi_Utama_Google_Search_Tool.configure(bg="#000000",cursor="crosshair")


		String_Var=tkinter.StringVar()
		String_Var.set("~> Google Search Tool")


		Label_Google_Search_Tool=Label(Fungsi_Utama_Google_Search_Tool,text="Google Search Tool",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
		# side = samping, sisi
		# expand = mengembangkan, memperluas
		Label_Google_Search_Tool.pack(expand=False,fill=BOTH,side="top")


		Entry_Google_Search_Tool=Entry(Fungsi_Utama_Google_Search_Tool,
			bg="#008b8b",bd=1,cursor="pirate",exportselection=True,
			fg="#ffffff",justify="center")
		Entry_Google_Search_Tool.pack(expand=False,fill=BOTH,side="top",padx=15,pady=15)


		def Alat_Pencarian_Google(Created_By="Ruben Leonardo Sigalingging"):
			import pyautogui
			Var_Alat_Pencarian_Google=Entry_Google_Search_Tool.get()
			Var_Alat_Pencarian_Google=str(Var_Alat_Pencarian_Google)

			String_Var.set(Var_Alat_Pencarian_Google)

			PyWhatKit_Google_Search=pywhatkit.search(Var_Alat_Pencarian_Google)

			Entry_Google_Search_Tool.config(text=PyWhatKit_Google_Search)

			PyWhatKit_Google_Search=pyautogui.press("enter")


		Button_Google_Search_Tool=Button(Fungsi_Utama_Google_Search_Tool,
			text="~> Google Search Tool!",activebackground="#008b8b",
			activeforeground="#ffffff",
			bd=1,bg="#ffffff",fg="#008b8b",font=("Ubuntu",15),justify="center",
			command=Alat_Pencarian_Google)
		Button_Google_Search_Tool.pack(expand=False,side="top",padx=15,pady=15)



	Google_Search_Tool=Button(Fungsi_Frame_Kiri,text="Google Search Tool",activebackground="#ffffff",
		activeforeground="#008b8b",bd=1,bg="#008b8b",fg="#ffffff",
		font=("Ubuntu",15),justify="center",cursor="pirate",
		command=Google_Search)
	Google_Search_Tool.pack(expand=False,side="top",padx=15,pady=15)


	# My IP Address


	def IP_Address(Created_By="Ruben Leonardo Sigalingging"):
		Fungsi_Utama_IP_Address=Tk()
		Fungsi_Utama_IP_Address.title("My IP Address is:")
		Fungsi_Utama_IP_Address.geometry("900x500")
		Fungsi_Utama_IP_Address.configure(bg="#000000",cursor="crosshair")


		Label_My_IP_Address_Tool=Label(Fungsi_Utama_IP_Address,text="My IP Address : ",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
		Label_My_IP_Address_Tool.pack(expand=False,fill="both",side="top")


		def Internet_Protocol_Address(Created_By="Ruben Leonardo Sigalingging"):
			import requests
			import json

			Label_IP=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")

			try:
				Var_IP=requests.get("https://api.ipify.org/").text
				Data_Alamat_IP=requests.post("https://coding.tools/my-ip-address",data={"queryIp":Var_IP}).text
				Uraikan_Data=json.loads(Data_Alamat_IP)


				Label_IP.config(text="Find IP Location: "+str(Var_IP))
				Label_IP.pack(expand=False,fill="both",
				padx=15,pady=15,side="top")

				Negara=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")

				Negara.config(text="Country: "+str(Uraikan_Data["country_name"]))
				Negara.pack(expand=False,fill=BOTH,side="top",padx=15,pady=15)

				Negara=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")

				Kota=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
				Kota.config(text="City: "+str(Uraikan_Data["city_name"]))
				Kota.pack(expand=False,fill=BOTH,side="top",padx=15,pady=15)

				Region=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
				Region.config(text="Region: "+str(Uraikan_Data["region_name"]))
				Region.pack(expand=False,fill=BOTH,side=TOP,padx=15,pady=15)

				Latitude=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
				Latitude.config(text="Latitude: "+str(Uraikan_Data["latitude"]))
				Latitude.pack(expand=False,fill=BOTH,side=TOP,padx=15,pady=15)

				Zip_Code=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
				Zip_Code.config(text="Zip Code: "+str(Uraikan_Data["zip_code"]))
				Zip_Code.pack(expand=False,fill=BOTH,side=TOP,padx=15,pady=15)

				Time_Zone=Label(Fungsi_Utama_IP_Address,text="My IP Address",
			font=("Ubuntu",25),cursor="pirate",bd=1,bg="#008b8b",fg="#ffffff",
			justify="center")
				Time_Zone.config(text="Time Zone: "+str(Uraikan_Data["timezone"]))
				Time_Zone.pack(expand=False,fill=BOTH,side=TOP,padx=15,pady=15)


			except:
				Label_IP.config(text="Failed To Find Your IP Address!")
				Label_IP.pack(expand=False,fill="both",side="top",padx=15,pady=15)


		Alamat_IP_Saya=Button(Fungsi_Utama_IP_Address,
			text="Check My IP Address",
			activebackground="#008b8b",activeforeground="#ffffff",bg="#ffffff",
			fg="#008b8b",bd=1,font=("Ubuntu",15),justify="center",
			command=Internet_Protocol_Address)
		Alamat_IP_Saya.pack(expand=False,side="top",padx=15,pady=15)


	import sys
	User_Operating_System_Type=sys.platform
	Operating_System=Label(Fungsi_Frame_Tengah,text="User Operating System Detection Tool",
		activebackground="#ffffff",activeforeground="#008b8b",bd=1,
		bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		cursor="pirate")
	Operating_System.config(text="Your OS Type Is: "+str(User_Operating_System_Type))
	Operating_System.pack(expand=False,fill=BOTH,padx=15,pady=15)

	My_IP_Address=Button(Fungsi_Frame_Kiri,text="My IP Address",
		activebackground="#ffffff",activeforeground="#008b8b",bd=1,
		bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		cursor="pirate",command=IP_Address)
	My_IP_Address.pack(expand=False,side="top",padx=15,pady=15)


	def MD5_Hash(Created_By="Ruben Leonardo Sigalingging"):
		import webbrowser
		webbrowser.open("https://coding.tools/md5")


	MD5_Hash_Generator=Button(Fungsi_Frame_Kiri,text="MD5 Hash Generator\nOnline Tool",
		activebackground="#ffffff",activeforeground="#008b8b",bd=1,
		bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		cursor="pirate",command=MD5_Hash)
	MD5_Hash_Generator.pack(expand=False,side="top",padx=15,pady=15)


	def Password_Generator_Tool(Created_By="Ruben Leonardo Sigalingging"):
		Fungsi_Utama_Password_Generator_Tool=Tk()
		Fungsi_Utama_Password_Generator_Tool.title("Password Generator Tool")
		Fungsi_Utama_Password_Generator_Tool.geometry("800x500")
		Fungsi_Utama_Password_Generator_Tool.configure(cursor="crosshair",bg="#000000")


		Label_Password_Generator=Label(Fungsi_Utama_Password_Generator_Tool,text="Password Generator Tool",
			cursor="pirate",justify="center",bg="#008b8b",fg="#ffffff",
			font=("Ubuntu",25))
		Label_Password_Generator.pack(expand=False,fill=BOTH,side="top")


		def Password_Generator_Tool_Function(Created_By="Ruben Leonardo Sigalingging"):
			import string
			import random
			Function_Of_String_Module=string.printable
			Password_Length=12
			Random_Password="".join(random.sample(Function_Of_String_Module,Password_Length))

			Label_Password_Generator=Label(Fungsi_Utama_Password_Generator_Tool,
				bg="#ffffff",fg="#008b8b",font=("Times New Roman",18),justify="center")
			Label_Password_Generator.config(text="Results: "+str(Random_Password))
			Label_Password_Generator.pack(expand=False,fill=BOTH,side="top",padx=12,pady=12)


		Button_Password_Generator=Button(Fungsi_Utama_Password_Generator_Tool,text="Click Here To Generate Random Password!",
			justify="center",activebackground="#ffffff",activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",bd=2,font=("Ubuntu",15),
			command=Password_Generator_Tool_Function)
		Button_Password_Generator.pack(expand=False,fill=BOTH,side="top",padx=25,pady=25)


	Password_Generator=Button(Fungsi_Frame_Kiri,text="Password Generator Tool",
		activebackground="#ffffff",activeforeground="#008b8b",bd=1,
		bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		cursor="pirate",command=Password_Generator_Tool)
	Password_Generator.pack(expand=False,side="top",padx=15,pady=15)


	def Check_Operating_System(Created_By="Ruben Leonardo Sigalingging"):
		Fungsi_Utama_Check_Operating_System=Tk()
		Fungsi_Utama_Check_Operating_System.title("Check Operating System Using Python")
		Fungsi_Utama_Check_Operating_System.geometry("800x500")
		Fungsi_Utama_Check_Operating_System.configure(cursor="pirate",bg="#000000")


		Label_Check_Operating_System=Label(Fungsi_Utama_Check_Operating_System,text="Check My Operating System",
			font=("Ubuntu",25),justify="center",bg="#008b8b",fg="#ffffff")
		Label_Check_Operating_System.pack(expand=False,fill=BOTH,side="top")


		def Functions_Of_The_Operating_System_Checker_Tool(Created_By="Ruben Leonardo Sigalingging"):
			Label_Operating_System=Label(Fungsi_Utama_Check_Operating_System,font=("Times New Roman",15),justify="center",cursor="pirate",bg="#ffffff",fg="#008b8b")
			Label_Operating_System.config(text="Your Operating System Type Is: "+str(sys.platform))
			Label_Operating_System.pack(expand=False,fill=BOTH,side="top",padx=5,pady=5)


			Label_Python_Version=Label(Fungsi_Utama_Check_Operating_System,font=("Times New Roman",15),justify="center",cursor="pirate",bg="#ffffff",fg="#008b8b")
			Label_Python_Version.config(text="Your Python Version Is: "+str(sys.version_info))
			Label_Python_Version.pack(expand=False,fill=BOTH,side="top",padx=5,pady=5)


			Data_Alamat_IP=requests.get("https://api.ipify.org/").text
			Label_IP_Address=Label(Fungsi_Utama_Check_Operating_System,font=("Times New Roman",15),justify="center",cursor="pirate",bg="#ffffff",fg="#008b8b")
			Label_IP_Address.config(text="Your Public IP Address Is: "+str(requests.get("https://api.ipify.org/").text))
			Label_IP_Address.pack(expand=False,fill=BOTH,side="top",padx=5,pady=5)


			Label_Get_Hostname=Label(Fungsi_Utama_Check_Operating_System,font=("Times New Roman",15),justify="center",cursor="pirate",bg="#ffffff",fg="#008b8b")
			Label_Get_Hostname.config(text="Your Host Name: "+str(socket.gethostname()))
			Label_Get_Hostname.pack(expand=False,fill=BOTH,side="top",padx=5,pady=5)


			Label_Get_IP_Address_Information=Label(Fungsi_Utama_Check_Operating_System,font=("Times New Roman",15),justify="center",cursor="pirate",bg="#ffffff",fg="#008b8b")
			Label_Get_Hostname.config(text="Get IP Address Information: "+str(socket.gethostbyaddr(Data_Alamat_IP)))
			Label_Get_Hostname.pack(expand=False,fill=BOTH,side="top",padx=5,pady=5)

		Button_Check_Operating_System=Button(Fungsi_Utama_Check_Operating_System,text="Check My Operating System Type!",bg="#ffffff",fg="#008b8b",activebackground="#008b8b",activeforeground="#ffffff",justify="center",
			font=("Ubuntu",18),bd=2,command=Functions_Of_The_Operating_System_Checker_Tool)
		Button_Check_Operating_System.pack(expand=False,fill=Y,side="top",padx=12,pady=12)
		Fungsi_Utama_Check_Operating_System.mainloop()


	Check_Operating_System_Using_Python=Button(Fungsi_Frame_Tengah,text="Check Operating System\nUsing Python",
		activebackground="#ffffff",activeforeground="#008b8b",bd=1,
		bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		cursor="pirate",command=Check_Operating_System)
	Check_Operating_System_Using_Python.pack(expand=False,side="left",padx=15,pady=15)


	def Password_Generator_Tool(Created_By="Ruben Leonardo Sigalingging"):
		import random
		import string
		Var_Password_Generator_Tool=string.printable
		Fungsi_Utama_Password_Generator=Tk()
		Fungsi_Utama_Password_Generator.title("Password Generator Tool")
		Fungsi_Utama_Password_Generator.geometry("800x500")
		Fungsi_Utama_Password_Generator.configure(cursor="crosshair",bg="#000000")


		Label_Password_Generator=Label(Fungsi_Utama_Password_Generator,text="Password Generator Online Tool",
			bg="#008b8b",fg="#ffffff",cursor="pirate",font=("Ubuntu",25),justify="center")
		Label_Password_Generator.pack(expand=False,fill="both",side="top")


		def Function_Of_Password_Generator(Created_By="Ruben Leonardo Sigalingging"):
			Var_Function_Of_Password_Generator="".join(random.sample(Var_Password_Generator_Tool,k=12))
			Label_Function=Label(Fungsi_Utama_Password_Generator,bg="#008b8b",fg="#ffffff",
				font=("Times New Roman",18),justify="center")
			Label_Function.config(text="Results: "+str(Var_Function_Of_Password_Generator))
			Label_Function.pack(expand=False,fill="x",side="top",padx=5,pady=5)

			
		Button_Password_Generator=Button(Fungsi_Utama_Password_Generator,text="Click Here!",bg="#ffffff",fg="#008b8b",bd=2,font=("Times New Roman",18),activebackground="#008b8b",activeforeground="#ffffff",justify="center",
			command=Function_Of_Password_Generator)
		Button_Password_Generator.pack(expand=False,fill="both",side="top",padx=25,pady=25)

	Password_Generator=Button(Fungsi_Frame_Tengah,text="Password Generator\nTool",bg="#008b8b",
		fg="#ffffff",font=("Ubuntu",15),justify="center",cursor="pirate",bd=2,
		activebackground="#ffffff",activeforeground="#008b8b",command=Password_Generator_Tool)
	Password_Generator.pack(expand=False,side="left",padx=15,pady=15)


	def YouTube_Video_Downloader_Tool_Functions(Created_By="Ruben Leonardo Sigalingging"):
		import pytube
		from pytube import YouTube
		Fungsi_Utama_YouTube_Video_Downloader_Tool=Tk()
		Fungsi_Utama_YouTube_Video_Downloader_Tool.title("YouTube Video Downloader Tool")
		Fungsi_Utama_YouTube_Video_Downloader_Tool.geometry("800x500")
		Fungsi_Utama_YouTube_Video_Downloader_Tool.configure(cursor="crosshair",bg="#000000")


		Judul_YouTube_Video_Downloader_Tool=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,text="YouTube Video Downloader Tool",anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Ubuntu",25),fg="#ffffff",justify="center",relief="flat")
		Judul_YouTube_Video_Downloader_Tool.pack(expand=False,fill="both",side="top")


		String_Var=tkinter.StringVar()
		String_Var.set("~> Input Your YouTube Video Link Here!")


		Entry_YouTube_Video_Downloader_Tool=Entry(Fungsi_Utama_YouTube_Video_Downloader_Tool,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#008b8b",justify="center",relief="flat",state="normal",textvariable=String_Var)
		Entry_YouTube_Video_Downloader_Tool.pack(expand=False,fill="both",side="top",padx=25,pady=25)


		def Downloader_Function(Created_By="Ruben Leonardo Sigalingging"):
			import pytube
			# https://youtu.be/AdHE5Nss4HI
			Get_URL=Entry_YouTube_Video_Downloader_Tool.get()
			URL=Get_URL
			Download_The_Video=pytube.YouTube(URL)

			YouTube_Video_Title_Label=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center")
			YouTube_Video_Title_Label.config(text="Title: "+str(Download_The_Video.title))
			YouTube_Video_Title_Label.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Thumbnails_URL=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center")
			Thumbnails_URL.config(text="Thumbnails URL: "+str(Download_The_Video.thumbnail_url))
			Thumbnails_URL.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Total_Viewed_Function=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center",relief="flat")
			Total_Viewed_Function.config(text="Total Viewed: "+str(Download_The_Video.views))
			Total_Viewed_Function.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Label_Publish_Date=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center",relief="flat")
			Label_Publish_Date.config(text="Publish Date: "+str(Download_The_Video.publish_date))
			Label_Publish_Date.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Keywords_Label=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center",relief="flat")
			Keywords_Label.config(text="Keywords Label: "+str(Download_The_Video.keywords))
			Keywords_Label.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Author_Label=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center",relief="flat")
			Author_Label.config(text="Author Of This Video: "+str(Download_The_Video.author))
			Author_Label.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			Channel_URL=Label(Fungsi_Utama_YouTube_Video_Downloader_Tool,anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify="center",relief="flat")
			Channel_URL.config(text="YouTube Channel URL: "+str(Download_The_Video.channel_url))
			Channel_URL.pack(expand=False,fill="x",side="top",padx=5,pady=5)


			# get highest resolution = dapatkan resolusi tertinggi
			Download_The_Video=Download_The_Video.streams.get_highest_resolution()
			Download_The_Video.download()


		Button_YouTube_Video_Downloader_Tool=Button(Fungsi_Utama_YouTube_Video_Downloader_Tool,text="Let's Download This Video!",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Times New Roman",15),justify="center",state="normal",cursor="pirate",command=Downloader_Function)
		Button_YouTube_Video_Downloader_Tool.pack(expand=False,fill="both",side="top",padx=25,pady=25)


	YouTube_Downloader_Tool=Button(Fungsi_Frame_Tengah,text="YouTube Video\nDownloader Tool",bg="#008b8b",fg="#ffffff",bd=2,
		font=("Ubuntu",15),justify="center",cursor="pirate",activebackground="#ffffff",activeforeground="#008b8b",command=YouTube_Video_Downloader_Tool_Functions)
	YouTube_Downloader_Tool.pack(expand=False,side="left",padx=15,pady=15)


	Fungsi_Frame_Kiri_Bawah=Frame(Fungsi_Utama_Tkinter,bg="#ffffff",cursor="crosshair")
	Fungsi_Frame_Kiri_Bawah.pack(expand=False,fill="both",side="top")


	def The_First_Function_Of_MD5_Hash_Generator(Created_By="Ruben Leonardo Sigalingging"):
		First_Function=Tk()
		First_Function.title("MD5 Hash Generator Offline Tool")
		First_Function.geometry("800x500")
		First_Function.configure(cursor="crosshair",bg="#000000")


		Label_MD5_Hash_Generator=Label(First_Function,text="MD5 Hash Generator Offline Tool",anchor="center",bg="#008b8b",bd=2,cursor="pirate",font=("Ubuntu",25),fg="#ffffff",justify="center",relief="flat")
		Label_MD5_Hash_Generator.pack(expand=False,fill="both",side="top")


		Entry_MD5_Hash_Generator_Offline_Tool=Entry(First_Function,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",18),justify="center",relief="flat",state="normal",fg="#008b8b")
		Entry_MD5_Hash_Generator_Offline_Tool.pack(expand=False,fill="both",side="top",padx=25,pady=25)


		def Second_Function(Created_By="Ruben Leonardo Sigalingging"):
			Get_Entry_Button=Entry_MD5_Hash_Generator_Offline_Tool.get()
			MD5_Code=hashlib.md5()
			MD5_Code.update(Get_Entry_Button.encode("ascii"))


			MD5_Encryption_Result_Label=Label(First_Function,bg="#ffffff",bd=2,fg="#008b8b",font=("Times New Roman",18),justify="center",cursor="pirate",anchor="center")
			MD5_Encryption_Result_Label.config(text="MD5 Encryption Results: "+str(MD5_Code.hexdigest()))
			MD5_Encryption_Result_Label.pack(expand=False,fill="both",side="top",padx=25,pady=25)


		Button_MD5_Hash_Generator=Button(First_Function,text="Let's Encrypt MD5!",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Times New Roman",18),justify="center",command=Second_Function)
		Button_MD5_Hash_Generator.pack(expand=False,fill="both",side="top",padx=15,pady=15)


	MD5_Hash_Generator_Online_Tool=Button(Fungsi_Frame_Kiri_Bawah,text="MD5 Hash Generator\nOffline Tool",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",cursor="pirate",command=The_First_Function_Of_MD5_Hash_Generator)
	MD5_Hash_Generator_Online_Tool.pack(expand=False,fill="both",side="left",padx=15,pady=15)


	def Message_Box_From_Me(Created_By="Ruben Leonardo Sigalingging"):
		import random
		from tkinter import messagebox

		List_Words=["You can have anything you want if you want it badly enough. You can be anything you want to be, do anything you set out to accomplish if you hold to that desire with singleness of purpose.",
		"Anda dapat memiliki apa pun yang Anda inginkan jika Anda sangat menginginkannya. Anda bisa menjadi apa pun yang Anda inginkan, melakukan apa pun yang ingin Anda capai jika Anda berpegang pada keinginan itu dengan satu tujuan.",
		"Knowing is not enough; we must apply. Willing is not enough; we must do.",
		"Mengetahui saja tidak cukup; kita harus melamar. Bersedia tidak cukup; harus kita lakukan.",
		"Do you want to know who you are? Don't ask. Act! Action will delineate and define you.",
		"Apakah Anda ingin tahu siapa Anda? Jangan tanya. Bertindak! Tindakan akan menggambarkan dan mendefinisikan Anda.","The path to success is to take massive, determined actions","Ambition is the path to success. Persistence is the vehicle you arrive in.","Ambition is enthusiasm with a purpose.","Ambisi adalah antusiasme dengan tujuan.","A man’s worth is no greater than his ambitions.","Nilai seorang pria tidak lebih besar dari ambisinya.","Believe it can be done. When you believe something can be done, really believe, your mind will find the ways to do it. Believing a solution paves the way to solution.","Percaya itu bisa dilakukan. Ketika Anda percaya sesuatu dapat dilakukan, benar-benar percaya, pikiran Anda akan menemukan cara untuk melakukannya. Percaya pada solusi membuka jalan menuju solusi.","Be brave to stand for what you believe in even if you stand alone.","Berani untuk membela apa yang Anda yakini bahkan jika Anda berdiri sendiri.","Clarity precedes success.","Kejelasan mendahului kesuksesan","A lack of clarity could put the brakes on any journey to success.","Kurangnya kejelasan dapat mengerem setiap perjalanan menuju kesuksesan.","The ultimate measure of a man is not where he stands in moments of comfort and convenience, but where he stands at times of challenge and controversy.","Ukuran tertinggi seorang pria bukanlah di mana dia berdiri di saat-saat nyaman dan nyaman, tetapi di mana dia berdiri pada saat-saat tantangan dan kontroversi.","The key to life is accepting challenges. Once someone stops doing this, he’s dead.","Kunci hidup adalah menerima tantangan. Begitu seseorang berhenti melakukan ini, dia mati.",
		"When you delete something, you’re making a choice to destroy it. To never see it again.","Saat Anda menghapus sesuatu, Anda membuat pilihan untuk menghancurkannya. Untuk tidak pernah melihatnya lagi.","I'm gonna fix the world I broke, and put it back together better than it was before.","Saya akan memperbaiki dunia yang saya hancurkan, dan menyatukannya kembali lebih baik dari sebelumnya.","Deletion. When you make that decision, there's always that moment of hesitation. That annoying 'Are you sure?' dialogue box, and then you have to make a decision. Yes or no.","Penghapusan. Ketika Anda membuat keputusan itu, selalu ada momen keragu-raguan. 'Apakah Anda yakin?' kotak dialog, dan kemudian Anda harus membuat keputusan. Ya atau tidak.","I don't want your proof. I want your belief.","Saya tidak ingin bukti Anda. Saya ingin kepercayaan Anda.","Every relationship is a power struggle. Some of us need to be controlled.","Setiap hubungan adalah perebutan kekuasaan. Beberapa dari kita perlu dikendalikan.","Control can sometimes be an illusion. But sometimes you need illusions to gain control. Fantasy is an easy way to give meaning to world. To cloak our harsh reality with escapist comfort. After all, isn't that why we surround ourselves with so many screens? So we can avoid seeing? So we can avoid each other? So we can avoid truth.","Kontrol terkadang bisa menjadi ilusi. Tetapi terkadang Anda membutuhkan ilusi untuk mendapatkan kendali. Fantasi adalah cara mudah untuk memberi makna pada dunia. Untuk menyelubungi kenyataan pahit kita dengan kenyamanan pelarian. Lagi pula, bukankah itu sebabnya kita mengelilingi diri kita dengan begitu banyak layar? Jadi kita bisa menghindari melihat? Jadi kita bisa saling menghindari? Jadi kita bisa menghindari kebenaran.",
		"I love you for all that you are, all that you have been and all that you’re yet to be.","Aku mencintaimu apa adanya, semua yang pernah ada dan yang belum.","I'm so grateful I get to love you.","Aku sangat bersyukur bisa mencintaimu.","I love you more than I could ever really say.","Aku mencintaimu lebih dari yang bisa aku katakan.","Have I mentioned how lucky I am to love you?","Sudahkah saya menyebutkan betapa beruntungnya saya mencintaimu?",
		"When you fall in love with someone’s personality, everything about them becomes beautiful.","Ketika Anda jatuh cinta dengan kepribadian seseorang, segala sesuatu tentang mereka menjadi indah.","I fancy the way your eyes shine when you smile.","Saya suka cara mata Anda bersinar ketika Anda tersenyum."]

		Random_Motivation=random.choice(List_Words)


		messagebox.showinfo(title="Message Box From Me:",message=Random_Motivation)


	Message_Box=Button(Fungsi_Frame_Kiri_Bawah,text="Message Box",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",command=Message_Box_From_Me)
	Message_Box.pack(expand=False,fill="both",side="left",padx=15,pady=15)


	def URL_Encode_Tool(Created_By="Ruben Leonardo Sigalingging"):
		Function_Of_URL_Encode=Tk()
		Function_Of_URL_Encode.title("URL Encode Tool")
		Function_Of_URL_Encode.geometry("800x500")
		Function_Of_URL_Encode.configure(bg="#000000",cursor="crosshair")


		Judul_URL_Encode=Label(Function_Of_URL_Encode,text="URL Encode Online Tool",bg="#008b8b",fg="#ffffff",cursor="pirate",bd=2,font=("Ubuntu",25),justify="center")
		Judul_URL_Encode.pack(expand=False,fill="both",side="top")


		Entry_Button_Of_URL_Encode=Entry(Function_Of_URL_Encode,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#008b8b",justify="center",state="normal")
		Entry_Button_Of_URL_Encode.pack(expand=False,fill="x",side="top",padx=25,pady=25)


		def Main_Function(Created_By="Ruben Leonardo Sigalingging"):
			Get_Entry_Button_Of_URL_Encode=Entry_Button_Of_URL_Encode.get()
			URL_Encryption=urllib.parse.quote_plus(Get_Entry_Button_Of_URL_Encode)
			print(URL_Encryption)

			Result_Label=Label(Function_Of_URL_Encode,anchor="center",bg="#ffffff",fg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),justify="center")
			Result_Label.config(text="Encrypted URL: "+str(URL_Encryption))
			Result_Label.pack(expand=False,fill="x",side="top",padx=25,pady=25)


		Button_Of_URL_Encode_Tool=Button(Function_Of_URL_Encode,text="URL Encode Tool",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Times New Roman",18),height=2,justify="center",
			command=Main_Function)
		Button_Of_URL_Encode_Tool.pack(expand=False,fill="x",side="top",padx=25,pady=25)


	URL_Encode_Online_Tool=Button(Fungsi_Frame_Kiri_Bawah,text="URL Encode\nOnline Tool",activebackground="#ffffff",activeforeground="#008b8b",bd=2,bg="#008b8b",fg="#ffffff",font=("Ubuntu",15),justify="center",
		command=URL_Encode_Tool)
	URL_Encode_Online_Tool.pack(expand=False,fill="both",side="left",padx=15,pady=15)

	# Buat program GUI ini berjalan terus, dengan metode .mainloop()
	Fungsi_Utama_Tkinter.mainloop()


Filipi()
# Learning Computer Science Is So Fun!
# Remember: Don't Give Up And Keep It Up!
# Believe You Can Do It!