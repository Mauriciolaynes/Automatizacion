from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service ('C:\chrome\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com")
time.sleep(1)

registrarse = driver.find_element(By.ID, "buttons").click()
time.sleep(1)
registrarse = driver.find_element(By.CLASS_NAME, "XOrBDc").click()
registrarse = driver.find_element(By.CLASS_NAME, "VfPpkd-StrnGf-rymPhb-b9t22c").click()
time.sleep(1)
registrarse = driver.find_element(By.ID,"firstName").send_keys("Pedro")
time.sleep(1)
registrarse = driver.find_element(By.ID,"lastName").send_keys("Castro Perez")
time.sleep(1)
registrarse = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
time.sleep(1)
registrarse = driver.find_element(By.ID,"day").send_keys("10")
time.sleep(1)
registrarse = driver.find_element(By.ID, "month").click()
registrarse = driver.find_element(By.XPATH, '//*[@id="month"]/option[11]').click()
registrarse = driver.find_element(By.ID,"year").send_keys("2000")
registrarse = driver.find_element(By.ID, "gender").click()
registrarse = driver.find_element(By.XPATH, '//*[@id="gender"]/option[3]').click()
registrarse = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
time.sleep(1)
registrarse = driver.find_element(By.ID,"identifierId").send_keys("castro_laynes@hotmail.com")
registrarse = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
time.sleep(1)
registrarse = driver.find_element(By.ID,"code").send_keys("123456")

time.sleep(5)

driver.quit()


