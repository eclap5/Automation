Automation for Student Union House working space reservation in LUT University. <br />


DISCLAIMER: <br />
Use with your own responsibility, this code might include bugs and/or security flaws!


HOW TO USE: <br />
Make sure your chromedriver and current Chrome version are up to date.
You need a chromedriver which supports your Chrome version.
You need to create 'config.ini' file which contains your LUT credentials.
'config.ini' file needs to be in following format: <br />
[DEFAULT] <br />
password = yourpassword <br />
email = yourLUTemail <br />
name = your name <br />
	
After creation insert 'config.ini' to the same folder as the files downloaded from this github repository.
Insert chromedriver.exe to the same folder.

After these steps run 'Automation.py' file.
Program reserves every free hour between 08:00 and 19:00 from the selected date.

At the moment the space has been defaulted to YO-Wappu, but it will be changed so that user can specify which room is wanted.
Also update for DUO MFA is coming in some point.


Created by: Aleksi Haapalainen

