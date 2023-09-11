
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\chrome\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://google.com")
driver.maximize_window()
time.sleep(2)

buscar = driver.find_element (By.ID, "APjFqb")
buscar.send_keys("Youtube")
buscar.send_keys(Keys.ENTER)
time.sleep(2)

Youtube = driver.find_element (By.CLASS_NAME,"VuuXrf")
Youtube.click()
time.sleep(2)

buscador = driver.find_element(By.NAME,"search_query")
buscador.send_keys("juegagerman")
clic = driver.find_element(By.ID,"search-icon-legacy")
clic.click()
time.sleep(2)

juegagerman = driver.find_element(By.CLASS_NAME,"style-scope ytd-video-renderer")
juegagerman.click()
time.sleep(5)
driver.quit()

