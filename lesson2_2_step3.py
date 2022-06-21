from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    input1 = browser.find_element(By.ID, "dropdown")
    input1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[value=str(int(x)+int(y))]")
    option1.click()
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()