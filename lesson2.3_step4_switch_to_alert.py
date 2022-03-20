from selenium import webdriver
import time
import math


try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("//button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_class_name("btn")
    button2.click()
    print(browser.switch_to.alert.text)


finally:
    time.sleep(7)
    browser.quit()
