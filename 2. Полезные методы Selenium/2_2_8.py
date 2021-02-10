from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    f_name = browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    l_name = browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    email = browser.find_element(By.NAME, 'email').send_keys('Ivan@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '../example.txt')

    send_file = browser.find_element(By.NAME, 'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()

    print_answer(browser)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
finally:
    sleep(10)
    browser.quit()


