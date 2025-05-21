import socket
import threading
HEADER = 64
PORT = 4090
#SERVER = "192.168.xxx.XXX"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT =  'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTED!'
#print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass
    print(f"[NEW CONNECTION] {addr} connected ")

    connected = True 
    while connected: 
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            #print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    pass
    server.listen()
    print(f"[LISTENING] Server is Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



print("[STARTING] server is starting...")
start()
