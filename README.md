# 🧑‍💻 Python Chat Application

A simple multi-user chat application using **Python sockets** and **threading**. This project includes both the server and client scripts.

## 📂 Project Structure

- `Server.py`: Handles multiple clients, broadcasting messages, and managing connections.
- `clinet.py`: Connects to the server, sends and receives messages.


## 🚀 How to Run

### 1. Start the Server

```bash
python Server.py
```

# 2. Start the Client
In a new terminal window (you can open multiple for different users), run:

```bash
python clinet.py
```
Enter your nickname when prompted and start chatting with other connected users.

# 🛠 Features
1- Multi-user support via threading.

2- Simple nickname identification system.

3- Real-time message broadcasting to all clients.

4- Handles client disconnections automatically.

📌 Requirements
Python 3.x

No external dependencies (only built-in libraries: socket, threading)



