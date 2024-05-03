import socket
import colorama

colorama.init(autoreset=True)

SERVER_HOST = '192.168.1.7'
SERVER_PORT = 65432

not_exit = True

while not_exit:
    command = str(input("The command: "))

    if command == "X":
        not_exit = True
        break

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        
        s.sendall(command.encode())
        print(f"Sent: {colorama.Fore.BLUE}{command}{colorama.Fore.RESET}")

        data = s.recv(1024)
        print(f"Received: \n\n {colorama.Fore.GREEN}{data.decode()}{colorama.Fore.RESET}")
