import socket
import threading

def receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'NICK':
                sock.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            sock.close()
            break

def write(sock):
    while True:
        message = f'{nickname}: {input()}'
        sock.send(message.encode('utf-8'))

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'  # Replace with the server's IP if needed
server_port = 12345  # Ensure this matches the server's port
client.connect((server_host, server_port))

# Take nickname from user
nickname = input("Choose your nickname: ")

# Start threads for receiving and writing messages
receive_thread = threading.Thread(target=receive, args=(client,))
receive_thread.start()

write_thread = threading.Thread(target=write, args=(client,))
write_thread.start()
