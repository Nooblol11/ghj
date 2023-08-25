import socket
import threading
import tkinter as tk


HOST = '192.168.1.8'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []



def listen_for_msg(client, username):
    while 1:
        message = response = client.recv(2048).decode('utf-8')
        if response != '':
            fin_msg = username + ':-' + response
            send_msg(fin_msg)
        else:
            print(f"empty from {username}")





def send_msg_to_client(client, message):
    client.sendall(message.encode())





def send_msg(message):
    for user in active_clients: 
        send_msg_to_client(user[1], message)







def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER:- " + f"{username} added to chat"
            send_msg(prompt_message)
            break
        else:
            print("client name is empty")

    threading.Thread(target=listen_for_msg, args=(client, username, )).start()








def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
        print(f"running")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    server.listen(LISTENER_LIMIT)

    while 1:
        client, address = server.accept()
        print(f"Done!!? {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()

if __name__ == '__main__':
    main()
