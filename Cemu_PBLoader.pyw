from tkinter import DISABLED, PhotoImage, StringVar, Tk, Toplevel, messagebox
import tkinter
from tkinter.ttk import *
from tkinter import ttk
import os
import os.path
import shutil
import sys
import webbrowser

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

master = Tk()
master.geometry('200x200')
master.title('Cemu Private Battle Loader')
master.resizable(False, False)
iconPath = resource_path('img\\icon.ico')
master.iconbitmap(iconPath)
showmsgbox = True

if showmsgbox == True:
	tkinter.messagebox.showinfo(title='Note', message='Place this app in the same folder where the Cemu executable (Cemu.exe) and the memorySearcher folder is located at, or else this program will fail to work.')

if showmsgbox == True:
	tkinter.messagebox.showwarning(title='Warning', message='If you already have a memory searcher file containing addresses you do not want to lose, make a backup of it because this program might wipe the file.')

def settingdone():
	if showmsgbox == True:
    		tkinter.messagebox.showinfo(title='Proccess Finished', message='The map has been set, open memory searcher on Cemu and keep it open so the map can load, you can now make a private battle room and play.')


current_map = tkinter.StringVar()
current_reg = tkinter.StringVar()

mapmenu = ttk.Combobox(master, textvariable=current_map,width=17)
mapmenu.place(x=3,y=3)
mapmenu['values'] = ("Octotrooper Hideout", "Lair of the Octoballs", "Rise of the Octocopters", "Gusher Gauntlet", "Floating Sponge Garden", "Propeller-Lift Playground", "Spreader Splatfest", "Octoling Invasion", "Unidentified Flying Object", "Inkrail Skyscape", "Inkvisible Avenues", "Flooder Junkyard", "Shifting Splatforms", "Octoling Assault", "Undeniable Flying Object", "Propeller-Lift Fortress", "Octosniper Ramparts", "Spinning Spreaders", "Tumbling Splatforms", "Octoling Uprising", "Unwelcome Flying Object", "Splat-Switch Revolution", "Spongy Observatory", "Pinwheel Power Plant", "Far-Flung Flooders", "Octoling Onslaught", "Unavoidable Flying Object", "The Mighty Octostomp", "The Dreaded Octonozzle", "The Rampaging Octowhirl", "The Ravenous Octomaw", "Enter the Octobot King", "Urchin Underpass (Dojo)", "Walleye Warehouse (Dojo)", "Saltspray Rig (Dojo)", "Arowana Mall (Dojo)", "Blackbelly Skatepark (Dojo)", "Plaza", "Octo Valley", "Tutorial(1)", "Tutorial(2)", "Shooting Range")
mapmenu['state'] = 'readonly'
regionmenu = ttk.Combobox(master, textvariable=current_reg,width=5)
regionmenu.place(x=143,y=3)
regionmenu['values'] = ('USA', 'EUR', 'JPN')
regionmenu['state'] = 'readonly'
	

def openaboutwindow():
	aboutWindow = Toplevel(master)
	aboutWindow.title('About')
	aboutWindow.geometry('200x200')
	aboutWindow.iconbitmap(iconPath)
	closeaboutWindowbtn = Button(aboutWindow, text='Exit', command=lambda: quit(aboutWindow),width=5)
	closeaboutWindowbtn.place(x=5,y=170)
	def githublink():
		webbrowser.open('https://github.com/token-canary/Cemu_PrivateBattleLoader')
	githublinkbtn = Button(aboutWindow, text='Github Repo', command=githublink,width=12)
	githublinkbtn.place(x=46,y=170)
	aboutText = Label(aboutWindow, text='Allows users playing Splatoon with \nCemu to go on maps meant for \nsingle-player in private battles.\n\nMade by TOKEN-CANARY')
	aboutText.place(x=0,y=0)
	iconimg = PhotoImage(file=resource_path('img\\iconsmall.png'))
	iconimglabel = Label(aboutWindow, image=iconimg)
	iconimglabel.place(x=5,y=100)
	aboutWindow.mainloop()

def quit(window):
	window.destroy()

def selectregion():
	region = current_reg.get()
	if region == 'USA':
		print('Selected USA')
		selectmap()
	elif region == 'EUR':
		print('Selected EUR')
		selectmap()
	elif region == 'JPN':
		print('Selected JPN')
		selectmap()
	else:
		print('Region not selected')
		if showmsgbox == True:
			tkinter.messagebox.showerror(title='Error', message='You did not set a region.')

def selectregionforwipe():
	region = current_reg.get()
	if region == 'USA':
		print('Selected USA')
		wipeaddresses()
	elif region == 'EUR':
		print('Selected EUR')
		wipeaddresses()
	elif region == 'JPN':
		print('Selected JPN')
		wipeaddresses()
	else:
		print('Region not selected')
		if showmsgbox == True:
			tkinter.messagebox.showerror(title='Error', message='You did not set a region.')

def wipeaddresses():
	os.chdir(r'memorySearcher/')
	region = current_reg.get()
	if showmsgbox == True:
		tkinter.messagebox.showinfo(title='Before Starting', message='Close the Memory Searcher window if it is open.')
	if region == 'USA':
		with open('0005000010176900.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				with open('0005000010176900.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
					return
			if not '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
					fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
					with open('0005000010176900.ini', 'w+') as filewrite:
						filewrite.write(fileread)
						os.chdir(r'../')
						if showmsgbox == True:
							tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
						return
				else:
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
					return
					
			# if '''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				# fileread2 = fileread.replace('''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				# with open('0005000010176900.ini', 'w+') as filewrite:
					# filewrite.write(fileread2)
					# if showmsgbox == True:
						# tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
			else:
				os.chdir(r'../')
				if showmsgbox == True:
					tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
	elif region == 'EUR':
		with open('0005000010176a00.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				with open('0005000010176a00.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
					return
			if not '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
					fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
					with open('0005000010176a00.ini', 'w+') as filewrite:
						filewrite.write(fileread)
						os.chdir(r'../')
						if showmsgbox == True:
							tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
						return
				else:
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
					return
					
			# if '''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				# fileread2 = fileread.replace('''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				# with open('0005000010176a00.ini', 'w+') as filewrite:
					# filewrite.write(fileread2)
					# if showmsgbox == True:
						# tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
			else:
				os.chdir(r'../')
				if showmsgbox == True:
					tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
	elif region == 'JPN':
		with open('0005000010162b00.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				with open('0005000010162b00.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
					return
			if not '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
					fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
					with open('0005000010162b00.ini', 'w+') as filewrite:
						filewrite.write(fileread)
						os.chdir(r'../')
						if showmsgbox == True:
							tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
						return
				else:
					os.chdir(r'../')
					if showmsgbox == True:
						tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
					return
					
			# if '''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				# fileread2 = fileread.replace('''\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '\n')
				# with open('0005000010162b00.ini', 'w+') as filewrite:
					# filewrite.write(fileread2)
					# if showmsgbox == True:
						# tkinter.messagebox.showinfo(title='Changes removed', message='Removal successful!')
			else:
				os.chdir(r'../')
				if showmsgbox == True:
					tkinter.messagebox.showerror(title='Error', message='''Address not found, perhaps you already removed it before.''')
def selectmap():
	currentmap = current_map.get()
	if currentmap == "Octotrooper Hideout":
		valuemap = 1001
		writeaddress(valuemap)
	elif currentmap == "Lair of the Octoballs":
		valuemap = 1002
		writeaddress(valuemap)
	elif currentmap == "Rise of the Octocopters":
		valuemap = 1003
		writeaddress(valuemap)
	elif currentmap == "Gusher Gauntlet":
		valuemap = 1004
		writeaddress(valuemap)
	elif currentmap == "Floating Sponge Garden":
		valuemap = 1005
		writeaddress(valuemap)
	elif currentmap == "Propeller-Lift Playground":
		valuemap = 1006
		writeaddress(valuemap)
	elif currentmap == "Spreader Splatfest":
		valuemap = 1007
		writeaddress(valuemap)
	elif currentmap == "Octoling Invasion":
		valuemap = 1008
		writeaddress(valuemap)
	elif currentmap == "Unidentified Flying Object":
		valuemap = 1009
		writeaddress(valuemap)
	elif currentmap == "Inkrail Skyscape":
		valuemap = 1010
		writeaddress(valuemap)
	elif currentmap == "Inkvisible Avenues":
		valuemap = 1011
		writeaddress(valuemap)
	elif currentmap == "Flooder Junkyard":
		valuemap = 1012
		writeaddress(valuemap)
	elif currentmap == "Shifting Splatforms":
		valuemap = 1013
		writeaddress(valuemap)
	elif currentmap == "Octoling Assault":
		valuemap = 1014
		writeaddress(valuemap)
	elif currentmap == "Undeniable Flying Object":
		valuemap = 1015
		writeaddress(valuemap)
	elif currentmap == "Propeller-Lift Fortress":
		valuemap = 1016
		writeaddress(valuemap)
	elif currentmap == "Octosniper Ramparts":
		valuemap = 1017
		writeaddress(valuemap)
	elif currentmap == "Spinning Spreaders":
		valuemap = 1018
		writeaddress(valuemap)
	elif currentmap == "Tumbling Splatforms":
		valuemap = 1019
		writeaddress(valuemap)
	elif currentmap == "Octoling Uprising":
		valuemap = 1020
		writeaddress(valuemap)
	elif currentmap == "Unwelcome Flying Object":
		valuemap = 1021
		writeaddress(valuemap)
	elif currentmap == "Splat-Switch Revolution":
		valuemap = 1022
		writeaddress(valuemap)
	elif currentmap == "Spongy Observatory":
		valuemap = 1023
		writeaddress(valuemap)
	elif currentmap == "Pinwheel Power Plant":
		valuemap = 1024
		writeaddress(valuemap)
	elif currentmap == "Far-Flung Flooders":
		valuemap = 1025
		writeaddress(valuemap)
	elif currentmap == "Octoling Onslaught":
		valuemap = 1026
		writeaddress(valuemap)
	elif currentmap == "Unavoidable Flying Object":
		valuemap = 1027
		writeaddress(valuemap)
	elif currentmap == "The Mighty Octostomp":
		valuemap = 1101
		writeaddress(valuemap)
	elif currentmap == "The Dreaded Octonozzle":
		valuemap = 1102
		writeaddress(valuemap)
	elif currentmap == "The Rampaging Octowhirl":
		valuemap = 1103
		writeaddress(valuemap)
	elif currentmap == "The Ravenous Octomaw":
		valuemap = 1104
		writeaddress(valuemap)
	elif currentmap == "Enter the Octobot King":
		valuemap = 1105
		writeaddress(valuemap)
	elif currentmap == "Urchin Underpass (Dojo)":
		valuemap = 2000
		writeaddress(valuemap)
	elif currentmap == "Walleye Warehouse (Dojo)":
		valuemap = 2001
		writeaddress(valuemap)
	elif currentmap == "Saltspray Rig (Dojo)":
		valuemap = 2002
		writeaddress(valuemap)
	elif currentmap == "Arowana Mall (Dojo)":
		valuemap = 2003
		writeaddress(valuemap)
	elif currentmap == "Blackbelly Skatepark (Dojo)":
		valuemap = 2004
		writeaddress(valuemap)
	elif currentmap == "Plaza":
		valuemap = 3000
		writeaddress(valuemap)
	elif currentmap == "Octo Valley":
		valuemap = 3100
		writeaddress(valuemap)
	elif currentmap == "Tutorial(1)":
		valuemap = 3200
		writeaddress(valuemap)
	elif currentmap == "Tutorial(2)":
		valuemap = 3210
		writeaddress(valuemap)
	elif currentmap == "Shooting Range":
		valuemap = 3300
		writeaddress(valuemap)
	else:
		print('Map not selected')
		if showmsgbox == True:
			tkinter.messagebox.showerror(title='Error', message='You did not set a map.')
			


def backupini():
	region = current_reg.get()
	os.chdir(r'memorySearcher/')
	if region == 'USA':
		shutil.copy('0005000010176900.ini', '000500010176900.ini.bak')
		print('Backup Successful')
		if showmsgbox == True:
			tkinter.messagebox.showinfo(title='Backup finished', message='Backup successful')
			os.chdir(r'../')
	elif region == 'EUR':
		shutil.copy('0005000010176a00.ini', '000500010176a00.ini.bak')
		print('Backup Successful')
		if showmsgbox == True:
			tkinter.messagebox.showinfo(title='Backup finished', message='Backup successful')
			os.chdir(r'../')
	elif region == 'JPN':
		shutil.copy('0005000010162b00.ini', '0005000010162b00.ini.bak')
		print('Backup Successful')
		if showmsgbox == True:
			tkinter.messagebox.showinfo(title='Backup finished', message='Backup successful')
			os.chdir(r'../')
	else:
		print('Region not selected')
		if showmsgbox == True:
			tkinter.messagebox.showerror(title='Error', message='You did not set a region.')
			os.chdir(r'../')

def writeaddress(value):
	os.chdir(r'memorySearcher/')
	region = current_reg.get()
	teamalpha = current_alpha.get()
	if showmsgbox == True:
		tkinter.messagebox.showinfo(title='Before Starting', message='Close the Memory Searcher window if it is open.')
	if region == 'USA':
		with open('0005000010176900.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value) + "\n")
				with open('0005000010176900.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					pass
					if teamalpha == 'on':
						with open('0005000010176900.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
								return
							else:
								with open ('0005000010176900.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
									return
					else:
						os.chdir(r'../')
						settingdone()
						return
			else:
				with open('0005000010176900.ini', 'a+') as fileappend:
					fileappend.write('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value))
					if teamalpha == 'on':
						with open('0005000010176900.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
							else:
								with open ('0005000010176900.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
					else:
						os.chdir(r'../')
						settingdone()
	elif region == 'EUR':
		with open('0005000010176a00.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value) + "\n")
				with open('0005000010176a00.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					if teamalpha == 'on':
						with open('0005000010176a00.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
							else:
								with open ('0005000010176a00.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
					else:
						os.chdir(r'../')
						settingdone()
			else:
				with open('0005000010176a00.ini', 'a+') as fileappend:
					fileappend.write('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value))
					if teamalpha == 'on':
						with open('0005000010176a00.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
							else:
								with open ('0005000010176a00.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
					else:
						os.chdir(r'../')
						settingdone()
	elif region == 'JPN':
		with open('0005000010162b00.ini', 'r+') as file:
			fileread = file.read()
			if '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' in fileread:
				fileread = fileread.replace('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''', '''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value) + "\n")
				with open('0005000010162b00.ini', 'w+') as filewrite:
					filewrite.write(fileread)
					if teamalpha == 'on':
						with open('0005000010162b00.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
							else:
								with open ('0005000010162b00.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
					else:
						os.chdir(r'../')
						settingdone()
			else:
				with open('0005000010162b00.ini', 'a+') as fileappend:
					fileappend.write('''\n\n[Entry]\ndescription=Stage Selector (PB)\naddress=0x1bd04ac8\ntype=int16\nvalue=''' + str(value))
					if teamalpha == 'on':
						with open('0005000010162b00.ini', 'r+') as file:
							fileread = file.read()
							if '''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0''' in fileread:
								file.close()
								os.chdir(r'../')
								settingdone()
							else:
								with open ('0005000010162b00.ini', 'a+') as alphaappend:
									alphaappend.write('''\n\n[Entry]\ndescription=Player1Team\naddress=0x1bd04aca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player2Team\naddress=0x1bd04acc\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player3Team\naddress=0x1bd04bca\ntype=int16\nvalue=0\n\n[Entry]\ndescription=Player4Team\naddress=0x1bd04bcc\ntype=int16\nvalue=0''')
									os.chdir(r'../')
									settingdone()
					else:
						os.chdir(r'../')
						settingdone()
	else:
		print('Region not selected')
		if showmsgbox == True:
			tkinter.messagebox.showerror(title='Error', message='You did not set a region.')
			os.chdir(r'../')

mapidstring = StringVar()

defimg = PhotoImage()
mapimagelabel = Label(master, image=defimg)
mapimagelabel.place(x=75,y=40)

# aboutbtn = Button(master, text='About', width=7, command=openaboutwindow)
# aboutbtn.place(x=5,y=120)

mapid = Label(master, textvariable=mapidstring).place(x = 3, y = 25)  
mapbtn = Button(master, text='Select Map', command=selectregion)
mapbtn.place(x=5,y=120)

wipebtn = Button(master, text='Wipe Changes', command=selectregionforwipe)
wipebtn.place(x=5,y=145)

bakbtn = Button(master, text='MemorySearcher Backup', command=backupini)
bakbtn.place(x=5,y=170)

verlabel = Button(master, text='v2.0.1', command=openaboutwindow,width=5)
verlabel.place(x=157,y=170)

current_alpha = tkinter.StringVar()
alphacheckbox = ttk.Checkbutton(master, text="Set First\n4 Players\n to Alpha", variable=current_alpha, onvalue='on',offvalue='off') #, state=DISABLED)
alphacheckbox.place(x=5,y=70)

def map_changed(e):
	currentmap = current_map.get()
	if currentmap == "Octotrooper Hideout":
		valuemap = 1001
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Lair of the Octoballs":
		valuemap = 1002
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Rise of the Octocopters":
		valuemap = 1003
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Gusher Gauntlet":
		valuemap = 1004
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Floating Sponge Garden":
		valuemap = 1005
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Propeller-Lift Playground":
		valuemap = 1006
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Spreader Splatfest":
		valuemap = 1007
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octoling Invasion":
		valuemap = 1008
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Unidentified Flying Object":
		valuemap = 1009
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Inkrail Skyscape":
		valuemap = 1010
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Inkvisible Avenues":
		valuemap = 1011
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Flooder Junkyard":
		valuemap = 1012
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Shifting Splatforms":
		valuemap = 1013
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octoling Assault":
		valuemap = 1014
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Undeniable Flying Object":
		valuemap = 1015
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Propeller-Lift Fortress":
		valuemap = 1016
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octosniper Ramparts":
		valuemap = 1017
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Spinning Spreaders":
		valuemap = 1018
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Tumbling Splatforms":
		valuemap = 1019
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octoling Uprising":
		valuemap = 1020
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Unwelcome Flying Object":
		valuemap = 1021
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Splat-Switch Revolution":
		valuemap = 1022
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Spongy Observatory":
		valuemap = 1023
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Pinwheel Power Plant":
		valuemap = 1024
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Far-Flung Flooders":
		valuemap = 1025
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octoling Onslaught":
		valuemap = 1026
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Unavoidable Flying Object":
		valuemap = 1027
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "The Mighty Octostomp":
		valuemap = 1101
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "The Dreaded Octonozzle":
		valuemap = 1102
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "The Rampaging Octowhirl":
		valuemap = 1103
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "The Ravenous Octomaw":
		valuemap = 1104
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Enter the Octobot King":
		valuemap = 1105
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Urchin Underpass (Dojo)":
		valuemap = 2000
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Walleye Warehouse (Dojo)":
		valuemap = 2001
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Saltspray Rig (Dojo)":
		valuemap = 2002
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Blackbelly Skatepark (Dojo)":
		valuemap = 2004
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Arowana Mall (Dojo)":
		valuemap = 2003
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Plaza":
		valuemap = 3000
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Octo Valley":
		valuemap = 3100
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Tutorial(1)":
		valuemap = 3200
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Tutorial(2)":
		valuemap = 3210
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3
	elif currentmap == "Shooting Range":
		valuemap = 3300
		mapidstring.set('ID: ' + str(valuemap))
		if os.path.exists(resource_path('img\\' + str(valuemap) + '.png')):
			img2 = PhotoImage(file=resource_path('img\\' + str(valuemap) + '.png'))
			mapimagelabel.configure(image=img2)
			mapimagelabel.image = img2
		else:
			img3 = PhotoImage(file=resource_path('img\\placeholder.png'))
			mapimagelabel.configure(image=img3)
			mapimagelabel.image = img3

mapmenu.bind('<<ComboboxSelected>>', map_changed)

master.mainloop()