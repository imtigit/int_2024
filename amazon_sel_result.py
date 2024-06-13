from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import re


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_amazon():
        driver = webdriver.Chrome()
        try:
            app_search = '//*[@id="twotabsearchtextbox"]'
            driver.implicitly_wait(10)
            driver.get('https://www.amazon.in')
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, app_search)))  #explicit wait
            driver.find_element(By.XPATH, app_search).send_keys('mobiles under 10000')
            driver.find_element(By.XPATH, app_search).click()

            driver.find_element(By.XPATH, "//input[contains(@id, 'nav-search-submit-button')]").click()
            page = driver.title
            print(page)
            output = driver.find_element(By.XPATH, "/html/body").text  # To print Enter test of page
            matchvalue = re.search('Results', output)
            if matchvalue:
                print(f'We are in amazon "{matchvalue.group()}" page')
        except Exception as e:
            print(e)
        finally:
            driver.quit()


