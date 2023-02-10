from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import configparser
import Assets


config = configparser.ConfigParser()
config.read('config.ini')

now = datetime.datetime.now()
today = now.strftime("%d")

name = config['DEFAULT']['name']
email = config['DEFAULT']['email']
password = config['DEFAULT']['password']

print("What date you want to book? (Answer in format: 'DD', only current month): ")
date = input()

while (int(date) < int(today)):
    print("Please select new date.")
    date = input()

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 90)

driver.get(Assets.reservationUrl)
wait.until(EC.presence_of_element_located((By.XPATH, Assets.logInEmail)))
driver.find_element(By.XPATH, Assets.logInEmail).send_keys(email)
wait.until(EC.element_to_be_clickable((By.XPATH, Assets.logInNext)))
driver.find_element(By.XPATH, Assets.logInNext).click()

passwordInput = wait.until(EC.presence_of_element_located((By.XPATH, Assets.logInPassword)))
passwordInput.send_keys(password)

driver.find_element(By.XPATH, Assets.logInSubmit).click()

if (driver.current_url == Assets.logInUrl):
    driver.find_element(By.XPATH, Assets.logInBackBtn).click()

wait.until(EC.url_to_be(Assets.reservationUrl))


for i in range(1, 12):

    # Reload the correct page
    driver.get(Assets.reservationUrl)
    wait.until(EC.url_to_be(Assets.reservationUrl))

    # Select calendar from site and select wanted date
    calendarPick = Assets.SelectDate(driver, date, wait)
    wait.until(EC.element_to_be_clickable((By.XPATH, calendarPick)))
    driver.find_element(By.XPATH, calendarPick).click()

    # Select space to be reserved. Currently defaulted to Yo Wappu  
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[6]/div/div/ul/li[14]/label/span').click() 

    # Select time to be reserved. Selects one hour with every iteration.
    xPathTime = Assets.SelectTime(driver, wait, i)
    driver.find_element(By.XPATH, xPathTime).click()

    # Fills in name and email
    driver.find_element(By.XPATH, Assets.nameField).send_keys(name)
    driver.find_element(By.XPATH, Assets.emailField).send_keys(email)

    # Clicks 'book' button
    driver.find_element(By.XPATH, Assets.bookBtn).click()

    #Clicks 'OK' button
    wait.until(EC.element_to_be_clickable((By.XPATH, Assets.okBtn)))
    driver.find_element(By.XPATH, Assets.okBtn).click()

