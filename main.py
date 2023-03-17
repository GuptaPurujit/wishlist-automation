from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "<enter-site-url>"
options = webdriver.ChromeOptions()
options.add_argument('--headless')

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
    for i in range(1,10):
        email = "johndoe_" + str(i) + "@gmail.com"
        driver.get(url)
        print("Page URL:", driver.current_url)
        print("Page Title:", driver.title)
        input_text_box = driver.find_element(By.XPATH, "<enter xpath of the input text box>")
        click_button = driver.find_element(By.XPATH, "<enter xpath of the submit button>")
        input_text_box.click()
        input_text_box.send_keys(email)
        print(f"Entering email: {email}")
        time.sleep(5)
        print("Submitting")
        click_button.click()
        print("Wating 5 seconds before opening new table")
        time.sleep(5)
