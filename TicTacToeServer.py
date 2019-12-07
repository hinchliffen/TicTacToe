from socket import *
from threading import Thread

activeConnections = []

# Accepts connections and adds them to activeConnections list
# Prints out active connections and starts a thread: handle_client
def accept_incoming_connections(serverSocket):
    count = 0
    while 1:
        connectionSocket, addr = serverSocket.accept()
        activeConnections.append(connectionSocket)
        count = count + 1
        print("Connections active: " + str(activeConnections))
        print(count)

        Thread(target=handle_client, args=(connectionSocket, addr)).start()

# Handles the received message from the client
# Prints message to console then calls broadcastConnection with message-
# - as input
def handle_client(connectionSocket, addr):
    while 1:
        message = connectionSocket.recv(1024).decode()
        print(message)
        broadcastConnection(message)

# Loops through activeConnections and sends
# message to all connections
def broadcastConnection(message):
    for i in activeConnections:
        i.send(message.encode())

# Loops through activeConnections
# if connectionSocket is equal to i-
# -then remove connectionSocket from active connections
def removeConnection(connectionSocket):
    for i in activeConnections:
        if i == connectionSocket:
            activeConnections.remove(connectionSocket)


# Main code which creates sockets and listens for connections
# Starts a thread: accecpt_incoming_connections
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


