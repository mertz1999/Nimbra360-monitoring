from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class PMOverview():
    """
    Scrap TRUNK informtions.

    """

    def __init__(self, driver : webdriver.Chrome, url):
        # Print information
        print(f'(Info) Start PM Overview (Trunk) ({url}) ')        
    
        # Save parameters
        self.url        = url
        self.driver     = driver
    
    def start(self):  
        result = {
            'ES'  : [],
            'SES' : [],
            'UAS' : [],
            'SS'  : [],
        }
        # Open page 
        self.driver.get(self.url)
        time.sleep(1)

        # Get list of rows
        rows = self.driver.find_elements(By.XPATH,"//tr[@class='row']")

        # Get columns 7,8,9,10
        for row in rows:
            # We need columns: ES:7, SES:8, UAS:9, SS:0
            cols = row.find_elements(By.TAG_NAME,"td")

            # Save informations
            result['ES'].append(int(cols[7].text))
            result['SES'].append(int(cols[8].text))
            result['UAS'].append(int(cols[9].text))
            result['SS'].append(int(cols[10].text))
            


        return result

    def sp_print(self,result):
        print(f"+ Trunk monitoring results:")
        print(f"   - ES  : {result['ES']}")
        print(f"   - SES : {result['SES']}")
        print(f"   - BBE : {result['UAS']}")
        print(f"   - SS  : {result['SS']}")



# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  PMOverview(driver, "F://Nimbra360_scrapping/temp/pm_overview.html")

# result = temp.start()
# print(result)
# driver.close()
# exit()