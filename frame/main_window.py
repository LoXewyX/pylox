from data.metadata import app_title, my_version
import customtkinter
import tkinter as tk

SIZE = "600x400"

def main(user):
    global root
    root = tk.Tk()
    root.title(f"{app_title} v{my_version} [EARLY RELEASE]")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.geometry(SIZE)

    frame = customtkinter.CTkFrame(master=root)
    frame.place(in_=root, anchor="center", relx=.5, rely=.5)

    tk_app = customtkinter.CTkLabel(text=f"{app_title} portal")
    tk_app.grid(column=0, padx=20, pady=0, sticky="ew")
    tk_app.configure(font=("", 20))
    tk_app.place(anchor="center", relx=.5, rely=.25)

    customtkinter.CTkLabel(master=frame,text=f"Welcome {user}!").pack()

    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()