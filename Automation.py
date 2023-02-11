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
currentDay = now.strftime("%d")
currentMonth = now.strftime("%m")

if (int(currentMonth) == 2):
    maxdate = 28
elif (int(currentMonth)%2 == 0):
    maxdate = 30
else:
    maxdate = 31

name = config['DEFAULT']['name']
email = config['DEFAULT']['email']
password = config['DEFAULT']['password']

while True:
    date = input("What date you want to book? (Answer in format: 'DD', only current month): ")
    try:
        while (int(date) < int(currentDay) or int(date) > maxdate):
            date = input("Please select new date: ")
        break
    except:
        print("Use only numbers please.")
    
# while True:
#     print("Which room would you like to choose?")
#     print("1. Yo Delphi\n2. Yo Gif\n3. Yo Gurtti\n4. Yo Kofeiini")
#     print("5. Yo Kondensaattori\n6. Yo Konkaavi\n7. Yo Kosmos")
#     print("8. Yo Kuivatyöstö\n9. Yo Laulu\n10. Yo Reaktori")
#     print("11. Yo Saimaa\n12. Yo Uni\n13. Yo Wappu")
#     print("Your choice: ")
#     space = input()
#     try:
#         while (int(space) < 1 and int(space) > 13):
#             print("Please select a number between 1 and 13.")
#             print("Your choice: ")
#             space = input()
#         break
#     except:
#         print("Use only numbers please.")

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
    if (xPathTime == None):
        continue
    driver.find_element(By.XPATH, xPathTime).click()

    # Fills in name and email
    driver.find_element(By.XPATH, Assets.nameField).send_keys(name)
    driver.find_element(By.XPATH, Assets.emailField).send_keys(email)

    # Clicks 'book' button
    driver.find_element(By.XPATH, Assets.bookBtn).click()

    #Clicks 'OK' button
    wait.until(EC.element_to_be_clickable((By.XPATH, Assets.okBtn)))
    driver.find_element(By.XPATH, Assets.okBtn).click()

print("Reserved times: ")
for i in Assets.reservedHours:
    print(i)
