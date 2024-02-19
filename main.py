# main.py
from layout import MinhaInterface, EventPublisher


def handle_login_data(username, password, login_frame):
    if username == "asd" and password == "asd":
        return True
    else:
        return False


def handle_city_register(city_name, city_date):
    print(city_name)
    print(city_date)

def handle_model_register(model_name, model_link, model_archive):
    print(model_name)
    print(model_link)
    print(model_archive)


def handle_login_attempt(username, password):
   if username == "asd" and password == "asd":
       app.main_screen()


EventPublisher.subscribe("login_attempt", handle_login_attempt)
EventPublisher.subscribe("city_register_clicked", handle_city_register)
EventPublisher.subscribe("model_register_clicked", handle_model_register)

app = MinhaInterface()
app.login_screen()
app.janela.mainloop()
