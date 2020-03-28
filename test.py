import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://en.wikipedia.org/wiki/Special:Random')
randomHeading = driver.find_elements_by_name('firstHeading')[0]
randomTitle = randomHeading.text

driver.quit()
