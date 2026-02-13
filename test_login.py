from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    print("Opening login page...")
    driver.get("https://the-internet.herokuapp.com/login")

    # wait for full page load
    wait = WebDriverWait(driver, 20)

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    print("Login success")

    driver.save_screenshot("login_success.png")

    driver.find_element(By.LINK_TEXT, "Logout").click()

    print("Logout success")
    time.sleep(2)

except Exception as e:
    print("ERROR:", e)

finally:
    driver.quit()
    print("Browser closed")
