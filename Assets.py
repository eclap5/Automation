from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

reservationUrl = "https://outlook.office365.com/owa/calendar/StudentUnionHousereservations@lut.onmicrosoft.com/bookings/"

# xpath values:
logInEmail = '//*[@id="i0116"]'
logInNext = '//*[@id="idSIButton9"]'
logInPassword = '//*[@id="passwordInput"]'
logInSubmit = '//*[@id="submitButton"]'
logInUrl = 'https://login.microsoftonline.com/common/federation/OAuth2ClaimsProvider'
logInBackBtn = '//*[@id="idBtn_Back"]'
duoMfaBackBtn = '//*[@id="dont-trust-browser-button"]'

nameField = '//*[@id="mainContainer"]/div/form/div[8]/div/div/div[1]/input[1]'
emailField = '//*[@id="mainContainer"]/div/form/div[8]/div/div/div[1]/input[2]'
bookBtn = '//*[@id="mainContainer"]/div/form/div[10]/button'
okBtn = '/html/body/div/div/form/div[3]/div[2]/div[2]/button'

reservedHours = []

# Function for selecting wanted date from date picker. Because date picker format, we must loop through every possible choice until wanted date is found.
# Also check if there is no available times for desired date.
def SelectDate(driver, date, wait): 
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContainer"]/div/form/div[7]/div[1]/div/div/div[3]/div[1]')))
    for i in range(1, 35):
        xpath = '//*[@id="mainContainer"]/div/form/div[7]/div[1]/div/div/div[3]/div[{}]'.format(i)
        try:
            element = driver.find_element(By.XPATH, xpath)
            if ((element.text == date) and 
                (element.get_attribute("title") == "Times available" or element.get_attribute("title") == "Selected date - Times available")):
                return xpath
            if (int(element.text) > int(date)):
                break 
        except:
            continue
    return None


# Function for room selection. 
def SelectRoom(room):
    room = int(room) + 1
    xpath = "/html/body/div/div/form/div[6]/div/div/ul/li[{}]/label/span".format(str(room))
    return xpath


# Function for selecting correct time slot. Iterate through all possible times until selected time is found. 
# Return xpath value for the selected time.
# If selected time is not found, return None and skip to the next hour.
def SelectTime(driver, wait, iterator):
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[1]/label/span')))
    match iterator:
        case 1:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "8:00 am"):
                        reservedHours.append("08:00")
                        return xPathTimeElement
                except:
                    break
        case 2:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "9:00 am"):
                        reservedHours.append("09:00")
                        return xPathTimeElement
                except:
                    break
        case 3:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "10:00 am"):
                        reservedHours.append("10:00")
                        return xPathTimeElement
                except:
                    break
        case 4:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "11:00 am"):
                        reservedHours.append("11:00")
                        return xPathTimeElement
                except:
                    break
        case 5:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "12:00 pm"):
                        reservedHours.append("12:00")
                        return xPathTimeElement
                except:
                    break
        case 6:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "1:00 pm"):
                        reservedHours.append("13:00")
                        return xPathTimeElement
                except:
                    break
        case 7:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "2:00 pm"):
                        reservedHours.append("14:00")
                        return xPathTimeElement
                except:
                    break
        case 8:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "3:00 pm"):
                        reservedHours.append("15:00")
                        return xPathTimeElement
                except:
                    break
        case 9:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "4:00 pm"):
                        reservedHours.append("16:00")
                        return xPathTimeElement
                except:
                    break
        case 10:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "5:00 pm"):
                        reservedHours.append("17:00")
                        return xPathTimeElement
                except:
                    break
        case 11:
            for i in range(1, 29):
                xPathTimeElement = '/html/body/div/div/form/div[7]/div[2]/div/div/ul/li[{}]/label/span'.format(i)
                try:
                    if (driver.find_element(By.XPATH, xPathTimeElement).text == "6:00 pm"):
                        reservedHours.append("18:00")
                        return xPathTimeElement
                except:
                    break
    return None