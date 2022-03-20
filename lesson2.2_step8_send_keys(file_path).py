from selenium import webdriver
import time
import os
link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Cat")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Boris")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("milk@mail.ru")

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson2.2_step8_file.txt')       # добавляем к этому пути имя файла 
    element.send_keys(file_path)                                # отправляем файл

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
