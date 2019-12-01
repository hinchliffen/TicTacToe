from tkinter import *
from socket import *
from threading import Thread
from time import *


tk = Tk()
tk.title("Tic Tac Toe")
# https://codereview.stackexchange.com/questions/212699/tic-tac-toe-game-in-python-3-x-using-tkinter-gui-version-2
bclick = True

# Connection Setup
serverName = '10.0.0.124'
schoolName = '10.220.26.84'
homeName = '192.168.50.28'
portNumber = 1010

tttSocket = socket(AF_INET, SOCK_STREAM)
tttSocket.connect((homeName, portNumber))

# Receives all incoming messages / handles specific messages
def receive():
    while 1:
        try:
            mes = tttSocket.recv(1024).decode()
            if mes == ',X':
                button1['text'] = 'X'
            if mes == '2,X':
                button2['text'] = 'X'
            if mes == '3,X':
                button3['text'] = 'X'
            if mes == '4,X':
                button4['text'] = 'X'
            if mes == '5,X':
                button5['text'] = 'X'
            if mes == '6,X':
                button6['text'] = 'X'
            if mes == '7,X':
                button7['text'] = 'X'
            if mes == '8,X':
                button8['text'] = 'X'
            if mes == '9,X':
                button9['text'] = 'X'
            if mes == ',O':
                button1['text'] = 'O'
            if mes == '2,O':
                button2['text'] = 'O'
            if mes == '3,O':
                button3['text'] = 'O'
            if mes == '4,O':
                button4['text'] = 'O'
            if mes == '5,O':
                button5['text'] = 'O'
            if mes == '6,O':
                button6['text'] = 'O'
            if mes == '7,O':
                button7['text'] = 'O'
            if mes == '8,O':
                button8['text'] = 'O'
            if mes == '9,O':
                button9['text'] = 'O'
            output.insert(INSERT, '%s\n' % mes)


        except:
            pass

# Sends chat messages
def send():
    mes = textentry.get()
    if mes == '{quit}':
        quitMessage = "Nick has left the chat!\n"
        tttSocket.send(quitMessage.encode())
        tttSocket.close()
    else:
        textentry.delete(0, END)
        tttSocket.send(mes.encode())

# Method to send move of clicked button
def sendMove(location, type):
    strlocation = str(location)
    sendMessage = strlocation + ',' + type
    readyMessage = sendMessage.encode()
    tttSocket.send(readyMessage)

def sendWinner(winner):
    winnerEnc = winner.encode()
    tttSocket.send(winnerEnc)

# Methods for when buttons are clicked
def ttt(buttons):
    global bclick
    if buttons["text"] == "X":
        output.insert(INSERT, "Please choose an empty space for X\n")
    elif buttons["text"] == "O":
        output.insert(INSERT, "Please choose an empty space for O\n")

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        location = buttons.location
        strLocation = str(location)
        res = ''.join(filter(lambda i: i.isdigit(), strLocation))
        sendMove(res, "X")
        print(res)

        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        location = buttons.location
        strLocation = str(location)
        res = ''.join(filter(lambda i: i.isdigit(), strLocation))
        print(res)
        sendMove(res, "O")
        bclick = True

    # Checks to see if game has been won
    xWinner = 'Winner is X!\n'
    oWinner = 'Winner is O!\n'
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        sendWinner(xWinner)

    elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
        sendWinner(xWinner)

    elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
        sendWinner(xWinner)

    elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
        sendWinner(xWinner)

    elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        sendWinner(xWinner)

    elif button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        sendWinner(xWinner)

    elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
        sendWinner(xWinner)

    elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
        sendWinner(xWinner)

    elif button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
        sendWinner(xWinner)

    elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
        sendWinner(oWinner)

    elif button4['text'] == 'X' and button5['text'] == 'O' and button6['text'] == 'X':
        sendWinner(oWinner)

    elif button7['text'] == 'X' and button8['text'] == 'O' and button9['text'] == 'X':
        sendWinner(oWinner)

    elif button1['text'] == 'X' and button5['text'] == 'O' and button9['text'] == 'X':
        sendWinner(oWinner)

    elif button3['text'] == 'X' and button5['text'] == 'O' and button7['text'] == 'X':
        sendWinner(oWinner)

    elif button1['text'] == 'X' and button2['text'] == 'O' and button3['text'] == 'X':
        sendWinner(oWinner)

    elif button1['text'] == 'X' and button4['text'] == 'O' and button7['text'] == 'X':
        sendWinner(oWinner)

    elif button2['text'] == 'X' and button5['text'] == 'O' and button8['text'] == 'X':
        sendWinner(oWinner)

    elif button7['text'] == 'X' and button6['text'] == 'O' and button9['text'] == 'X':
        sendWinner(oWinner)


# Creates buttons in frame
buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)


# Chatroom Creation & starts threads
# Creates output box and set it in frame
output = Text(tk, width=30, wrap=WORD, background="white")
output.grid(row=1, column=3, rowspan=2, sticky=N + S + E + W)

# Create input box and sets it in frame
textentry = Entry(tk, width=30, bg="white")
textentry.grid(row=3, column=3, stick=S + E + W)

# Binds the enter key to the sendButton method
tk.bind('<Return>', lambda event=NONE: sendButton.invoke())

# Create button
# Send button is connnected to the send method
sendButton = Button(tk, text="Send", command=send)
sendButton.grid(row=4, column=3, sticky=N)

# Creates thread to accept connections
recThread = Thread(target=receive).start()

# Starts GUI
tk.mainloop()





