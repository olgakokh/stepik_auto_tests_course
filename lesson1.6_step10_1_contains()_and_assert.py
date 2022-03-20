from selenium import webdriver
import time

link = "https://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath('//input[contains(@placeholder, "first")]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[contains(@placeholder, "last")]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[contains(@placeholder, "email")]')
    input3.send_keys("molensk@ya.ry")
    input4 = browser.find_element_by_xpath('//input[contains(@placeholder, "phone")]')
    input4.send_keys("758426")
    input5 = browser.find_element_by_xpath('//input[contains(@placeholder, "address")]')
    input5.send_keys("Tomsk, Krasnaya Street, 18, 35")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    