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
dashboard = driver.window_handles[0]
driver.switch_to.window(dashboard)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module' and text()='Dashboard']"
))
)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-userdropdown-tab'))
)
icon = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-tab')
icon.click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.oxd-dropdown-menu'))
)
# Logout
profile_dropdown = driver.find_element(By.CSS_SELECTOR, '.oxd-dropdown-menu')
# Hover over the profile dropdown
ActionChains(driver).move_to_element(profile_dropdown).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
)
# Click on the Logout button
logout_button = driver.find_element(By.LINK_TEXT, "Logout")
logout_button.click()
# Validate logout
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title' and text()='Login']"
))
)
login_page_title = driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title' and text()='Login']").text
print(f"Login Page Title: {login_page_title}")
if "Login" in login_page_title:
    print("Test Case 3: Logout - Passed")
else:
    print("Test Case 3: Logout - Failed")

time.sleep(10)
# Close the browser
driver.quit()
