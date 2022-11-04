import socket
import threading
import subprocess

PORT = 5000
HEADER = 128
SERVER = "192.168.8.120"
ADDRESS = (SERVER,PORT)
DISCONNECTION_MSG = "!LEAVE!"
FORMAT = "utf-8"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)


def run_command(command,con):

    list = command.split(" ")
    command = list[0]
    list.pop(0)


    if command == "sudo":
        com = ""
        for i in list:
            com+=i
        print(subprocess.call(f"echo karam2005 | sudo -S {com}",shell=True))


    output = subprocess.run(command,capture_output=True,shell=True).stdout
    print(output)
    con.send(output)

def handle_client(connection,address):
    print(f"[new connaection] {address}")
    connected = True
    while connected:
            command = connection.recv(128).decode(FORMAT)
            if command == DISCONNECTION_MSG:
                break

            run_command(command,connection)



    connection.close()



def start():
        server.listen()
        while True:
            (connection,address) = server.accept()
            handle_client(connection,address)
            #handle = threading.Thread(target=handle_client,args=(connection,address))
            #handle.start()

start()

