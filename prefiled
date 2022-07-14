from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://88.214.35.93:8080/"

driver = webdriver.Chrome(executable_path="/Users/artemkharitidi/PycharmProjects/selenium/chrome/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)

    text_input = driver.find_element(By.ID, "myTextInput2")

    text = driver.find_element(By.ID, "myTextInput2").get_attribute("value")

    if text == ("Text..."):
        print('Prefield Text input field test: ok')
    else:
        print('Prefield Text input field test: error')

    text_input.send_keys("testtest")

    text = driver.find_element(By.ID, "myTextInput2").get_attribute("value")
    if text == ("Text...testtest"):
        print('After changePrefield ext input field test: ok')
    else:
        print('After change prefield Text input field test: error')

    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
