from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class DTMInterface():
    """
    Get DTM information from ftm_interface.html file
    In this class we get images (gray and green) and then find that RX and TX are work correctly or not

    Inputs:
        1. Driver
        2. URL
    
    Outputs:
        1. DTM: A dictionary that have TX and RX keys

    """

    def __init__(self, driver : webdriver.Chrome, url):
        # Print information
        print(f'(Info) Start DTM Interface ({url})')        
    
        # Save parameters
        self.url        = url
        self.driver     = driver
    
    def start(self):  
        # Result data
        DTM = {
            'TX' : False,
            'RX' : False,
        }

        # Open page 
        self.driver.get(self.url)
        time.sleep(1)

        # Get list of rows
        rows = self.driver.find_elements(By.XPATH,"//tr[@class='row']")
        
        # Get TX and RX data
        for row in rows:
            # If Rx and Tx is Ok break total loops
            if DTM['RX'] == True and DTM['TX'] == True: break

            # Get all columns for each row
            selected_cols = row.find_elements(By.TAG_NAME,"td")
            selected_RX_TX = [selected_cols[i] for i in [4,7]]   # needed Cols are in index 4,7 (index 0 is for TX, index 1 is for RX)

            # Check RX and TX is ok based on images
            for idx, col in enumerate(selected_RX_TX):
                if   idx == 0 and DTM['TX'] == True: continue
                elif idx == 1 and DTM['RX'] == True: continue 

                # labels (images gray and green)
                labels = col.find_elements(By.XPATH,'.//*[@class="per"]')
                for label in labels:
                    image_format = label.get_attribute('src')[-3:]   # png->cleared, jpg->gray
                    if   image_format == 'png' and idx == 0: DTM['TX'] = True
                    elif image_format == 'png' and idx == 1: DTM['RX'] = True

        return DTM
    
    def sp_print(self,DTM):
        print("+ DTM result: ")
        print(f"   - TX: {DTM['TX']}")
        print(f"   - RX: {DTM['RX']}")





# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  DTMInterface(driver, "F://Nimbra360_scrapping/temp/dtm_interface.html")

# result = temp.start()
# print(result)
# driver.close()
# exit()