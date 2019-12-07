from tkinter import *
from socket import *
from threading import Thread
from time import *

bclick = True
associatedName = ''
gameEnded = 0

def startGUI(profileName):
    tk = Tk()
    tk.title("Tic Tac Toe")
    # https://codereview.stackexchange.com/questions/212699/tic-tac-toe-game-in-python-3-x-using-tkinter-gui-version-2

    # Connection Setup
    serverName = '10.0.0.124'
    portNumber = 1010

    tttSocket = socket(AF_INET, SOCK_STREAM)
    tttSocket.connect((serverName, portNumber))

    # Freezes all moves, sleeps for one second & resets board
    def disable():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        sleep(1.5)
        button1['text'] = " "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "
        button1.configure(state=NORMAL)
        button2.configure(state=NORMAL)
        button3.configure(state=NORMAL)
        button4.configure(state=NORMAL)
        button5.configure(state=NORMAL)
        button6.configure(state=NORMAL)
        button7.configure(state=NORMAL)
        button8.configure(state=NORMAL)
        button9.configure(state=NORMAL)

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
                if mes == associatedName + ' is the winner! \n':
                    disable()
                if mes == 'Exit()':
                    tk.quit()
                else:
                    output.insert(INSERT, '%s\n' % mes)

            except:
                pass

    # Sends chat messages
    def send():
        mes = textentry.get()
        sendMes = profileName + ": " + mes
        sendMesgo = sendMes.encode()
        if mes == '{quit}':
            quitMessage = profileName + " has left the chat!\n"
            tttSocket.send(quitMessage.encode())
            tttSocket.close()
            tk.destroy()
        else:
            textentry.delete(0, END)
            tttSocket.send(sendMesgo)

    # Method to send move of clicked button
    def sendMove(location, type):
        strlocation = str(location)
        sendMessage = strlocation + ',' + type
        readyMessage = sendMessage.encode()
        tttSocket.send(readyMessage)

    def sendWinner(winner):
        winnerEnc = winner.encode()
        tttSocket.send(winnerEnc)

    def sendOpponent(name):
        nameEnc = name.encode()
        tttSocket.send(nameEnc)

    # Methods for when buttons are clicked
    def ttt(buttons):
        global bclick
        global associatedName
        if buttons["text"] == "X":
            output.insert(INSERT, "Please choose an empty space for X\n")
        elif buttons["text"] == "O":
            output.insert(INSERT, "Please choose an empty space for O\n")

        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            associatedName = profileName
            location = buttons.location
            strLocation = str(location)
            res = ''.join(filter(lambda i: i.isdigit(), strLocation))
            sendMove(res, "X")
            print(res)

            bclick = False
        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            associatedName = profileName
            location = buttons.location
            strLocation = str(location)
            res = ''.join(filter(lambda i: i.isdigit(), strLocation))
            print(res)
            sendMove(res, "O")
            bclick = True

        # Checks to see if game has been won
        rWinner = associatedName + ' is the winner! \n'
        if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
            sendWinner(rWinner)

        elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
            sendWinner(rWinner)

        elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
            sendWinner(rWinner)

        elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
            sendWinner(rWinner)

        elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
            sendWinner(rWinner)

        elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
            sendWinner(rWinner)

        elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
            sendWinner(rWinner)

        elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
            sendWinner(rWinner)

        if button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
            sendWinner(rWinner)

        elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
            sendWinner(rWinner)

        elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':
            sendWinner(rWinner)

        elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
            sendWinner(rWinner)

        elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
            sendWinner(rWinner)

        elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
            sendWinner(rWinner)

        elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
            sendWinner(rWinner)

        elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
            sendWinner(rWinner)

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
    output = Text(tk, width=40, wrap=WORD, background="white")
    output.grid(row=1, column=3, rowspan=2, sticky=N + S + E + W)
    output.insert(INSERT, "Hello " + profileName + "! Welcome to TicTacToe!\n")
    playerJoin = profileName + " has joined the game!\n"
    sendOpponent(playerJoin)

    # Create input box and sets it in frame
    textentry = Entry(tk, width=40, bg="white")
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
