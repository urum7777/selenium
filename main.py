from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://88.214.35.93:8080/"

driver = webdriver.Chrome(executable_path="/Users/artemkharitidi/PycharmProjects/selenium/chrome/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)

    text_input = driver.find_element(By.ID, "myTextInput")
    text_input.send_keys("text")

    time.sleep(5)

    text = driver.find_element(By.ID, "myTextInput").get_attribute("value")
    if text == ("text"):
        print('Text input field test: ok')
    else:
        print('Text input fiels test: error')

    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
