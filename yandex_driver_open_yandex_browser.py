import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver_login():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = r'C:\Users\PerebeynosVV\yandexdriver.exe'
    service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.yandex.ru') #любой url  адрес
    yield driver
    driver.quit()

