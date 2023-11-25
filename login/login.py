from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "YourFacebookEmail@example.com"
password = "YourFacebookPassword"

driver_path = 'C:/Users/chromedriver.exe'
chrome_service = webdriver.chrome.service.Service(driver_path)

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.facebook.com")

username_field = driver.find_element("id", "email")
password_field = driver.find_element("id", "pass")

# Enter your username and password
username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("https://www.facebook.com/profile.php")
time.sleep(10)

# Close the browser window
driver.quit()
