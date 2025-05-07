import socket
import threading

# Comments in this code are for my own reference incase I forget what is going on

IP = '0.0.0.0'
PORT = 9998

def main():
    # TCP socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # pass the IP and port
    server.bind((IP, PORT))
    # listen for a max of 5 connections
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')
    # main loop to accept connections
    while True:
        client, address = server.accept() # accept the connection
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) # thread object pointing to the handle_client function
        client_handler.start()

def handle_client(client_socket):
    # receive data from client
    request = client_socket.recv(1024)
    print(f'[*] Received: {request.decode("utf-8")}')
    # response from server
    client_socket.send(b'ACK')
    client_socket.close()

if __name__ == '__main__':
    main()