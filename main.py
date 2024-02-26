# main.py
from Archives.python.layout import MinhaInterface, EventPublisher
from Archives.python.models.OneForm import OneForm
from Archives.python.driver import DriveMethods
from Archives.python.data_treatment import City
from Archives.python.data_treatment import Content
from tkinter import messagebox


def error_popup(content):
    messagebox.showinfo("ATENÇÃO", f"Você esqueceu de preencher o campo: {content}")


def handle_city_register(city_name, city_date, model, link, screen):
    if Content.is_empty(city_name):
        error_popup("Cidade")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(city_date):
        error_popup("Data do evento")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(model):
        error_popup("Modelo")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(link):
        error_popup("Link")
        MinhaInterface.city_register(screen)
        return
    month, day, year = city_date.split("/")
    if int(day) < 10:
        day = f"0{day}"
    if int(month) < 10:
        month = f"0{month}"
    city_date = f"{month}/{day}/{year}"
    data = []
    address = "Archives/Assets/Data/city.csv"
    with open(address, "r", encoding="utf-8") as f:
        tmp_data = f.readlines()
        for line in tmp_data:
            if line.strip() != "":
                data.append(line)
    new_data = f"\n{Content.sanitize_input(city_name)},{Content.sanitize_input(city_date)},{Content.sanitize_input(model)},{Content.sanitize_input(link)}"
    data.append(new_data)
    with open(address, "w", encoding="utf-8") as f:
        f.writelines(data)
    City.input_generator()


def handle_model_register(model_name, model_link, model_archive):
    print(model_name)
    print(model_link)
    print(model_archive)


def handle_login_attempt(username, password):
    if username == "captacao" and password == "autenticar2024":
        app.main_screen()
        EventPublisher.unsubscribe("login_attempt", handle_login_attempt)


def handle_lp_generation(data):
    drive = DriveMethods.drive_gen()
    for line in data:
        print(line)
        handler = OneForm(drive)
        handler.page_clone(line[0])
        handler.locate_cloned_page()
        handler.rename_page(line[2])
        handler.edit_page(line)
        handler.insert_thanks_page_link(line[5])
        handler.config_active_campaign(line[6], line[4])
        handler.publish_page(line[3].strip()[:-5])


City.input_generator()

EventPublisher.subscribe("login_attempt", handle_login_attempt)
EventPublisher.subscribe("city_register_clicked", handle_city_register)
EventPublisher.subscribe("model_register_clicked", handle_model_register)
EventPublisher.subscribe("lp_generation_confirm_button_pressed", handle_lp_generation)

app = MinhaInterface()
app.login_screen()
app.janela.mainloop()
