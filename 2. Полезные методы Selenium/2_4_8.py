import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from utils import calc, copy_answer


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
)
browser.find_element(By.ID, 'book').click()

x = browser.find_element(By.ID, 'input_value').text

browser.find_element(By.ID, 'answer').send_keys(calc(x))

browser.find_element(By.ID, 'solve').click()

copy_answer(browser)

browser.quit()
