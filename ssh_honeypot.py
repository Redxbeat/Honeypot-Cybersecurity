import socket
import datetime
import csv

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("[+] Advanced SSH Honeypot Running on Port 2222")

while True:
    try:
        client, addr = server.accept()
        timestamp = datetime.datetime.now()

        print(f"[!] Connection from {addr}")

        client.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        data = client.recv(1024)

        with open("honeypot.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, addr[0], addr[1], data])

        client.close()

    except KeyboardInterrupt:
        print("\n[!] Honeypot stopped.")
        break
