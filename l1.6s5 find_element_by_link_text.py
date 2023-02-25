from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "https://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
time.sleep(5)
browser.get(link)
x = browser.find_element(By.LINK_TEXT, '224592')
x.click()
input1 = browser.find_element(By.TAG_NAME, 'input')
input1.send_keys("q")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("q")
input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
input3.send_keys("q")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("q")
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(15)
# закрываем браузер после всех манипуляций
browser.quit()
# не забываем оставить пустую строку в конце файла