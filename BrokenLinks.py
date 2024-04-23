from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Specify the path to the Chrome driver executable
chrome_driver_path = 'chromedriver.exe' # Replace with the actual path to chromedriver.exe

# Create a new instance of the Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
url= "https://www.tecno-mobile.com/rw/privacy-policy/"
driver.get(url)
driver.maximize_window()
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.TAG_NAME,'a'))
)

all_links= driver.find_elements(By.TAG_NAME, 'a')

print(f"Total number of links on the page : {len(all_links)}" )

for link in all_links:
    href= link.get_attribute('href')
    if href and href.startswith(('http://', 'https://')):
        response = requests.head(href)
        if response.status_code !=200 :
            print (f"Broken link : {href} (Status code : {response.status_code})")
        

time.sleep(30)
driver.quit()