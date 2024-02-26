# main.py
from Archives.python.layout import MinhaInterface, EventPublisher
from Archives.python.models.OneForm import OneForm
from Archives.python.driver import DriveMethods
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio',
              '06': 'Junho',
              '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro',
              '12': 'Dezembro'}


def input_generator():
    header = "link,model,page_name,city,date,link_tk,active_name\n"
    data = [header]

    with open("Archives/Assets/Data/city.csv", "r", encoding="utf-8") as f:
        tmp = f.readlines()[1:]  # Skip the header line
        print(tmp)

    for line in tmp:
        city, date, model, link = map(str.strip, line.split(','))
        month, day, year = date.split('/')
        page_name = f"[{month_dict[month][:3]}/{year}] [{model}] [{city}] PALESTRA ABERTA - AUTO".upper()
        link_tk = f"https://palestra.polozi.com.br/obg-{remove_accents(city.lower().replace(' ', '-'))}-{month_dict[month][:3].lower()}"
        active_name = f"{day}/{month}/{year} - {city.lower()} - palestra aberta"
        content = f"{link},{model},{page_name},{city},{date},{link_tk},{active_name}\n"
        print(content)
        data.append(content)

    with open("Archives/Assets/Data/input.csv", "w", encoding="utf-8") as f:
        f.writelines(data)


def handle_city_register(city_name, city_date, model, link):
    data = []
    address = "Archives/Assets/Data/city.csv"
    with open(address, "r", encoding="utf-8") as f:
        tmp_data = f.readlines()
        for line in tmp_data:
            if line.strip() != "":
                data.append(line)
    new_data = f"\n{city_name},{city_date},{model},{link}"
    data.append(new_data)
    with open(address, "w", encoding="utf-8") as f:
        f.writelines(data)
    input_generator()


def handle_model_register(model_name, model_link, model_archive):
    print(model_name)
    print(model_link)
    print(model_archive)


def handle_login_attempt(username, password):
    if username == "asd" and password == "asd":
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


input_generator()

EventPublisher.subscribe("login_attempt", handle_login_attempt)
EventPublisher.subscribe("city_register_clicked", handle_city_register)
EventPublisher.subscribe("model_register_clicked", handle_model_register)
EventPublisher.subscribe("lp_generation_confirm_button_pressed", handle_lp_generation)

app = MinhaInterface()
app.login_screen()
app.janela.mainloop()
