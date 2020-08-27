from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = 'G:\FliproboAssgn\chromedriver_win32\Chromedriver.exe'
browser = webdriver.Chrome(executable_path = DRIVER_PATH)

search = ['nature']
for book in search:
  browser.get('https://www.google.com/imghp')
  e = browser.find_element_by_name('q')
  e.send_keys(search)
  e.send_keys(Keys.ENTER)
