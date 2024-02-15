import tkinter as tk

class MinhaInterface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("1280x960")
        self.main_frame = tk.Frame(self.janela, bg="white")
        self.main_frame.place(relheight="1.0", relwidth="0.85", relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.main_font = ("Arial", 14)

    def login_screen(self, callback):
        def on_button_click():
            username = username_entry.get()
            password = password_entry.get()
            callback(username, password, login_frame)

        # Generate the frame
        login_frame = tk.Frame(self.main_frame, bg="lightblue")
        login_frame.place(relheight="0.6", relwidth="0.4", relx=0.5, rely=0.5, anchor=tk.CENTER)

        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=1)
        login_frame.grid_rowconfigure(2, weight=1)
        login_frame.grid_rowconfigure(3, weight=1)
        login_frame.grid_rowconfigure(4, weight=1)

        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=1)
        login_frame.grid_columnconfigure(2, weight=0)
        login_frame.grid_columnconfigure(3, weight=0)
        login_frame.grid_columnconfigure(4, weight=1)
        login_frame.grid_columnconfigure(5, weight=1)

        tk.Label(login_frame, text="Username: ", bg="lightblue", font=self.main_font).grid(row=1, column=2, pady=20, padx=10, sticky="nsew")
        tk.Label(login_frame, text="Password: ", bg="lightblue", font=self.main_font).grid(row=2, column=2, pady=20, padx=10, sticky="nsew")

        username_entry = tk.Entry(login_frame, font=self.main_font)
        password_entry = tk.Entry(login_frame, show="*", font=self.main_font)
        username_entry.grid(row=1, column=3)
        password_entry.grid(row=2, column=3)

        button = tk.Button(login_frame, text="Confirmar", command=on_button_click)
        button.grid(row=3, column=2, columnspan=2, ipadx=100)

        self.janela.mainloop()
