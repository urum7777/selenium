import time

url = "http://88.214.35.93:8080/"

driver = webdriver.Chrome(executable_path="/Users/artemkharitidi/PycharmProjects/selenium/chrome/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)

    text_input = driver.find_element(By.ID, "placeholderText")

    placeholder_text = driver.find_element(By.ID, "placeholderText").get_attribute("placeholder")

    if placeholder_text == "Placeholder Text Field":
        print("Placeholder text test: ok")
    else:
        print("Placeholder text test: error")
    time.sleep(5)

    text_input.send_keys("None gray text")
    time.sleep(10)
    text = driver.find_element(By.ID, 'placeholderText').get_attribute("value")
    if text == "None gray text":
        print("after change test: ok")
    else:
        print("after change test: error")
        time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
