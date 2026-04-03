import socket

def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    msg = input("Enter message: ")

    print("\n--- UDP Sender ---")
    print("Sending without connection...")

    s.sendto(msg.encode(), ("127.0.0.1", 5001))

sender()