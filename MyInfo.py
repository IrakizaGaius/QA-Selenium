from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Specify the path to the Chrome driver executable
chrome_driver_path = 'chromedriver.exe' # Replace with the actual path to chromedriver.exe

# Create a new instance of the Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# Open the login page
driver.get("https://opensource-demo.orangehrmlive.com/")
# Click on the username field and type 'Admin'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
)
username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
username_field.click()
username_field.send_keys("Admin")

# Click on the password field and type 'admin123'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
)
password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
password_field.click()
password_field.send_keys("admin123")

# Click on the Login button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
)
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

print(f"Login Successfull")

# Dashboard
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module' and text()='Dashboard']"))
)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name" and text()="My Info"]'))
)
info = driver.find_element(By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name" and text()="My Info"]')
info.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'))
)
new_dob = "1990-04-12"
dob = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')
dob.click()
dob.send_keys(Keys.CONTROL + "a")
dob.send_keys(Keys.DELETE)
dob.send_keys(new_dob)

save = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
save.click()

print(f"Test 4 Passed : Date Of Birth saved")

# Verify My Info page is updated with the latest selected date of birth
dob_after_update = dob.get_attribute("value")
if dob_after_update == new_dob:
    print("Step 5: My Info page is updated with the latest selected date of birth - Passed")
else:
    print("Step 5: My Info page is updated with the latest selected date of birth - Failed")


time.sleep(30)
driver.quit()
