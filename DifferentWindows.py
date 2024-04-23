from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Specify the path to the Chrome driver executable
chrome_driver_path = 'chromedriver.exe' # Replace with the actual path to chromedriver.exe

# Create a new instance of the Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.flashscore.com/")
driver.maximize_window()
milan= "g_1_rNSNxFKQ"
cookies = "onetrust-accept-btn-handler"
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, cookies))
)

cookie= driver.find_element(By.ID, cookies)
cookie.click()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, milan))
)
match_1= driver.find_element(By.ID, milan)
match_1.click()

match_1_window = driver.window_handles[1]
driver.switch_to.window(match_1_window)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total Number of links on this page are: {len(all_links)}")
for link in all_links:
    href= link.get_attribute('href')
    if href and href.startswith(('http://', 'https://')):
        response = requests.head(href)
        if response.status_code !=200 :
            print (f"Broken link : {href} (Status code : {response.status_code})")

time.sleep(30)
driver.quit()
