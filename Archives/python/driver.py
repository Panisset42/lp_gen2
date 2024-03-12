import selenium.common.exceptions as SE
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options


class DriveMethods:
    @classmethod
    def drive_gen(cls):
        # get login info
        user_account = "polozi.scripts@gmail.com"
        user_pass = "RnUYz91K"
        #chrome_options = Options()

        # Add the --headless option
        #chrome_options.add_argument("--headless")

        # Create the headless Chrome driver
        driver = webdriver.Chrome()
        driver.get('https://app.greatpages.com.br/login')
        # get camps and making login
        user_input = driver.find_element(By.XPATH, "//*[@id=\"usuario\"]")
        pass_input = driver.find_element(By.XPATH, "//*[@id=\"senha\"]")
        user_input.send_keys(user_account)
        pass_input.send_keys(user_pass)
        pass_input.submit()
        sleep(3)
        cookies = driver.get_cookies()
        # returning driver
        return cookies
    @classmethod
    def clean_driver(cls, cookies):

        # Create a new driver
        driver = webdriver.Chrome()

        driver.get('https://app.greatpages.com.br/')
        # Add cookies to the new driver
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        return driver
