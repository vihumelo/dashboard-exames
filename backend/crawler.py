from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os



def save_csv(driver):
    
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink"]'))
    )

    time.sleep(3)

    save.click()

    csv = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportViewerControl_ctl05_ctl04_ctl00_Menu"]/div[7]/a'))
    )

    csv.click()

while True:
    # chrome_options = Options()
    # chrome_options.add_argument('--headless') 
    driver = webdriver.Chrome()
    driver.get('Endereço para SCRAP')

    save_csv(driver)
    time.sleep(2)
    insert_database()
        

    while True:
        
        try:
            time.sleep(10)
            driver.refresh()
            save_csv(driver)
            time.sleep(2)
            insert_database()
            
        except Exception as error:
            print('Erro')
            print(error)
            driver.quit()
            break
    