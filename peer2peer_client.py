import socket
import sqlite3
import select
import time

my_ip = '10.239.128.59'  # Replace with your IP address
my_port = 5001

peer_ip = '10.239.128.59'  # Replace with server IP address
peer_port = 5001  # Replace with server port

KEEP_ALIVE_INTERVAL = 30  # in seconds
MESSAGE_TYPE_LIST_CLIENTS = "list clients"
MESSAGE_TYPE_CHAT = "chat"

def start_client():
    conn = sqlite3.connect('p2p_chat.db')
    c = conn.cursor()

    # Connect to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((peer_ip, peer_port))
        print(f"Connected to server {peer_ip}:{peer_port}")
    except socket.error as e:
        print(f"Error connecting to {peer_ip}:{peer_port}: {e}")
        return

    last_keep_alive_time = time.monotonic()

    while True:
        message = input("Enter message (type 'quit' to exit, 'list' for clients): ")
        if message == 'quit':
            break
        elif message == 'list':
            server_socket.send(MESSAGE_TYPE_LIST_CLIENTS.encode())
        else:
            server_socket.send(message.encode())

        current_time = time.monotonic()
        if current_time - last_keep_alive_time >= KEEP_ALIVE_INTERVAL:
            server_socket.send("keep alive".encode())
            last_keep_alive_time = current_time

        # Wait for up to 5 seconds for a response
        ready = select.select([server_socket], [], [], 5)
        if ready[0]:
            response = server_socket.recv(1024).decode()
            if response == MESSAGE_TYPE_LIST_CLIENTS:
                client_list = server_socket.recv(1024).decode()
                print(f"Client list:\n{client_list}")
            else:
                print(f"Server response: {response}")
        else:
            print("No response received from server")

    server_socket.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    start_client()

