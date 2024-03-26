from time import sleep

import pyautogui
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OneForm:
    wait = None
    drive = None
    actions = None
    city_data = []
    month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio',
                  '06': 'Junho',
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro',
                  '12': 'Dezembro'}

    @classmethod
    def __init__(cls, drive):
        cls.drive = drive
        cls.actions = ActionChains(drive)
        cls.wait = WebDriverWait(drive, 30)

    @classmethod
    def click(cls, by, path, timer=5):
        temp_wait = WebDriverWait(cls.drive, timer)
        sleep(1)
        element = temp_wait.until(EC.presence_of_element_located((by, path)))
        element.click()

    @classmethod
    def page_clone(cls, link):
        print(link)
        cls.drive.get(link)
        cls.click(By.XPATH, '//*[@id="admin_centro_area-acoes"]/div[3]/div', 5)
        cls.click(By.XPATH, '//*[@id="dropdown_1"]/ul/li[3]/span', 5)
        sleep(5)
        cls.click(By.XPATH, '//*[@id="admin_topo_basico_logotipo"]', 5)

    @classmethod
    def locate_cloned_page(cls):
        sleep(2)
        try:
            page = WebDriverWait(cls.drive, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), '00_00[MES/ANO] [M2C] [LARANJA] PALESTRA ABERTA - Cópia')]")))
        except Exception as e:
            print(e)
            searcher = cls.wait.until(
                EC.presence_of_element_located(((By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/div/input"))))
            searcher.click()
            searcher.send_keys("[MES/ANO] [M16] PALESTRA AO VIVO REVELA: CIDADE - Cópia")
            page = WebDriverWait(cls.drive, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), '[MES/ANO] [M16] PALESTRA AO VIVO REVELA: CIDADE - Cópia')]")))
        page.click()
        sleep(3)

    @classmethod
    def rename_page(cls, page_name=None):
        cls.click(By.XPATH, '//*[@id="admin_centro_area-acoes"]/div[3]/div')
        element = WebDriverWait(cls.drive, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown_1"]/ul/li[1]/span')))
        element.click()

        name_input = WebDriverWait(cls.drive, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="titulo"]')))
        name_input.clear()

        name_input.send_keys(page_name)
        sleep(2)
        cls.click(By.XPATH, '//*[@id="enviar_formulario_ajax"]')

    @classmethod
    def input_info(cls, data):
        month, day, year = data[4].split('-')
        pyperclip.copy(f'{day} de {cls.month_dict[month].capitalize()}')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('Dia: ')
        pyautogui.press('end')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')
        pyautogui.press('end')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('Enter')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')

        flicker = False
        neighborhood = ['Bairro', 'bairro', '(bairro)', '(Bairro)']
        for nbh in neighborhood:
            if not flicker:
                if nbh in data[3]:
                    flicker = True

        if flicker:
            value = data[3][:-5]
            value = value.replace('(Bairro)', '')
            value = value.replace('Bairro', '')
            pyperclip.copy(value)
            pyautogui.write('Bairro: ')
            pyautogui.press('end')
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')
            pyautogui.press('end')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')
        else:
            pyperclip.copy(data[3][:-5])
            pyautogui.write('Cidade: ')
            pyautogui.press('end')
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')
            pyautogui.press('end')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')

        pyperclip.copy('Hor\u00E1rio: ')
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('Às 19:30h')
        pyautogui.press('end')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')
        pyautogui.press('end')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('Enter')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')

        pyperclip.copy('1Kg de alimento não perecível')
        pyautogui.write('Entrada: ')
        pyautogui.press('end')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')
        pyautogui.press('end')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('Enter')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')

        pyperclip.copy('Endereço: ')
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('Será enviado por E-mail e WhatsApp')
        pyautogui.press('end')
        pyautogui.keyDown('ctrl')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')
        pyautogui.press('end')
        pyautogui.hotkey('ctrl', 'v')

    @classmethod
    def edit_page(cls, data):
        cls.click(By.XPATH, '//*[@id="admin_botao_editar_pagina"]/span[2]')
        sleep(2)
        cls.click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[4]/div[1]')
        cls.click(By.XPATH, '//*[@id="gpc-blocos_editor"]/div[9]/span[1]')
        cls.input_info(data)

    @classmethod
    def insert_thanks_page_link(cls, data):
        forms = cls.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "form")))
        for form in forms:
            # Click on the form
            cls.actions.double_click(form)
            cls.actions.perform()
            # Release the click to allow further actions
            cls.actions.release()
            cls.actions.reset_actions()
            config = cls.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Configurar')]")))
            config.click()
            element = WebDriverWait(cls.drive, 30).until(EC.element_to_be_clickable((By.ID, 'link_redirecionar')))
            element.click()
            element.clear()
            element.send_keys(data)
            sleep(2)

    @classmethod
    def config_active_campaign(cls, active, date):
        month, day, year = date.split("-")
        # open the activeCampaign connectio editor
        cls.click(By.XPATH, '/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[2]/div[1]')
        sleep(3)
        # Click the main integration selector
        cls.click(By.XPATH, '//*[@id="10770"]/span[2]/span[1]', 20)
        sleep(3)
        # click proceed button
        cls.click(By.XPATH, '//*[@id="gmf_100000"]/div[4]/span[1]', 20)
        sleep(3)
        # Select the list
        sleep(25)
        list_name = f"PALESTRA ABERTA - {cls.month_dict[month][:3].upper()}/{year}".strip()
        print(list_name)
        element = WebDriverWait(cls.drive, 120).until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{list_name}')]")))
        element.click()
        sleep(2)
        element.click()
        sleep(2)
        cls.click(By.XPATH, '//*[@id="gmf_100000"]/div[4]/span[1]')
        # Select the tag
        input_area = WebDriverWait(cls.drive, 30).until(
            EC.presence_of_element_located((By.ID, "id_integracao_tags_busca")))
        input_area.click()
        input_area.send_keys(active)
        sleep(5)
        elements = WebDriverWait(cls.drive, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'radio')))

        for element in elements:
            if element.text == active:
                element.click()
        cls.click(By.XPATH, '//*[@id="gmf_100000"]/div[4]/span[1]')
        sleep(3)
        cls.click(By.XPATH, '//*[@id="enviar_formulario_ajax"]')
        sleep(1)
        cls.click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div')

    @classmethod
    def publish_page(cls, name):
        sleep(10)
        element = WebDriverWait(cls.drive, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="admin_topo_basico_voltar"]')))
        element.click()
        sleep(10)
        # click on publish
        element = WebDriverWait(cls.drive, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pagina_situacao"]/div[2]')))
        element.click()

        # Put the link
        sleep(5)
        link = WebDriverWait(cls.drive, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pagina_link"]')))
        link.click()
        link.send_keys(name)

        # change the host
        try:
            element = WebDriverWait(cls.drive, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "leonardo-brandi")]')))
            element.click()

            element = WebDriverWait(cls.drive, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "palestra.polozi.com.br")]')))
            element.click()
        except:
            pass

        # Confirming
        try:

            element = WebDriverWait(cls.drive, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="enviar_formulario_ajax"]')))
            element.click()
        except:
            element = WebDriverWait(cls.drive, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="aviso_mobile_publicar"]')))
            element.click()
            sleep(2)
            element = WebDriverWait(cls.drive, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="gd_2"]/div[3]/div[1]')))
            element.click()
        sleep(25)
