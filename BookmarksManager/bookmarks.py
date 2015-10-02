#!/usr/bin/python

import webbrowser
from Tkinter import *
import tkMessageBox
from tkMessageBox import *
import Tkinter

print 'Copyright  attributed to Jeffrey Macharia'


#Creating the top level components
#......................................................................................
root=Tk()
labelfont=('times',25,'bold')
widget=Label(root,text='Manage Your Bookmarks')
widget.config(bg='black',fg='blue',font=labelfont,height=4,width=25)
widget.pack(expand=YES,fill=BOTH)

lb=Label(root,text='Enter your new Bookmark below')
lb.config(fg='blue',font=('times',12,'italic'))
lb.pack(expand=YES,fill=BOTH)



#function for checking if your bookmark exists in the bookmark files
#.............................................................................................
def getter():
	g=en.get()
	with open('bkm','a+r') as book:
		if g in  book.read():
                	showinfo("Duplicate","site already exists in your bookmarks")
			book.close()
        	else:
                	book.write((g+'\n'))
			showinfo('Succesful','%s successfuly added to your bookmarks'%g)
			book.close()



#function for checking if the site url starts with the http or https protocol definition			
def run():
	h=en.get()
	if h.startswith('http'):
		webbrowser.open(h)
	else:
		showinfo('Erro inf','Invalid url syntax ... start with http....')

from dialog import showinfo as show



#...................................................................
en=Entry(root)
en.focus()
en.bind('<Return>', (lambda event: getter()))
en.pack(expand=YES,fill=BOTH)



#...function to create the customized dialog boxes
def dialog():
        win=Toplevel()

	lb3=Label(win,text='Click next to show the list of your Bookmarks')
        lb3.config(fg='blue',font=('times',12,'italic'))
        lb3.pack(expand=YES,fill=BOTH)


	en4=Entry(win)
        en4.focus()
        en4.bind('<Return>', (lambda event: getter()))
	def nxt():
		with open('bkm','r') as bookd:
			for value in bookd.readlines():
				r=showinfo('Bookmarks',value)
				o=askyesno('Bookmarks','run current bookmark')
					
				if o:
					webbrowser.open(value.strip('\n'))					
								



        
	def run2():
		ul=en4.get()
		if ul.startswith('http'):
			webbrowser.open(ul)
		else:
			oo=showinfo("Error","Malformed url....start with http...")

        Button(win,text='Run',command=run2).pack(side=LEFT)
	en4.pack(expand=YES,fill=BOTH)
	Button(win,text='Next',command=nxt).pack(side=RIGHT)
       	Button(win,text='Quit',command=win.quit).pack(side=BOTTOM)
        win.protocol('WM_DELETE_WINDOW',win.quit)

        
	win.focus_set()
        win.grab_set()
        win.mainloop()
        win.destroy()
        print 'dialog exited gracefully'














###.............code to pack the command buttons
#.................................................................
bt=Button(root,text='Add your bookmark',command=getter)
bt2=Button(root,text='run your bookmark',command=run)


bt.pack(expand=YES,side=LEFT)
bt2.pack(expand=YES,side=RIGHT)








bt3=Button(root,text='View your current bookmarks',command=dialog)
bt3.pack(expand=YES,side=BOTTOM,pady=30)


txt=Label(root,text='Author -- Jeffrey Macharia')
txt.config(fg='green',font=('times',14,'bold'))
txt.pack()


if __name__=="__main__":
	root.mainloop()




