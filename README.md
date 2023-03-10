# Automation for Student Union House Working Space Reservation in LUT University

## DISCLAIMER
Use at your own risk. This code may contain bugs and security vulnerabilities.

## Introduction
This project automates the process of reserving a working space in the Student Union House at LUT University.

## Prerequisites
- DUO MFA mobile app.
- Up-to-date Chrome browser and chromedriver.
- Python 3.7 or newer version.
- Selenium library for Python. (pip install selenium).
- `config.ini` file containing your LUT credentials in the following format:<br/>
[DEFAULT]<br/>
password = yourpassword<br/>
email = yourLUTemail<br/>
name = your name<br/>

## Installation
1. Download the files from this Github repository.
2. Make sure you have Python and Selenium library installed.
3. Place the `config.ini` file and the `chromedriver.exe` in the same folder as the downloaded files.
4. Run the `Automation.py` file.

## Usage
The program reserves every free hour between 08:00 and 19:00 from the selected date. Program asks the user to determine which room he/she wants to reserve. When user is logged in, there will be DUO MFA Authentication that user must provide manually with DUO MFA mobile app. Other than that everything else is automated.

## Note
Please make sure that your chromedriver and Chrome browser are up to date and that the chromedriver supports your Chrome version.

## Future plans
- Suggestions for improvements are welcome!

## Author
This project was created by Aleksi Haapalainen.

