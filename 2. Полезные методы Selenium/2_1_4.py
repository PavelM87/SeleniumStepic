from selenium import webdriver
import math
from time import sleep


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(url)

try:
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer').send_keys(y)

    option1 = browser.find_element_by_css_selector("[type='checkbox']").click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()

    button = browser.find_element_by_css_selector("[type='submit']").click()
finally:
    sleep(20)
    browser.quit()