import time
import math
import pytest
from selenium import webdriver


ufo_msg = ''

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(ufo_msg)


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_ufo_messages(browser, link):
    global ufo_msg
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('.string-quiz__textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission').click()
    msg = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert msg == "Correct!", 'Инопланетяне шалят!'
    except AssertionError:
        ufo_msg += msg

#  pytest -s -v test_fixture_3_6_3.py
