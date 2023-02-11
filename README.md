# Automation for Student Union House Working Space Reservation in LUT University

## DISCLAIMER
Use at your own risk. This code may contain bugs and security vulnerabilities.

## Introduction
This project automates the process of reserving a working space in the Student Union House at LUT University.

## Prerequisites
- Up-to-date Chrome browser and chromedriver
- Python 3.7 or newer version.
- Selenium library for Python. (pip install selenium).
- `config.ini` file containing your LUT credentials in the following format:<br/>
[DEFAULT]<br/>
password = yourpassword<br/>
email = yourLUTemail<br/>
name = your name<br/>

## Installation
1. Download the files from this Github repository.
2. Place the `config.ini` file and the `chromedriver.exe` in the same folder as the downloaded files.
3. Run the `Automation.py` file.

## Usage
The program reserves every free hour between 08:00 and 19:00 from the selected date. By default, the room is set to YO-Wappu, but this will be changed in the future to allow the user to specify their preferred room. Additionally, support for DUO MFA will be added in the future.

## Note
Please make sure that your chromedriver and Chrome browser are up to date and that the chromedriver supports your Chrome version.

## Future plans
- Allow the user to specify their preferred room.
- Add support for DUO MFA.

## Author
This project was created by Aleksi Haapalainen.

