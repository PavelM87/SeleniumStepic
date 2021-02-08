from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    answer = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(answer))

    browser.find_element_by_tag_name('button').click()

    print_answer(browser)

finally:
    sleep(15)
    browser.quit()
