# main.py
from Archives.python.layout import MinhaInterface, EventPublisher
from Archives.python.models.OneForm import OneForm
from Archives.python.driver import DriveMethods
def handle_city_register(city_name, city_date):
    pass


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

EventPublisher.subscribe("login_attempt", handle_login_attempt)
EventPublisher.subscribe("city_register_clicked", handle_city_register)
EventPublisher.subscribe("model_register_clicked", handle_model_register)
EventPublisher.subscribe("lp_generation_confirm_button_pressed", handle_lp_generation)

app = MinhaInterface()
app.login_screen()
app.janela.mainloop()
