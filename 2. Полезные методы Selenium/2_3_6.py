from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep


url = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.TAG_NAME, 'button').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value').text
    print(x)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    print_answer(browser)
finally:
    sleep(5)
    print(browser)
    browser.quit()


