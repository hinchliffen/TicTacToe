from socket import *
from threading import Thread

activeConnections = []


def accept_incoming_connections(serverSocket):
    count = 0
    while 1:
        connectionSocket, addr = serverSocket.accept()
        activeConnections.append(connectionSocket)
        count = count + 1
        print("Connections active: " + str(activeConnections))
        print(count)

        Thread(target=handle_client, args=(connectionSocket, addr)).start()


def handle_client(connectionSocket, addr):
    while 1:
        quitMessage = "Nick has left the chat!\n"
        message = connectionSocket.recv(1024).decode()
        if message == quitMessage:
            removeConnection(connectionSocket)
            print(activeConnections)
            broadcastConnection(message)
        else:
            print(message)
            broadcastConnection(message)


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


