from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class PMDetails():
    """
    Track TS Flag

    Input:
        1. Driver
        2. URL
        3. Date
    
    Output:
        1. result -> ES, SES, BBE, UAS

    """

    def __init__(self, driver : webdriver.Chrome, url, date='20 Oct 2021'):
        # Print information
        print(f' ################## Start PM Details ({url}) ################## ')        
    
        # Save parameters
        self.url        = url
        self.driver     = driver
    
        # Split date
        self.date = date.split(' ') # Day, month, year

    def start(self):
        # Result
        result = {
            'ES'  : 0,
            'SES' : 0,
            'BBE' : 0,
            'UAS' : 0,
            }
        # Open page 
        self.driver.get(self.url)
        time.sleep(1)

        # Get list of rows
        rows = self.driver.find_elements(By.XPATH,"//tr[@class='row']")

        # Get columns
        for row in rows[0:-3]:
            cols = row.find_elements(By.TAG_NAME,"td")
            
            # Check date and then sum flags value
            date_column = cols[0].text.split(' ')
            if date_column[0] == self.date[1] and date_column[1] == self.date[0]:
                result['ES']  += int(cols[3].text)
                result['SES'] += int(cols[4].text)
                result['BBE'] += int(cols[5].text)
                result['UAS'] += int(cols[6].text)

            
        return result




# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  PMDetails(driver, "F://Nimbra360_scrapping/temp/pm_details.html?dch.1", '5 Oct 2021')

# result = temp.start()
# print(result)
# driver.close()
# exit()