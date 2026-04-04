def encrypt(data):
    return ''.join(chr(ord(c)+3) for c in data)

def decrypt(data):
    return ''.join(chr(ord(c)-3) for c in data)


def sender_side(message):
    print("\n🔹 --- SENDER SIDE --- 🔹")

    # Application Layer
    app_data = encrypt(message)
    print("Application Layer (Encrypted):", app_data)

    # Presentation Layer
    pres_data = f"[Encoded]{app_data}"
    print("Presentation Layer:", pres_data)

    # Session Layer
    sess_data = f"[SessionID:123]{pres_data}"
    print("Session Layer:", sess_data)

    # Transport Layer
    trans_data = f"[Port:5050]{sess_data}"
    print("Transport Layer:", trans_data)

    # Network Layer
    net_data = f"[IP:127.0.0.1]{trans_data}"
    print("Network Layer:", net_data)

    # Data Link Layer
    data_link = f"[MAC:00:1A:2B:3C:4D:5E]{net_data}"
    print("Data Link Layer:", data_link)

    # Physical Layer
    bits = ' '.join(format(ord(c), '08b') for c in data_link)
    print("Physical Layer (Bits):", bits)

    return data_link


def receiver_side(data):
    print("\n🔸 --- RECEIVER SIDE --- 🔸")

    # Data Link Layer
    print("Data Link Layer:", data)
    data = data.split("]", 1)[1]

    # Network Layer
    print("Network Layer:", data)
    data = data.split("]", 1)[1]

    # Transport Layer
    print("Transport Layer:", data)
    data = data.split("]", 1)[1]

    # Session Layer
    print("Session Layer:", data)
    data = data.split("]", 1)[1]

    # Presentation Layer
    print("Presentation Layer:", data)
    data = data.replace("[Encoded]", "")

    # Application Layer
    print("Application Layer (Encrypted):", data)
    original = decrypt(data)
    print("🔓 Decrypted Message:", original)


# 🔥 Main Execution
msg = input("Enter message: ")

sent_data = sender_side(msg)
receiver_side(sent_data)