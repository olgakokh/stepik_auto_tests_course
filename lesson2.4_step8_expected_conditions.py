from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
