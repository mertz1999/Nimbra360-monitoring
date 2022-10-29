from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class StatusEqm():
    """
    Scrap temprature for Eqm page
    inputs:
        1. Driver
        2. url
    
    output:
        1. temprature
    """

    def __init__(self, driver : webdriver.Chrome, url):
        # Print information
        print(f'(Info) Start Status  Equipment({url})')        
    
        # Save parameters
        self.url        = url
        self.driver     = driver
    
    def start(self):  
        temprature = 0.0 
        # Open page 
        self.driver.get(self.url)
        time.sleep(1)

        # Get list of data included temprature
        list_of_data = self.driver.find_elements(By.XPATH,"//td[@class='left']")
        for data in list_of_data:
            splited_data = data.text.split(' ')
            if splited_data[-1] == '°C':
                temprature = splited_data[0]
 

        return float(temprature)
    




# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  StatusEqm(driver, "F://Nimbra360_scrapping/temp/status_eqm.html")

# result = temp.start()
# print(result)
# driver.close()
# exit()