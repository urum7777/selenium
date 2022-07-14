from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

url = "http://88.214.35.93:8080/"

driver = webdriver.Chrome(executable_path="/Users/artemkharitidi/PycharmProjects/selenium/chrome/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)
    SelectDropdown = driver.find_element(By.ID, "mySelect")
    SelectDropdown_choice = SelectDropdown.get_attribute("value")
    if SelectDropdown_choice == "25%":
        print("Prechoice test:ok")
    else:
        print("Prechoice test:error")
        time.sleep(5)
    HTML_Meter_value = driver.find_element(By.ID, "meterBar").get_attribute("value")
    if HTML_Meter_value == "0.25":
        print("Prechoice meter test:ok")
    else:
        print("Prechoice meter test:error")

    # clic = ActionChains(driver).send_keys_to_element(SelectDropdown)
    # clic.perform()
    # time.sleep(4)
    # clic.perform()

except Exception as e:
    print(e, type(e))