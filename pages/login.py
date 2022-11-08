from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class Login():
    """
    Login class is used to enter username and password for other works
    Inputs:
        1. driver
        2. url : login url (ex. 10.50.60.2:8060/login.html)
        3. password
        4. usename
        5. login name: name of this nimbra (ex. Birjand)
    """

    def __init__(self, driver : webdriver.Chrome, url, password = 'password', username = 'admin', login_name = 'Ghaen'):
        # Print information
        print(f'(Info) Start login page ({login_name}) ({url})')
    
        # Save parameters
        self.url        = url
        self.password   = password 
        self.username   = username 
        self.login_name = login_name
        self.driver     = driver
    
    def start(self):       
        # Open login page and check it
        self.driver.get(self.url)
        time.sleep(1)
        
        # Find all inputs and then check to file login, password and submit buttun
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for inp in inputs:
            name_of_input = inp.get_attribute("name")  # Get name of inputs tag

            if name_of_input == 'login'    : inp.send_keys(self.username) # For send passwd
            elif name_of_input == 'passwd' : inp.send_keys(self.password) # For send username
            elif name_of_input == 'ok'     : login_buttun = inp           # Submit login form

        login_buttun.click()
        print("(Info) Login is completed!")

        return True




# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  Login(driver, "F://Nimbra360_scrapping/temp/login.html")

# temp.start()
# driver.close()
# exit()