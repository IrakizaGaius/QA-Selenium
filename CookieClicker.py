from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to the Chrome driver executable
chrome_driver_path = 'chromedriver.exe' # Replace with the actual path to chromedriver.exe

# Create a new instance of the Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(( By.XPATH, "//div[@id='langSelect-EN' and contains(@class, 'langSelectButton') and contains(@class, 'title')]"
)))

language = driver.find_element (By.XPATH, "//div[@id='langSelect-EN' and contains(@class, 'langSelectButton') and contains(@class, 'title')] "
)
language.click()

cookie_id = "bigCookie"
cookies_id = "cookies"
product_prefix_price = "productPrice"
product_prefix = "product"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_prefix_price + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue
        product_price= int(product_price)
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

time.sleep(10)

driver.quit