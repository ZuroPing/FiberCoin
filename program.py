import json
import socket

def Node(settings):
    #Broadcast joining the network
    for node in settings["nodes"]:
        socket.sendto(bytes("broadcast "+settings["port"], "ASCII"), (node[0], node[1]))

def node_settings(settings):
    while True:
        user_input = input("\n*****settings*****\nport: "+settings["port"]+"\nmining: "+settings["mining"]+"\n******************\n'setting'='value': ")
        if not bool(user_input):
            break
        elif user_input.split("=")[0] in settings:
            settings[user_input.split("=")[0]] = user_input.split("=")[1]
    return settings

def main(settings):
    display = True
    while True:
        if display:
            user_input = input("\n*****FiberCore*****\n1-Start Node\n2-Settings\n3-Exit\n**********************\n:")
        else:
            user_input = input(":")
            display = True
        if user_input == "1":
            Node(settings)
        elif user_input == "2":
            settings = node_settings(settings)
        elif user_input == "3":
            with open("settings.json", "w") as file:
                json.dump(settings, file)
            break
        else:
            display = False

def startup():
    #I Exist
    with open("nodes.txt", "r") as nodes:
        nodes = nodes.read().split("\n")
        for node in nodes:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((node, 50007))
            s.sendall(b'a') # a for add me
            s.close()

if __name__ == "__main__":
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        print("Settings not found!")
    main(settings)


"""
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
"""
