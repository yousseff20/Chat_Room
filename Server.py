import socket
import threading


host = "127.0.0.1"
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames.pop(index)
            broadcast(f"{nickname} left chat ".encode("utf-8"))
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"New connect {str(address)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f" Nickname of user {nickname}")
        broadcast(f"{nickname} Join the chat ".encode("utf-8"))
        client.send(" Connected to the server ".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("Server is working")
receive()
