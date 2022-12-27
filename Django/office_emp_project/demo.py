import time
name = input("Enter user name: ").title()
currentTime = time.strftime('%H:%M:%S')
hour = time.strftime('%H')
if hour < "12":
    print("Good Morning", name)
elif "12" < hour < "17":
    print("Good Afternoon", name)
else:
    print("Good Evening", name)


import sys
sys.exit(0)

from datetime import datetime

current_hour = int(datetime.now().strftime('%H'))
if current_hour<12:
    print('Good morning')
elif 12<=current_hour<18:
    print('Good afternoon')
else:
    print('Good Evening')


import sys
sys.exit(0)

import time
name = input("Enter Your Name:- ").title()
currentTime = time.strftime('%H:%M:%S')
hour = time.strftime('%H')

if hour < "12":
    print("Good Morning", name)
elif "12" < hour < "17":
    print("Good Afternoon", name)
else:
    print("Good Evening", name)