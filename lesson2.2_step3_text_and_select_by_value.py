from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1_element = browser.find_element_by_id("num1")
    num1 = num1_element.text
    num2_element = browser.find_element_by_id("num2")
    num2 = num2_element.text
    y = str(int(num1) + int(num2))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    buttin = browser.find_element_by_class_name("btn-default")
    buttin.click()

finally:
    time.sleep(5)
    browser.quit()
