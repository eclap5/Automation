Automation for Student Union house upstairs working space reservation in LUT University. <br />


DISCLAIMER: <br />
Use with your own responsibility, this code might include bugs or/and security risks!


How to use: <br />
Make sure your chromedriver and current Chrome version are up to date.
You need a chromedriver which supports your Chrome version.
You need to create 'config.ini' file which contains your LUT credentials.
'config.ini' file needs to be in following format: <br />
[DEFAULT] <br />
password = yourpassword <br />
email = yourlutemail <br />
name = yourname <br />
	
After creation insert 'config.ini' to the same folder as the files downloaded from this github repository.
Insert chromedriver.exe to the same folder.

After these steps run 'Automation.py' file.

At the moment the space has been defaulted to YO-Wappu, but it will be changed that user can specify which room is wanted.
Also only spaces where every time slot is free between 08:00 and 20:00 can be reserved. If not, every free hour will be reserved until first reserved hour comes up.
Program will crash when it tries to reserve already reserved hour. Also update for DUO MFA is coming in some point.

Enjoy!

Created by: Aleksi Haapalainen

