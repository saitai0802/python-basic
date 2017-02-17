import time
from datetime import datetime as dt

"""
A script bases on website URL to block website


The theory is chaanging the host file. 
Window - C:\Windows\System32\drivers\etc\host
Linux - \etc\host

127.0.0.1 TheDomainNameYouWant2Block

======================Schedule this script in Window enviroment===============================
You may run this script without terminal.
.py will be executed by python.exe by default. This executable opens a terminal, which stays open even if the program uses a GUI. 
.pyw will cause the script to be executed by pythonw.exe by default (both executables are located in the top-level of your Python installation directory). 
This suppresses the terminal window on startup.
"""

# Run this program as Admin everytimes to modify the hosts file.
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect_url = "127.0.0.1"
website_list  = ["facebook.com","facebook"]


currentTime = dt.now()
while True:
	# Check current time is working hour? (Later than 8am, but earlier than 4pm)
	# If so, Add a line to block domain
	if dt(currentTime.year, currentTime.month, currentTime.day,8) < currentTime < dt(currentTime.year, currentTime.month, currentTime.day,16):
		with open(hosts_path, "r+") as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass # It means continue
				else:
					file.write(redirect_url +"\t"+ website +"\n")
		print("Working hours")
	else:
		# Step 1: Read single line, if this line have no blocked url print this line from pointer(0)
		# Step 2: Ignore blocker url line
		# Step 3: After looping through all lines (There have no blocked information again) => Truncate this file

		# r+, read and write + not truncate + from begining of doc.
		with open(hosts_path, "r+") as file:
			content = file.readlines() # Get a list of each line
			file.seek(0)
			for line in content:
				# if not any item(website) in website_list appear IN this line
				# Which means this line have no blocked url then
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("Non-working hours")
	time.sleep(3)


