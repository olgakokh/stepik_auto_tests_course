from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("5")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
