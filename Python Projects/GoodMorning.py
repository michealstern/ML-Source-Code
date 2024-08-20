import time
# Morning time : 04:00:00 to 11:59:59
# Afternoon time : 12:00:00 to 16:59:59
# Evening time : 17:00:00 to 20:59:59
# Nihgt time : 21:00:00 to 03:59:59

name = input("Enter Your Name :- ").title()
# currentTime = time.strftime('%H:%M:%S')
# print(currentTime)
hour = int(time.strftime('%H'))
if 4 <= hour <12:
 print("Goood Morning",name)
elif 12 <= hour <17:
 print("Goood Afternoon",name)
elif 17 <= hour <21:
 print("Good Evening",name)
else:
 print("Goood Night",name)