from tkinter import *
from collections import OrderedDict
import TicTacToe_Chatroom_GUI


leaderboard = {
    'Justin': 5,
    'Nick': 3,
    'Marcus': 7,
    }

# Suppose to update Leaderboard
def updateboard(x):
    if x in leaderboard:
        leaderboard[x] += 1
    else:
        leaderboard[x] = 1

# Saves leaderboard into .txt file
def saveleaderboard():
    f = open("leaderboard.txt", "w")
    d_sorted_by_value = OrderedDict(sorted(leaderboard.items(), key=lambda t: t[1], reverse=True))
    for k, v in d_sorted_by_value.items():
      f.write("%s: %s\n" % (k,v))
    f.close()

# Sorts the leaderboard
def trueboard():
    topboard = Toplevel()
    title = Label(topboard, text="Top Players:", font=('Times New Roman', '16'))
    T = Text(topboard, height=20, width=13)
    title.pack()
    T.pack()
    f = open("leaderboard.txt", "r")
    message = f.read()
    T.insert(END,message)
    f.close()

# Starts client and names them based on entered
def startClient():
    entered = profile.get()
    profile.delete(0, END)
    if entered in leaderboard:
        TicTacToe_Chatroom_GUI.startGUI(entered)
    else:
        leaderboard.update({entered:0})
        TicTacToe_Chatroom_GUI.startGUI(entered)

# Creates intro GUI
intro = Tk()
label = Label(intro, text="Welcome to Tic-Tac-Toe!", font=('Times New Roman', '16'))
label2 = Label(intro, text="Enter your profile name:", font=('Times New Roman', '13'))
profile = Entry(intro)
enter = Button(intro, text='Enter', command=startClient)
board = Button(intro, text='Leaderboard', command=trueboard)


intro.bind('<Return>', lambda event=NONE: enter.invoke())

label.pack()
label2.pack()
profile.pack()
enter.pack()
board.pack()

intro.title('Introduction')
intro.geometry("300x300+120+120")
intro.mainloop()
