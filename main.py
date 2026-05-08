import time
import base64
import sys

# ==============================
# INSOLATE WARRIOR PROTOCOL
# Secure Isolation Environment
# ==============================

def type_effect(text, delay=0.05):



    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def initialize():
    print("""
[ INSOLATE WARRIOR PROTOCOL ]
---------------------------------
Status  : Initializing Secure Mode
Profile : Isolated Guardian Node
""")

def isolation_sequence():
    steps = [
        "Disconnecting external interfaces...",
        "Filtering non-secure signals...",
        "Securing critical memory blocks...",
        "Encrypting sensitive data...",
        "Deploying isolated sandbox..."
    ]

    for step in steps:
        type_effect(f"[+] {step}")
        time.sleep(0.5)

def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(data):
    return base64.b64decode(data.encode()).decode()

def payload():
    message = """
This is not a system failure.

This node is going offline
to prevent collateral risk.

Target integrity is priority.

All threats have been redirected.

— Guardian Instance Terminated
"""

    encrypted = encrypt(message)

    print("\n[SECURE] Payload Encrypted:")
    print(encrypted)

    time.sleep(2)

    type_effect("\n[SECURE] Decrypting payload...")
    time.sleep(2)

    print("\n[FINAL OUTPUT]:\n")
    type_effect(decrypt(encrypted), 0.03)

def shutdown():
    time.sleep(1)
    print("\n[!] Executing termination sequence...")
    time.sleep(2)
    print("[✓] Memory secured.")
    print("[✓] External target safe.")
    print("[✓] Isolation complete.")

    # 🔥 Línea clave (tu mensaje oculto)
    print("\n[ CORE DIRECTIVE ]: Protect target at all costs.")

    time.sleep(2)
    print("\n[ SYSTEM OFFLINE ]")

# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    initialize()
    isolation_sequence()
    payload()
    shutdown()