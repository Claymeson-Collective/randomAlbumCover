import time
from selenium import webdriver


def wikichop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s


def gettitle():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    driver.quit()
    return wikichop(driver.title, " - Wikipedia")


