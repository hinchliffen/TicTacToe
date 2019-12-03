from tkinter import *
from tkinter import Tk, Label, Button
import tkinter.messagebox
import sys
import os

tk = Tk()
tk.title("Tic Tac Toe")
#https://codereview.stackexchange.com/questions/212699/tic-tac-toe-game-in-python-3-x-using-tkinter-gui-version-2
bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

def click():
    entered_text = textentry.get()
    output.insert(INSERT, '%s\n' % entered_text)
    textentry.delete(0, END)

##Button Clicks for x
##https://codereview.stackexchange.com/questions/212699/tic-tac-toe-game-in-python-3-x-using-tkinter-gui-version-2 (This was used to help with the else if statements)
def ttt(buttons):
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True

    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    
    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    ##Button Clicks for o
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'):
        tkinter.messagebox.showinfo("Player X", "Winner is X!!!")
    elif (button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")
    elif (button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Player O", "Winner is O!!!")


#Appearce and command of the buttons
##https://stackoverflow.com/questions/6171493/how-to-set-the-button-sticky-property-properly (Used to help the syntax and format of the buttons)
buttons = StringVar()

button1 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)


#Chatroom Creation
#Create imput box
textentry = Entry(tk, width = 30, bg = "white")
textentry.grid(row = 3, column = 3, stick = S+E+W)

#Create display
output = Text(tk, width = 30, wrap =WORD, background = "white")
output.grid(row = 1, column = 3, rowspan = 2, sticky = N+S+E+W)

tk.bind('<Return>', lambda event = NONE: sendButton.invoke())

#Create button
sendButton =Button(tk, text = "Send", command = click)
sendButton.grid(row = 4, column = 3, sticky = N)

#restart button 
sendButton =Button(tk, text = "Restart", command = restart_program)
sendButton.grid(row = 4, column = 1, sticky = N)



tk.mainloop()
