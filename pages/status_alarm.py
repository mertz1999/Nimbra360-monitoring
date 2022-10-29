from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

    
class StatusAlarm():
    """
    This block of code fetch data from alarm page and check date of it and then save all information about this alarm

    inputs:
        1. driver
        2. url
        3. date (ex. '20 Oct 2021')
    
    result:
        today_alarm:
            0. Cause
            1. Type
            2. Object Name
            3. Text
            4. Time
            5. Ack

    """

    def __init__(self, driver : webdriver.Chrome, url, date='20 Oct 2021'):
        # Print information
        print(f' ################## Start Status Alarm({url}) ################## ')

        # Split date
        self.date = date.split(' ') # Day, month, year
        
    
        # Save parameters
        self.url        = url
        self.driver     = driver
    
    def start(self):   
        today_alarms = [] # 0-> Cause, 1-> type, 2->object_name, 3-> text, 4-> time, 5->Ack   
        # Open login page and check it
        self.driver.get(self.url)
        time.sleep(1)
        
        # Find all inputs and then check to file login, password and submit buttun
        list_of_alarm = self.driver.find_elements(By.XPATH,"//tr[@class='row']")
        for row in list_of_alarm:
            # Get each of column and iterate on them
            cols = row.find_elements(By.TAG_NAME, "td") # 0->Cuase, 1->Not important, 2->type of cols, 3->object name, 4->Text, 5->Time, 6->Ack

            # Check for time
            date_in_row = cols[5].text.split(' ')
            if date_in_row[4] == self.date[2] and date_in_row[1] == self.date[1] and date_in_row[2] == self.date[0]:
                today_alarms.append([cols[0].text, cols[2].text, cols[3].text, cols[4].text, cols[5].text, cols[6].text])
                

        return today_alarms




# service = Service(executable_path="./driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# temp =  StatusAlarm(driver, "F://Nimbra360_scrapping/temp/status_alarm.html", date='10 Sep 2022')

# result = temp.start()
# for i in result:
#     print(i)
# driver.close()
# exit()