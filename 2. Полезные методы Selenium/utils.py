import math
import pyperclip
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def copy_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    alert_text = alert.text.split()[-1]
    print(alert_text)
    pyperclip.copy(alert_text)
