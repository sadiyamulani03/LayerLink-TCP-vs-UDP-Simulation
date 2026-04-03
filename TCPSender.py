import socket

def encrypt(msg):
    return ''.join(chr(ord(c)+3) for c in msg)  # simple Caesar cipher

def sender():
    s = socket.socket()
    s.connect(("127.0.0.1", 5000))

    msg = input("Enter message: ")

    print("\n--- OSI Layers (Sender Side) ---")

    # Application Layer
    enc_msg = encrypt(msg)
    print("Application Layer: Encrypted Data ->", enc_msg)

    # Transport Layer
    transport_data = f"PORT:5000|{enc_msg}"
    print("Transport Layer:", transport_data)

    # Network Layer
    network_data = f"IP:127.0.0.1|{transport_data}"
    print("Network Layer:", network_data)

    # Data Link Layer
    datalink_data = f"MAC:00:1A:2B:3C:4D:5E|{network_data}"
    print("Data Link Layer:", datalink_data)

    # Physical Layer
    bits = ' '.join(format(ord(i), '08b') for i in datalink_data)
    print("Physical Layer (Bits):", bits)

    s.send(datalink_data.encode())
    s.close()

sender()