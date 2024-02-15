# main.py
from layout import MinhaInterface

def handle_login_data(username, password, login_frame):
    if username == "asd" and password == "asd":
        return True
    else:
        return False

app = MinhaInterface()
app.login_screen(handle_login_data)
app.janela.mainloop()
