from tkinter import *
from collections import OrderedDict
import  TicTacToe_Chatroom_GUI

from functools import partial
from socket import AF_INET, socket, SOCK_STREAM

leaderboard = {
    'Justin': 5,
    'Nick': 3,
    'Marcus': 7,
    }


def printboard():
    topboard = Toplevel()
    title = Label(topboard, text="Top Players:", font=('Times New Roman', '16'))
    T = Text(topboard, height=20, width=13 )
    title.pack()
    T.pack()
    d_sorted_by_value = OrderedDict(sorted(leaderboard.items(), key=lambda t: t[1], reverse=True))
    for k, v in d_sorted_by_value.items():
        print("%s: %s" % (k, v))
    T.insert(END,leaderboard)



def secondpage():
    second = Toplevel()
    entered = profile.get()
    if entered in leaderboard:
        player = Label(second, text="Welcome back " + entered)
        start = Label(second, text="Start Game?")
        ok = Button(second, text="Yes!")

        player.pack()
        start.pack()
        ok.pack()
    else:
        leaderboard.update({entered:0})
        letsgo = Label(second, text="Welcome new player!")
        ready = Label(second, text="Ready to start?")
        alright = Button(second, text="Yes", command=TicTacToe_Chatroom_GUI.startGUI)

        letsgo.pack()
        ready.pack()
        alright.pack()



intro = Tk()
label = Label(intro, text="Welcome to Tic-Tac-Toe!", font=('Times New Roman', '16'))
label2 = Label(intro, text="Enter your profile name:", font=('Times New Roman', '13'))
profile = Entry(intro)
enter = Button(intro, text='Enter', command=secondpage)
board = Button(intro, text='Leaderboard', command=printboard)

intro.bind('<Return>', lambda event=NONE: enter.invoke())

label.pack()
label2.pack()
profile.pack()
enter.pack()
board.pack()

intro.title('Introduction')
intro.geometry("300x300+120+120")
intro.mainloop()
