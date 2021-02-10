from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


link = "https://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    answer = browser.find_element(By.ID, 'input_value').text
    inp = browser.find_element(By.ID, 'answer').send_keys(calc(answer))
    browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    print_answer(browser)
finally:
    sleep(10)
    browser.quit()