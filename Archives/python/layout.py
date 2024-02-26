import tkinter as tk
from tkcalendar import DateEntry


class MinhaInterface:
    def __init__(self):
        # configuring main screen
        self.options = None
        self.entry_model = None
        self.janela = tk.Tk()
        self.janela.geometry("1280x960")
        # configuring main work area
        self.main_frame = tk.Frame(self.janela, bg="white")
        self.main_frame.place(relheight="1.0", relwidth="0.8", relx=0.5, rely=0.5, anchor=tk.CENTER)
        # main font configuration
        self.main_font = ("Arial", 14)
        self.entry_name = None
        self.entry_date = None
        self.entry_link = None
        self.entry_archive = None
        self.table_columns = []
        self.table_rows = []

    def login_screen(self):
        def on_button_click():
            # getting and returning the username and the password for the login
            username = username_entry.get()
            password = password_entry.get()

            EventPublisher.publish("login_attempt", username, password)

        # Generate the frame
        login_frame = tk.Frame(self.main_frame, bg="lightblue")
        login_frame.place(relheight="0.6", relwidth="0.4", relx=0.5, rely=0.5, anchor=tk.CENTER)
        # setting up columns
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=1)
        login_frame.grid_rowconfigure(2, weight=1)
        login_frame.grid_rowconfigure(3, weight=1)
        login_frame.grid_rowconfigure(4, weight=1)
        # setting up collumns
        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=1)
        login_frame.grid_columnconfigure(2, weight=0)
        login_frame.grid_columnconfigure(3, weight=0)
        login_frame.grid_columnconfigure(4, weight=1)
        login_frame.grid_columnconfigure(5, weight=1)
        # setting up labels
        tk.Label(login_frame, text="Username: ", bg="lightblue", font=self.main_font).grid(row=1, column=2, pady=20,
                                                                                           padx=10, sticky="nsew")
        tk.Label(login_frame, text="Password: ", bg="lightblue", font=self.main_font).grid(row=2, column=2, pady=20,
                                                                                           padx=10, sticky="nsew")
        # setting up entries
        username_entry = tk.Entry(login_frame, font=self.main_font)
        password_entry = tk.Entry(login_frame, show="*", font=self.main_font)
        username_entry.grid(row=1, column=3)
        password_entry.grid(row=2, column=3)
        # setting up button and functionality
        button = tk.Button(login_frame, text="Confirmar", command=on_button_click)
        button.grid(row=3, column=2, columnspan=2, ipadx=100)

        self.janela.mainloop()

    def main_screen(self):

        # setting up main menu area
        main_menu = tk.Frame(self.janela, bg="#FEA500")
        main_menu.place(relheight="1.0", relwidth="0.20")
        # Setting up main menu rows
        main_menu.grid_rowconfigure(0, weight=1)
        main_menu.grid_rowconfigure(1, weight=1)
        main_menu.grid_rowconfigure(2, weight=0)
        main_menu.grid_rowconfigure(3, weight=0)
        main_menu.grid_rowconfigure(4, weight=0)
        main_menu.grid_rowconfigure(5, weight=1)
        main_menu.grid_rowconfigure(6, weight=1)
        # safety column configuration
        main_menu.grid_columnconfigure(0, weight=1)
        # setting up menu buttons
        city_register = tk.Button(
            main_menu,
            text="Cadastrar Cidade",
            font=self.main_font,
            command=self.city_register
        )

        # model_register = tk.Button(
        #     main_menu,
        #     text="Cadastrar Modelo",
        #     font=self.main_font,
        #     command=self.model_register
        # )

        landing_page_generator = tk.Button(
            main_menu,
            text="Gerador de LPs",
            font=self.main_font,
            command=self.landing_page_generator
        )
        city_register.grid(row=2, sticky="ew", pady=5)
        # model_register.grid(row=3, sticky="ew", pady=5)
        landing_page_generator.grid(row=4, sticky="ew", pady=5)
        # setting up main content area
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.janela, bg="white")
        self.main_frame.place(relheight="1.0", relwidth="0.8", relx=0.20)
        self.city_register()

    def main_frame_setup(self):
        # cleaning everything but the menu
        try:
            child_frames = self.main_frame.winfo_children()
            for child in child_frames:
                child.destroy()
                # create a city register frame
            self.register_frame = tk.Frame(self.main_frame, bg="lightblue")
            self.register_frame.place(relwidth="1.0", relheight="0.8", relx=0.5, rely=0.5,
                                      anchor=tk.CENTER)
            # Creating a form-holder
            self.form_holder = tk.Frame(self.register_frame, bg="#FEA500")
            self.form_holder.place(relx=0.5, rely=0.5, relwidth="0.5", relheight="0.7", anchor=tk.CENTER)
        except:
            pass

    def city_register(self):
        self.options = tk.StringVar()

        # Set_up the main frame
        self.main_frame_setup()

        label_name = tk.Label(self.form_holder, text="Name:", bg="#FEA500")
        self.entry_name = tk.Entry(self.form_holder)

        label_date = tk.Label(self.form_holder, text="Data:", bg="#FEA500")
        self.entry_date = DateEntry(self.form_holder, selectmode="day")

        label_model = tk.Label(self.form_holder, text="Modelo:", bg="#FEA500")
        self.entry_model = tk.OptionMenu(self.form_holder, self.options, "M2C")

        label_link = tk.Label(self.form_holder, text="Link:", bg="#FEA500")
        self.entry_link = tk.Entry(self.form_holder)

        city_register_button = tk.Button(self.form_holder, text="Cadastrar Cidade", command=self.city_register_clicked)

        # placement for form elements
        label_name.place(relx=0.4, rely=0.3, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_name.place(relx=0.6, rely=0.3, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        label_date.place(relx=0.4, rely=0.4, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_date.place(relx=0.6, rely=0.4, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        label_model.place(relx=0.4, rely=0.5, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_model.place(relx=0.6, rely=0.5, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        label_link.place(relx=0.4, rely=0.6, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_link.place(relx=0.6, rely=0.6, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        city_register_button.place(relx=0.5, rely=0.8, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

    def city_register_clicked(self):
        # getting data
        city_name = self.entry_name.get()
        event_date = str(self.entry_date.get())
        model = self.options.get()
        link = self.entry_link.get()
        # cleaning the data from screen
        self.entry_name.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        # send data to main archive
        EventPublisher.publish("city_register_clicked", city_name, event_date, model, link, self)

    def model_register(self):
        # Set_up the main frame
        self.main_frame_setup()
        # set up data entry
        label_name = tk.Label(self.form_holder, text="Name:", bg="#FEA500")
        self.entry_name = tk.Entry(self.form_holder)

        label_archive = tk.Label(self.form_holder, text="Arquivo:", bg="#FEA500")
        self.entry_archive = tk.Entry(self.form_holder)

        label_link = tk.Label(self.form_holder, text="Link:", bg="#FEA500")
        self.entry_link = tk.Entry(self.form_holder)

        model_register_button = tk.Button(self.form_holder, text="Cadastrar Modelo",
                                          command=self.model_register_clicked)

        # placement for form elements
        label_name.place(relx=0.4, rely=0.3, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_name.place(relx=0.6, rely=0.3, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        label_archive.place(relx=0.4, rely=0.4, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_archive.place(relx=0.6, rely=0.4, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        label_link.place(relx=0.4, rely=0.5, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)
        self.entry_link.place(relx=0.6, rely=0.5, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        model_register_button.place(relx=0.5, rely=0.7, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

    def model_register_clicked(self):
        # getting data
        model_name = self.entry_name.get()
        model_archive = self.entry_archive.get()
        model_link = self.entry_link.get()
        # cleaning the data from screen
        self.entry_name.delete(0, tk.END)
        self.entry_archive.delete(0, tk.END)
        self.entry_link.delete(0, tk.END)
        # send data to main archive
        EventPublisher.publish("model_register_clicked", model_name, model_archive, model_link)

    def landing_page_generator(self):
        row_list = []
        self.main_frame_setup()
        self.form_holder.destroy()
        self.form_holder = tk.Frame(self.register_frame, bg="#FEA500")
        self.form_holder.place(relx=0.5, rely=0.5, relwidth="0.9445", relheight="0.7", anchor=tk.CENTER)
        with open("Archives/Assets/Data/input.csv", "r", encoding="utf-8") as f:
            self.table_rows = f.readlines()

        table_header = [
            "Select",
            "link",
            "model",
            "page_name",
            "city",
            "date",
            "link_tk",
            "active_name"
        ]
        canva_holder = tk.Frame(self.form_holder, bg="#FEA500")
        canva_holder.place(relx=0.5, rely=0.0, anchor=tk.N, relwidth=1.0, relheight=0.85)
        # Generate Canvas
        canvas = tk.Canvas(canva_holder, height=self.form_holder.winfo_reqheight(),
                           width=(self.form_holder.winfo_reqwidth() - 100), bg="#FEA500")
        canvas.pack(side=tk.TOP, anchor=tk.NE, fill=tk.BOTH, expand=True)

        # Setting up the ScrollBars
        horizontal_scrollbar = tk.Scrollbar(self.form_holder, orient=tk.HORIZONTAL, command=canvas.xview)
        horizontal_scrollbar.pack(side="bottom", fill="x")

        vertical_scrollbar = tk.Scrollbar(self.form_holder, orient=tk.VERTICAL, command=canvas.yview)
        vertical_scrollbar.pack(side="right", fill="y")

        canvas.configure(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)

        frame = tk.Frame(canvas, width="0")
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # Setting up the labels in the top row
        for col_index, column in enumerate(table_header):
            label_test = tk.Label(frame, text=f"{column}", bg="#FEA500", font=("Arial", "16", "bold"))
            label_test.grid(row=0, column=col_index, sticky="ew")

        # Make the actual table with selectors
        for row_index, row in enumerate(self.table_rows):
            column_list = []
            if row_index == 0:
                continue
            # Adding a checkbox for each row (selector)
            var = tk.IntVar()
            selector = tk.Checkbutton(frame, variable=var)
            selector.grid(row=row_index + 1, column=0, sticky="ew")
            self.table_columns = row.split(",")

            for col_index, column in enumerate(self.table_columns):
                entry_test = tk.Entry(frame, bg="#FEA500")
                entry_test.insert(tk.END, f"{column.strip()}")
                if col_index == len(self.table_columns) - 1:
                    entry_test.configure(width=50)
                entry_test.grid(row=(row_index + 1), column=col_index + 1, sticky="ew")
                column_list.append(entry_test)
            row_list.append((var, column_list))

        # Generate and position confirm and cancel buttons

        cancel_button = tk.Button(self.form_holder, text="Cancel", command=self.cancel_button_function)
        cancel_button.place(relx=0.2, rely=0.93, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        confirm_button = tk.Button(self.form_holder, text="Confirm",
                                   command=lambda: self.confirm_button_function(row_list))
        confirm_button.place(relx=0.8, rely=0.93, relwidth="0.3", relheight="0.05", anchor=tk.CENTER)

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Placeholder functions for confirm and cancel buttons

    def confirm_button_function(self, row_list):
        # create list of the selected rows
        selected_rows = []
        # iterate the rows
        for row_index, (var, entry_list) in enumerate(row_list):
            # check if the checkbox is selected
            if var.get() == 1:
                # retrieve data
                row_data = [entry.get() for entry in entry_list]
                selected_rows.append(row_data)
        # send it as a publisher
        EventPublisher.publish("lp_generation_confirm_button_pressed", selected_rows)

    def cancel_button_function(self):
        self.landing_page_generator()


class EventPublisher:
    observers = {}

    @classmethod
    def subscribe(cls, event, observer):
        if event not in cls.observers:
            cls.observers[event] = []
        cls.observers[event].append(observer)

    @classmethod
    def publish(cls, event, *args):
        if event in cls.observers:
            for observer in cls.observers[event]:
                observer(*args)

    @classmethod
    def unsubscribe(cls, event, observer):
        if event in cls.observers and observer in cls.observers[event]:
            cls.observers[event].remove(observer)
