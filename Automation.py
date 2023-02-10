from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import configparser
import Assets


config = configparser.ConfigParser()
config.read('config.ini')

now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

name = config['DEFAULT']['name']
email = config['DEFAULT']['email']
password = config['DEFAULT']['password']

#print("What date you want to book? (Answer in format: 'DD', only current month): ")
date = "12" #input()

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 90)

driver.get(Assets.reservationUrl)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))
driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

passwordInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordInput"]')))
passwordInput.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()

if (driver.current_url == 'https://login.microsoftonline.com/login.srf'):
    driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()

wait.until(EC.url_to_be(Assets.reservationUrl))


for i in Assets.xPathList:
    if (driver.current_url != Assets.reservationUrl):
        driver.get(Assets.reservationUrl)
        time.sleep(1)

        # Select calendar from site and select wanted date
        calendarPick = Assets.SelectDate(driver, date)
        wait.until(EC.element_to_be_clickable)
        driver.find_element(By.XPATH, calendarPick).click()

        # Select space to be reserved. Currently defaulted to Yo Wappu  
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[6]/div/div/ul/li[14]/label/span').click() 

        # Select time to be reserved. Selects one hour with every iteration.
        xPathElementTime = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
        driver.find_element(By.XPATH, xPathElementTime).click()

        # Fills in name and email
        driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/form/div[8]/div/div/div[1]/input[1]').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/form/div[8]/div/div/div[1]/input[2]').send_keys(email)

        # Clicks 'book' button
        driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/form/div[10]/button').click()
        time.sleep(3)

