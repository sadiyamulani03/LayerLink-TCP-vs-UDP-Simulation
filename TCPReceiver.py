import socket

def decrypt(msg):
    return ''.join(chr(ord(c)-3) for c in msg)

def receiver():
    s = socket.socket()
    s.bind(("127.0.0.1", 5000))
    s.listen(1)

    print("Waiting for connection...")
    conn, addr = s.accept()

    data = conn.recv(1024).decode()

    print("\n--- OSI Layers (Receiver Side) ---")

    # Data Link Layer
    print("Data Link Layer:", data)
    data = data.split("|", 1)[1]

    # Network Layer
    print("Network Layer:", data)
    data = data.split("|", 1)[1]

    # Transport Layer
    print("Transport Layer:", data)
    data = data.split("|", 1)[1]

    # Application Layer
    print("Application Layer (Encrypted):", data)

    dec_msg = decrypt(data)
    print("Decrypted Message:", dec_msg)

    conn.close()

receiver()