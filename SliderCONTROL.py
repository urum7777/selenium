from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://88.214.35.93:8080/"

driver = webdriver.Chrome(executable_path="/Users/artemkharitidi/PycharmProjects/selenium/chrome/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)

    slider_control = driver.find_element(By.ID, "mySlider")
    position_of_slider = slider_control.get_attribute("Value")
    if position_of_slider == "50":
        print("Slider test: ok")
    else:
        print("Slider test: error")

    hover = ActionChains(driver).move_to_element(slider_control)
    hover.perform()
    time.sleep(5)
    progress_bar = driver.find_element(By.ID, "progressBar").get_attribute("value")

    if progress_bar == "50":
        print("Progress bar test: ok")
    else:
        print("Progress bar test: error")




    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
