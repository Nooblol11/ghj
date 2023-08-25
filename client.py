#library
#Server
import socket
import threading
#GUI
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

#Server
HOST = '192.168.1.8'
PORT = 1234
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#functions
#add message to the box in the middle frame 
def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)
#connect to the server
def connect():
   
    try:
        client.connect((HOST,PORT))
        print("[Server]:connected to the server")
    except:
        messagebox.showerror(f"Unable to connect to server","Unable to connect to server {HOST} {PORT}")
        exit(0)
    
    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
        
        
    else:
        messagebox.showerror("Error","username cant be empty")
        exit(0)
    threading.Thread(target=listen_for_message_from_server, args=(client, )).start()
    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)
    
    
    


#send the message to server using GUI
def send():
    
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
        
    else:
        messagebox.showerror("","you cant send empty msg")
        #exit(0)


#Colors
Dark_Grey = '#101010'
Medium_Grey = '#1f1B24'
Ocean_Blue = '#464EB8'
White = 'white'
FONT = ("Helvetica", 17)
SMALL_FONT = ("Helvetica", 13)
Button_font = ("Helvetica", 15)
Button_font2 = ("Helvetica", 15)
#GUI Properties
root = tk.Tk()
root.geometry("600x600")
root.title("Noobs whatsapp")
root.resizable(False, False)
#make frames to sperate the screen
top_frame = tk.Frame(root, width=600, height=100, bg=Dark_Grey)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)
middle_frame = tk.Frame(root, width=600, height=500, bg=Medium_Grey)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)
bottom_frame = tk.Frame(root, width=600, height=100, bg=Dark_Grey)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
#username label
username_label = tk.Label(top_frame, text="Enter username:", font=FONT, bg=Dark_Grey, fg=White)
username_label.pack(side=tk.LEFT, padx=10)
#username textbox
username_textbox = tk.Entry(top_frame, font=FONT, bg=Medium_Grey, fg=White, width=23)
username_textbox.pack(side=tk.LEFT, padx=5)
message_textbox = tk.Entry(bottom_frame, font=FONT, bg=Medium_Grey, fg=White, width=40)
message_textbox.pack(side=tk.LEFT, padx=5)
#username Confirm button
username_button = tk.Button(top_frame, text="Join", font=Button_font, bg=Ocean_Blue, fg=White, command=connect)
username_button.pack(side=tk.LEFT, padx=15)
message_button = tk.Button(bottom_frame, font=Button_font2, text="send", bg=Ocean_Blue, fg=White, command=send)
message_button.pack(side=tk.LEFT, padx=5)
#box appear messages
message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=Medium_Grey, fg=White, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.LEFT, padx=1)


#Gain message from server and show to the user 
def listen_for_message_from_server(client):
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split(":-")[0]
            content = message.split(':-')[1]

            add_message(f"[{username}] {content}")
        else:
            pass


#send the to server to show to another users
def send_msg_to_server(client):
    
    pass



#intro of the program
def comunicate_to_server(client):
    pass    




def main():

    root.mainloop()
    


if __name__ == '__main__':
    main()