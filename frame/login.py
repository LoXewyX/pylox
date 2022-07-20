from tkinter import DISABLED, Tk, StringVar, Toplevel, messagebox
import db.db_config as dfg
from data.metadata import app_title, my_version, current_dir
import data.pswd_crypto as pycry
import customtkinter
import utils.stringParser as strp
from PIL import Image, ImageTk
import json

#https://github.com/TomSchimansky/CustomTkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

SIZE = "600x400"

def hideMain():
    root.withdraw()

def showMain():
    root.deiconify()
    if 'root1' in globals():
        root1.destroy()
    if 'root2' in globals():
        root2.destroy()

def logged():
    global usr
    if 'root1' in globals():
        root1.destroy()
    if 'root2' in globals():
        root2.destroy()
    if 'root' in globals():
        root.destroy()

    if reg: print("Logged successfully!")
    import frame.main_window as fm
    fm.main(usr)

def error(text):
    messagebox.showerror('Error', text)

def success(username):
    messagebox.showinfo('Success', f'Account {username} was created')
    showMain() # not necessary but it returns to main

def register_user():
    username_info = username.get()
    password_info = password.get()

    min_usr_len = 3
    min_pswd_len = 6
    min_pswd_uppers = 1

    if len(username_info) >= 3:
        if len(password_info) >= 6 and strp.UpperChecker(password_info, min_pswd_uppers):
            data = dfg.show_values(
                "usrdata",
                "`username`, `ip`",
                returnValues = True,
                reg = reg
            )

            rep_ip = 0

            from utils.ip import get_public_ip
            
            for d in data:
                if d[1] == get_public_ip():
                    rep_ip += 1

            if rep_ip < 3:
                for d in data:
                    if password_info == "":
                        error("Password cannot be empty")
                        root1.focus_get()
                        break

                    elif username_info.lower() in d[0]:
                        error("Username already exists")
                        break
                else:
                    dfg.insert_table_values(
                        "usrdata",
                        [
                            "`username`",
                            "`password`"
                        ],
                        [(
                            username_info.lower(),
                            pycry.encode(password_info)
                        )],
                        reg = reg
                    )
                    success(username_info)

            else:
                error("Your IP address have a maximum of 3 accounts")
        else:
            error(
                f"""Password must contain at least:
                \n- Minimum length must be {min_pswd_len} characters
                \n- {min_pswd_uppers} uppercase
                """)
    else:
        error(f"Name must contain {min_usr_len} or more characters")

def enableBox():
    global enbl, tk5
    if enbl:
        if reg: print("show pswd")
        tk5 = customtkinter.CTkEntry(master=frame1, textvariable=password, state=DISABLED, cursor="")
        tk5.grid(row=6, padx=20, pady=10, sticky="ew")
    else:
        if reg: print("hide pswd")
        tk5.grid_remove()
    enbl = not enbl

def registration():
    hideMain()
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry(SIZE)
    root1.resizable(False, False)
    root.eval(f'tk::PlaceWindow {str(root1)} center')
    root1.protocol("WM_DELETE_WINDOW", showMain)

    global frame1
    frame1 = customtkinter.CTkFrame(master=root1, bg_color='white')
    frame1.place(in_=root1, anchor="center", relx=.5, rely=.5)

    global username, password, enbl

    username = StringVar()
    password = StringVar()
    enbl = True

    tk1 = customtkinter.CTkLabel(master=frame1,text="Username")
    tk1.grid(row=1, padx=20, pady=10, sticky="ew")
    tk1.configure(font=("", 12))

    tk2 = customtkinter.CTkEntry(master=frame1, textvariable=username)
    tk2.grid(row=2, padx=20, sticky="ew")

    tk3 = customtkinter.CTkLabel(master=frame1, text="Password")
    tk3.grid(row=4, padx=20, pady=10, sticky="ew")
    tk3.configure(font=("", 12))

    tk4 = customtkinter.CTkEntry(master=frame1, textvariable=password,show="*")
    tk4.grid(row=5, padx=20, sticky="ew")

    img = ImageTk.PhotoImage(Image.open(PATH + "\\img\\sight.png").resize((25, 25)))
    tk6 = customtkinter.CTkButton(master=frame1, text="", image=img, command=enableBox)
    tk6.grid(row=7, padx=20, pady=10, sticky="ew")
    tk7 = customtkinter.CTkButton(master=frame1, text="Register", command=register_user)
    tk7.grid(row=8, padx=20, pady=10, sticky="ew")

def login():
    hideMain()
    if 'root1' in globals():
        root1.destroy()

    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry(SIZE)
    root2.resizable(False, False)
    root.eval(f'tk::PlaceWindow {str(root2)} center')
    root2.protocol("WM_DELETE_WINDOW", showMain)

    global frame2
    frame2 = customtkinter.CTkFrame(master=root2, bg='white')
    frame2.place(in_=root2, anchor="center", relx=.5, rely=.5)

    customtkinter.CTkLabel(master=frame2,text="").pack()
    customtkinter.CTkLabel(master=frame2,text="Username").pack()
    customtkinter.CTkEntry(master=frame2, textvariable=username_varify).pack()
    customtkinter.CTkLabel(master=frame2, text="").pack()
    customtkinter.CTkLabel(master=frame2, text="Password").pack()
    customtkinter.CTkEntry(master=frame2, textvariable=password_varify,show="*").pack()
    button = customtkinter.CTkButton(master=frame2, text="Log-In", command=login_varify)
    button.pack(pady=12, padx=12)

def login_varify():
    global username_varify, password_varify
    results = dfg.show_values(
        "usrdata",
        "`username`, `password`",
        reg = reg,
        returnValues = True
    )

    if results == []:
        results = [("", "")]

    for data in results:
        if data[0] == username_varify.get().lower() and pycry.decode(data[1]) == password_varify.get():
            global usr
            with open(current_dir, 'r') as f:
                l = json.load(f)
            usr = l['username'] = username_varify.get()
            l['password'] = pycry.encode(password_varify.get())
            with open(current_dir, 'w') as f:
                json.dump(l, f)

            global isVerified
            isVerified = True

            logged()
            break
    else:
        if data[0] == username_varify.get().lower():
            error("Invalid user")
        else:
            error("Invalid password")

def checkDataStored():
    global username_varify, password_varify
    with open(current_dir, 'r') as f:
        l = json.load(f)

    if l['username'] == "" or l['password'] == "":
        return False
    username_varify.set(l['username'])
    password_varify.set(pycry.decode(l['password']))
    login_varify()

    if isVerified:
        if reg: print("Auto-login successfully!")
        return True
    
    if reg: print("Auto-login went wrong!")
    return False

def main_screen(path, register):

    global root
    root = Tk()
    root.title(f"{app_title} v{my_version} [EARLY RELEASE]")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.geometry(SIZE)

    global username_varify, password_varify
    username_varify = StringVar()
    password_varify = StringVar()
    global isVerified
    isVerified = False
    global PATH, reg
    PATH = path
    reg = register

    if checkDataStored(): logged()

    frame = customtkinter.CTkFrame(master=root)
    frame.place(in_=root, anchor="center", relx=.5, rely=.5)

    tk_app = customtkinter.CTkLabel(text=f"{app_title} portal")
    tk_app.grid(column=0, padx=20, pady=0, sticky="ew")
    tk_app.configure(font=("", 20))
    tk_app.place(anchor="center", relx=.5, rely=.25)

    button_1 = customtkinter.CTkButton(master=frame, command=login, text="Log-In")
    button_1.pack(pady=12, padx=12)

    button_2 = customtkinter.CTkButton(master=frame, command=registration, text="Register")
    button_2.pack(pady=12, padx=12)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()