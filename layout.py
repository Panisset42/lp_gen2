import tkinter as tk

class MinhaInterface:
    def __init__(self):
        #configuring main screen
        self.janela = tk.Tk()
        self.janela.geometry("1280x960")
        #configuring main work area
        self.main_frame = tk.Frame(self.janela, bg="white")
        self.main_frame.place(relheight="1.0", relwidth="0.8", relx=0.5, rely=0.5, anchor=tk.CENTER)
        #main font configuration
        self.main_font = ("Arial", 14)

    def login_screen(self, callback):
        def on_button_click():
            #getting and returning the username and the password for the login
            username = username_entry.get()
            password = password_entry.get()
            if callback(username, password, login_frame):
                login_frame.destroy()
                self.main_screen()

        # Generate the frame
        login_frame = tk.Frame(self.main_frame, bg="lightblue")
        login_frame.place(relheight="0.6", relwidth="0.4", relx=0.5, rely=0.5, anchor=tk.CENTER)
        #setting up columns
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=1)
        login_frame.grid_rowconfigure(2, weight=1)
        login_frame.grid_rowconfigure(3, weight=1)
        login_frame.grid_rowconfigure(4, weight=1)
        #setting up collumns
        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=1)
        login_frame.grid_columnconfigure(2, weight=0)
        login_frame.grid_columnconfigure(3, weight=0)
        login_frame.grid_columnconfigure(4, weight=1)
        login_frame.grid_columnconfigure(5, weight=1)
        #setting up labels
        tk.Label(login_frame, text="Username: ", bg="lightblue", font=self.main_font).grid(row=1, column=2, pady=20, padx=10, sticky="nsew")
        tk.Label(login_frame, text="Password: ", bg="lightblue", font=self.main_font).grid(row=2, column=2, pady=20, padx=10, sticky="nsew")
        #setting up entries
        username_entry = tk.Entry(login_frame, font=self.main_font)
        password_entry = tk.Entry(login_frame, show="*", font=self.main_font)
        username_entry.grid(row=1, column=3)
        password_entry.grid(row=2, column=3)
        #setting up button and functionality
        button = tk.Button(login_frame, text="Confirmar", command=on_button_click)
        button.grid(row=3, column=2, columnspan=2, ipadx=100)

        self.janela.mainloop()
    def main_screen(self):

        #setting up main menu area
        main_menu = tk.Frame(self.janela, bg = "#FEA500")
        main_menu.place(relheight="1.0", relwidth="0.20")
        #Setting up main menu rows
        main_menu.grid_rowconfigure(0, weight = 1)
        main_menu.grid_rowconfigure(1, weight = 1)
        main_menu.grid_rowconfigure(2, weight = 0)
        main_menu.grid_rowconfigure(3, weight = 0)
        main_menu.grid_rowconfigure(4, weight = 0)
        main_menu.grid_rowconfigure(5, weight = 1)
        main_menu.grid_rowconfigure(6, weight = 1)
        #safety column configuration
        main_menu.grid_columnconfigure( 0, weight = 1 )
        #setting up menu butons
        city_register = tk.Button(
            main_menu,
            text = "Cadastrar Cidade",
            font = self.main_font,
            )

        model_register = tk.Button(
            main_menu,
            text = "Cadastrar Modelo",
            font = self.main_font,
            )

        landing_page_generator = tk.Button(
            main_menu,
            text = "Gerador de LPs",
            font = self.main_font,
            )
        city_register.grid( row = 2, sticky = "ew", pady=5)
        model_register.grid( row = 3, sticky = "ew", pady=5)
        landing_page_generator.grid( row = 4, sticky = "ew", pady=5)
        #setting up main content area
        self.main_frame.destroy()
        self.main_frame = tk.Frame( self.janela, bg = "white" )
        self.main_frame.place(relheight="1.0", relwidth="0.8", relx=0.20)
