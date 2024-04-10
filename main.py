# main.py
import threading

from Archives.python.layout import MinhaInterface, EventPublisher
from Archives.python.models.OneForm import OneForm
from Archives.python.driver import DriveMethods, NotFoundException
from Archives.python.data_treatment import City
from Archives.python.data_treatment import Content
from tkinter import messagebox
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, UnexpectedAlertPresentException
from datetime import datetime


def error_popup(content):
    messagebox.showinfo("ATENÇÃO", message=content)


def handle_login_attempt(username, password):
    if username == "captacao" and password == "autenticar2024":
        app.main_screen()
        EventPublisher.unsubscribe("login_attempt", handle_login_attempt)


def handle_city_register(city_name, city_date, model, link, screen):
    if Content.is_empty(city_name):
        error_popup("Você esqueceu de preencher: O campo cidade")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(city_date):
        error_popup("Você esqueceu de preencher: O campo data do evento")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(model):
        error_popup("Você esqueceu de preencher: O campo modelo")
        MinhaInterface.city_register(screen)
        return
    elif Content.is_empty(link):
        error_popup("Você esqueceu de preencher: O campo link")
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
    new_data = f"\n{Content.sanitize_input(city_name)},{Content.sanitize_input(city_date)},{model},{link}"
    data.append(new_data)
    with open(address, "w", encoding="utf-8") as f:
        f.writelines(data)
    City.input_generator()


def handle_model_register(model_name, model_link, model_archive):
    print(model_name)
    print(model_link)
    print(model_archive)

def lp_gen(data):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("Archives/Assets/Data/city.csv", "r", encoding="utf-8") as f:
        city = f.readlines()
    if not any(data):
        error_popup("Você esqueceu de preencher: Cadastro de cidades")
        return
    cookies = DriveMethods.drive_gen()

    for line in data:
        new_drive = DriveMethods.clean_driver(cookies)
        try:
            print(line)
            handler = OneForm(new_drive)
            handler.page_clone(line[0])
            handler.locate_cloned_page()
            handler.rename_page(line[2])
            handler.edit_page(line)
            handler.insert_thanks_page_link(line[5])
            handler.config_active_campaign(line[6], line[4])
            handler.publish_page(line[3].strip()[:-5])

            # Remove the line containing the city name from the "city" list
            city = [c for c in city if line[3] not in c]

            # Write the modified "city" list back to the "city.csv" file
            with open("Archives/Assets/Data/city.csv", "w", encoding="utf-8") as f:
                f.writelines(city)
            new_drive.quit()
        except TimeoutException as e:
            with open("Erros.log", 'a', encoding="utf-8") as f:
                f.write(f"{line[3]} - {dt_string}\n\n{str(e)}\n\n\n\n\n")
                new_drive.quit()
                continue
        except UnexpectedAlertPresentException as e:
            with open("Erros.log", 'a', encoding="utf-8") as f:
                f.write(f"{line[3]} - {dt_string}\n\n{str(e)}\n\n\n\n\n")
                new_drive.quit()
                continue
        except StaleElementReferenceException as e:
            with open("Erros.log", 'a', encoding="utf-8") as f:
                f.write(f"{line[3]} - {dt_string}\n\n{str(e)}\n\n\n\n\n")
                new_drive.quit()
                print(str(e))
                continue
        except NotFoundException as e:
            error_popup(e.message)
            with open("Erros.log", 'a', encoding="utf-8") as f:
                f.write(f"{line[3]} - {dt_string}\n\n{str(e)}\n\n\n\n\n")
                new_drive.quit()
                print(str(e))
            continue


def handle_lp_generation(data):
    thread = threading.Thread(target=lp_gen, args=(data,))
    thread.daemon = True
    thread.start()

City.input_generator()

EventPublisher.subscribe("login_attempt", handle_login_attempt)
EventPublisher.subscribe("city_register_clicked", handle_city_register)
EventPublisher.subscribe("model_register_clicked", handle_model_register)
EventPublisher.subscribe("lp_generation_confirm_button_pressed", handle_lp_generation)

app = MinhaInterface()
app.login_screen()
app.janela.mainloop()
