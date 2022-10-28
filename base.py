from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




username = "Reza Tanakizadeh"
password = "alaki"
name_of_login_page = 'Ghaen'
url = "F://Nimbra360_scrapping/temp/login.html"

# Define ChromeDriver
service = Service(executable_path="./driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open login page and check it
driver.get(url)
time.sleep(1)
if driver.title != name_of_login_page:
    print("--- logged before ---")
    driver.close()
    exit()


# Find login and pass input
inputs = driver.find_elements(By.TAG_NAME, "input")

# Pass data to login page
for inp in inputs:
    # Get name of inputs tag
    name_of_input = inp.get_attribute("name")

    # Check inputs name
    if name_of_input == 'login':    # For login
        inp.send_keys(password)
    elif name_of_input == 'passwd': # For password
        inp.send_keys(username)
    elif name_of_input == 'ok':
        login_buttun = inp

