from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_webtable():
        driver = webdriver.Chrome()
        try:
            customer_table_allaccess = "//table[@id = 'customers']/tbody/tr[{}]/td[{}]"
            driver.get('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
            rows = len(driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr"))
            print(rows)
            for i in range(2, rows+1):
                col1 = driver.find_element(By.XPATH, customer_table_allaccess.format(i, 1)).text
                print(f'row number >>{i}---> Column element >> {col1}')
                col2 = driver.find_element(By.XPATH, customer_table_allaccess.format(i, 2)).text
                print(f'row number >>{i}---> Column element >> {col2}')
                col3 = driver.find_element(By.XPATH, customer_table_allaccess.format(i, 3)).text
                print(f'row number >>{i}---> Column element >> {col3}')
        except Exception as err:
            print(err)
        finally:
            driver.quit()


# if __name__ == '__main__':
#     unittest.main()
