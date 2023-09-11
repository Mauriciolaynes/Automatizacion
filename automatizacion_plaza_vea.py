from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time

class TestSelenium (unittest.TestCase):

    def setUp (self):
        service = Service ('C:\chrome\chromedriver-win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(3)

    def testing (self):
        driver = self.driver
        driver.get("https://www.plazavea.com.pe/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"Header__user__login").click()
        time.sleep(1)
        driver.find_element(By.ID,"vtexIdUI-google-plus").click()
        time.sleep(1)
        driver.find_element(By.ID,"identifierId").send_keys("mauriciolaynescastro@gmail.com")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"whsOnd zHQkBf").send_keys("123")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()