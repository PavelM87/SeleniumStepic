import unittest
from selenium import webdriver


class TestSelectorUnique(unittest.TestCase):

    def connect_and_input(self, url):
        # подключаемся
        browser = webdriver.Chrome()
        browser.get(url)
        browser.implicitly_wait(5)
        # заполняем обязательные поля
        browser.find_element_by_css_selector('.first_block .first').send_keys("Ivan")
        browser.find_element_by_css_selector('.first_block .second').send_keys("Ivanov")
        browser.find_element_by_css_selector('.third_class .third').send_keys("Ivanivanov@mail.ru")
        # жмем кнопку и запоминаем появившийся текст
        browser.find_element_by_css_selector("button.btn").click()
        text = browser.find_element_by_tag_name("h1").text
        browser.quit()
        return text

    def test_registration1(self):

        url = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual("Congratulations! You have successfully registered!",
                         self.connect_and_input(url), 'Unsuccessful registration!')

    def test_registration2(self):

        url = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual("Congratulations! You have successfully registered!",
                         self.connect_and_input(url), 'Unsuccessful registration!')


if __name__ == "__main__":
    unittest.main()
