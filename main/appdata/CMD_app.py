from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ctypes
import sys
from configparser import ConfigParser

root = Tk()
root.title('CMD')
root.geometry('500x400')
root.attributes("-fullscreen", True)
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
config = ConfigParser()
config.read('main/savedata/savefile.ini')



if config['DEFAULT']['entered_desktop_without_perms'] == 'True':
	MsgBox1 = messagebox.showwarning('You didnt enter the password', 'Enter the password', icon = 'warning')
	root.destroy()

def center_window(w=500, h=400):
	# get screen width and height
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	# calculate position x, y
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))




def retrieve_input(event):
	global input_entry, prew_commands
	result = input_entry.get()
	prew_commands.insert(END, f'<:{result}')
	if result == 'help':
		prew_commands.insert(END, f'Here is a list of default commands:')
		prew_commands.insert(END, f'clear - clears the commands')
		prew_commands.insert(END, f'quit - quits the CMD')
	elif result == 'clear':
			prew_commands.delete(0, END)
	elif result == 'quit':
		quit()
	else:
		prew_commands.insert(END, f'<:Unrecognized command.')
	input_entry.delete(0, END)

def quit():
	root.destroy()


main = Frame()

quitcmd = Button(width=2, height=1, text='X', bg='Red', command=quit)
prew_commands = Listbox(main, width=100, height=17)
input_entry = Entry(main, width=100)

quitcmd.pack(anchor=E)
main.pack(expand=True)
prew_commands.pack()
input_entry.pack()

center_window(500, 300)

root.bind('<Return>', retrieve_input)
root.mainloop()