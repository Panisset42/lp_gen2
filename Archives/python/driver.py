from selenium import webdriver
from selenium.webdriver.common.by import By


class DriveMethods:
    @classmethod
    def drive_gen(cls):
        # get login info
        user_account = "polozi.scripts@gmail.com"
        user_pass = "RnUYz91K"
        # instantiate driver and go to the site
        driver = webdriver.Chrome()
        driver.get('https://app.greatpages.com.br/login')
        # get camps and making login
        user_input = driver.find_element(By.XPATH, "//*[@id=\"usuario\"]")
        pass_input = driver.find_element(By.XPATH, "//*[@id=\"senha\"]")
        user_input.send_keys(user_account)
        pass_input.send_keys(user_pass)
        pass_input.submit()
        # returning driver
        return driver
