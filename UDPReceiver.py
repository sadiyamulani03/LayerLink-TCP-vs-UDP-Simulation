import socket

def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 5001))

    print("UDP Receiver waiting...")

    data, addr = s.recvfrom(1024)

    print("\n--- UDP Receiver ---")
    print("Received message:", data.decode())
    print("From:", addr)

receiver()