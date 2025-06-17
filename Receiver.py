# listener.py

import socket

UDP_IP = "127.0.0.1"

UDP_PORT = 5005  # Must match sender

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP events on {UDP_IP}:{UDP_PORT}...")

while True:

    data, addr = sock.recvfrom(1024)

    message = data.decode('utf-8')

    print("Received event:", message)

    # Basic logic to interpret success/failure

    if "CMD_EXEC_OK" in message:

        print(" Success event detected.")

    elif "CMD_EXEC_FAIL" in message:

        print(" Failure event detected.")

