import time
from selenium import webdriver


def getimage():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://picsum.photos/800')
    img = driver.
    driver.quit()
    return src


print(getimage())
