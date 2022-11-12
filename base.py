from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_pages import login, status_alarm, status_eqm, dtm_interface,pm_overview, pm_details
import time


# Make base class
class Base():
    def __init__(self, chrome_driver_path = "./driver/chromedriver.exe") -> None:
        self.chrome_driver_path = chrome_driver_path

        # Make an instance of Chrome driver
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        service = Service(executable_path= chrome_driver_path)
        self.driver  = webdriver.Chrome(service=service, options=op)
    
        # Nimbra variable that save informations
        self.nimbras_info = {
            'Ghaen' : {'ip': 'F://Nimbra360_scrapping/temp', 'username':'root', 'password':'xxxx'},
            'Tabas' : {'ip': 'F://Nimbra360_scrapping/temp', 'username':'root', 'password':'xxxx'},
            'Abiz'  : {'ip': 'F://Nimbra360_scrapping/temp', 'username':'root', 'password':'xxxx'},
        }
    
    # Start Scrapping
    def start(self, today_date='10 Sep 2022', yesterday_date='5 Oct 2021',stations=['Ghaen'], **kwargs):
        results = []
        # Iterate on each nimbra 
        for i, nimbra_name in enumerate(stations):
            kwargs['prog_bar'].progress(int(100/len(stations))*(i+1))
            if nimbra_name not in self.nimbras_info.keys(): continue
            nimbra = self.nimbras_info[nimbra_name]
            
            print('\n')
            print(f"**************** {nimbra_name} ****************")

            # Urls
            login_url    = f"{nimbra['ip']}/login.html"
            alarm_url    = f"{nimbra['ip']}/status_alarm.html"
            equ_url      = f"{nimbra['ip']}/status_eqm.html"
            dtm_url      = f"{nimbra['ip']}/dtm_interface.html"
            pm_trunk_url = f"{nimbra['ip']}/pm_overview.html?tif"
            pm_ts_url    = f"{nimbra['ip']}/pm_details.html"


            ## Login
            login_ins =  login.Login(self.driver, login_url, nimbra['username'], nimbra['password'], login_name=nimbra_name)
            login_ins.start()

            ## Alarm
            print(today_date)
            alarm_ins    =  status_alarm.StatusAlarm(self.driver, alarm_url, date=today_date)
            alarm_result = alarm_ins.start()

            ## Temprature 
            eqm_ins    =  status_eqm.StatusEqm(self.driver, equ_url)
            eqm_result = eqm_ins.start()

            # DTM 
            dtm_ins    =  dtm_interface.DTMInterface(self.driver, dtm_url)
            dtm_result = dtm_ins.start()


            ## TRUNK
            trunk_ins    =  pm_overview.PMOverview(self.driver, pm_trunk_url)
            trunk_result = trunk_ins.start()


            ## TS1 
            ts1_ins    =  pm_details.PMDetails(self.driver, pm_ts_url, 0, yesterday_date)
            ts1_result = ts1_ins.start()


            ## TS2 
            ts2_ins    =  pm_details.PMDetails(self.driver, pm_ts_url, 1, yesterday_date)
            ts2_result = ts2_ins.start()

            # Print Results
            print('\n')
            print("+ Temprature:  ", eqm_result)
            alarm_ins.sp_print(alarm_result)
            dtm_ins.sp_print(dtm_result)
            trunk_ins.sp_print(trunk_result)
            ts1_ins.sp_print(ts1_result)
            ts2_ins.sp_print(ts2_result)

            # Save result
            results.append({
                'name' : nimbra_name,
                'temprature' : eqm_result,
                'alarm' : alarm_result,
                'DTM' : dtm_result,
                'trunk' : trunk_result,
                'ts1' : ts1_result,
                'ts2' : ts2_result,
            })
        
        return results




