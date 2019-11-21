from socket import *
from threading import Thread


activeConnections = []


def accept_incoming_connections(serverSocket):
    while 1:
        connectionSocket, addr = serverSocket.accept()
        activeConnections.append(connectionSocket)
        #print(activeConnections)
        #print("%s:%s has connected." % addr)
        Thread(target=handle_client, args=(connectionSocket, addr)).start()


def handle_client(connectionSocket, addr):
    name = connectionSocket.recv(1024).decode()
    nameSend = (name + " has joined the chat!")
    print(nameSend)
    broadcastConnection(nameSend)
    while 1:
        quitMessage = name + " has left the chat!\n"
        message = connectionSocket.recv(1024).decode()
        if message == quitMessage:
            fqm = print(quitMessage)
            removeConnection(connectionSocket)
            broadcastConnection(fqm)
        else:
            readytogo = name + ": " + message
            print(readytogo)

            broadcastConnection(readytogo)


def broadcastConnection(message):
    for i in activeConnections:
        i.send(message.encode())


def removeConnection(connectionSocket):
    for i in activeConnections:
        if i == connectionSocket:
            activeConnections.remove(connectionSocket)



def main():
    serverPort = 1010
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    #can take up to 10 connections
    serverSocket.listen(10)
    #create list to track connetions
    print("Waiting for connection...")
    while 1:
        acceptThread = Thread(target=accept_incoming_connections, args=(serverSocket,))
        acceptThread.start()
        acceptThread.join()
        serverSocket.close()


if __name__ == "__main__":
    main()


