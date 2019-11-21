from tkinter import *
from socket import *
from threading import Thread

# import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")
# https://codereview.stackexchange.com/questions/212699/tic-tac-toe-game-in-python-3-x-using-tkinter-gui-version-2
bclick = True

# Connection Setup
serverName = '10.0.0.124'
schoolName = '10.220.25.198'
portNumber = 1010

tttSocket = socket(AF_INET, SOCK_STREAM)
tttSocket.connect((serverName, portNumber))


def receive():
    while 1:
        try:
            Thread(target=send).start()
            mes = tttSocket.recv(1024).decode()
            output.insert(INSERT, '%s\n' % mes)
            print(mes)

        except:
            pass


def send():
    mes = textentry.get()
    output.insert(INSERT, '%s\n' % mes)
    textentry.delete(0, END)
    if mes == '{quit}':
        quitMessage = name + "has left the chat!\n"
        tttSocket.send(quitMessage.encode())
        tttSocket.close()
    else:
        tttSocket.send(mes.encode())
        receive()


# GUI + Client interaction
# _______________________________________________________________________________________
#def click():
 #   entered_text = textentry.get()
  #  output.insert(INSERT, '%s\n' % entered_text)
   # textentry.delete(0, END)


def ttt(buttons):
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True

    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')

    elif (button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is X !!!!\n')


    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button4['text'] == 'X' and button5['text'] == 'O' and button6['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button7['text'] == 'X' and button8['text'] == 'O' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button1['text'] == 'X' and button5['text'] == 'O' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button3['text'] == 'X' and button5['text'] == 'O' and button7['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button1['text'] == 'X' and button2['text'] == 'O' and button3['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')
    elif (button1['text'] == 'X' and button4['text'] == 'O' and button7['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button2['text'] == 'X' and button5['text'] == 'O' and button8['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')

    elif (button7['text'] == 'X' and button6['text'] == 'O' and button9['text'] == 'X'):
        output.insert(INSERT, 'Winner is O !!!!\n')


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

# Chatroom Creation

# Create imput box
textentry = Entry(tk, width=30, bg="white")
textentry.grid(row=3, column=3, stick=S + E + W)

# Create display
output = Text(tk, width=30, wrap=WORD, background="white")
output.grid(row=1, column=3, rowspan=2, sticky=N + S + E + W)

tk.bind('<Return>', lambda event=NONE: sendButton.invoke())

# Create button
sendButton = Button(tk, text="Send", command=send)
sendButton.grid(row=4, column=3, sticky=N)

output.insert(INSERT, "Welcome to TicTacToe chatroom! Please type your name and press enter...\n\n")
name = input("Please enter name: ")
tttSocket.send((name.encode()))
helloMessage = tttSocket.recv(1024).decode()
output.insert(INSERT, "Hello " + name + "! If you ever want to quit, type {quit} to exit.\n\n")
output.insert(INSERT, helloMessage)

recThread = Thread(target=receive).start()
tk.mainloop()
