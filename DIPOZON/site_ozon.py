# Создаем базовый класс для тестирования веб-приложения LITRES

import pytest
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


with open(r"C:\Users\user\Desktop\pythonProject1\DIPOZON\config.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser1']

# Создадим класс, который будет управлять сайтом
class SiteOzon:
    # Инициализация сайта
    def __init__(self, address):
        # инициализация драйвера
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()

            self.driver = webdriver.Chrome(service=service, options=options)
        # добавим ожидание
        self.driver.implicitly_wait(3)
        # откроем браузер развернутым на весь экран
        self.driver.maximize_window()
        # откроем адрес сайта
        self.driver.get(address)
        # подождем некоторое время, кот указано в config
        time.sleep(testdata['sleep_time'])

    def find_field(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    # def enter_param_in_field(self, mode, path, param_for_enter):
    #     # отправляем искомый параметр в поле
    #     element = self.find_field(mode, path)
    #     element.send_keys(param_for_enter)
    #     # element.send_keys(Keys.ENTER)
    #     return element

    def close_browser(self):
        self.driver.close()

# SiteOzon(address)