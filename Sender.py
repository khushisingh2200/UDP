# sender.py
import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 5005 # Use any free port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
events = [
"CMD_EXEC_OK: Command A executed successfully",
"CMD_EXEC_FAIL: Command B failed due to timeout",
"CMD_EXEC_OK: Command C executed successfully"
]
while True:
    for event in events:
        sock.sendto(event.encode('utf-8'), (UDP_IP, UDP_PORT))
        print("Sent:", event)
        time.sleep(2) # Wait before sending next event