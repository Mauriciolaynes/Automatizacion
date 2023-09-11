import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestSelenium(unittest.TestCase):

    def setUp(self):
        service = Service ('C:\chrome\chromedriver-win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)

    def test_busqueda_google(self):
        buscar = self.driver
        buscar.get("https://www.google.com")
        time.sleep(1)
        buscar.find_element(By.NAME, "q").send_keys("Youtube")
        buscar.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        time.sleep(1)   
        buscar.find_element(By.CLASS_NAME, "XNo5Ab").click()
        time.sleep(2)
        self.assertIn("YouTube", buscar.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()