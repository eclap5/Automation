from selenium.webdriver.common.by import By
import time

xPathList = ['3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25']

reservationUrl = "https://outlook.office365.com/owa/calendar/StudentUnionHousereservations@lut.onmicrosoft.com/bookings/"

def SelectDate(driver, date):
    time.sleep(3)
    for i in range(1, 35):
        xpath = "/html/body/div/div/form/div[7]/div[1]/div/div/div[3]/div[{}]".format(i)
        try:
            print(driver.find_element(By.XPATH, xpath).text)
            if (driver.find_element(By.XPATH, xpath).text == date):
                return xpath
        except:
            continue



# chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Users\Aleksi\Desktop\Automation\Chrome_Test_Profile"
