from selenium import webdriver
from time import sleep

try:
    link_old = 'http://suninjuly.github.io/registration1.html'
    link_new = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link_old)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    sleep(1)

    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Ivanov")
    sleep(1)

    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("Ivanivanov@mail.ru")
    sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
