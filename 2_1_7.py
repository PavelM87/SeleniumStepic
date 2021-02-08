from selenium import webdriver
import math
from time import sleep


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    treasure = browser.find_element_by_id('treasure').get_attribute('valuex')

    answer = calc(treasure)

    _input = browser.find_element_by_id('answer').send_keys(answer)

    check = browser.find_element_by_id('robotCheckbox').click()

    radio = browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_css_selector('.btn.btn-default').click()

    print_answer(browser)
finally:
    sleep(20)
    browser.quit()

