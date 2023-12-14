import time
import datetime
from playsound import playsound

# pip install playsound==1.2.2

directory = "/" # Put audo files in same folder as this script
loop1 = ["X", "X", "X"] # Replace X with the name of your audiotrack, you don't need to add extension as script does it
loop2 = ["X", "X", "X"] # Replace X with the name of your audiotrack, you don't need to add extension as script does it
loop3 = ["X", "X", "X"] # Replace X with the name of your audiotrack, you don't need to add extension as script does it

loop1 = [x + ".mp3" for x in loop1]
loop2 = [x + ".mp3" for x in loop2]
loop3 = [x + ".mp3" for x in loop3]

while True:
    time_of_day = datetime.datetime.now().strftime("%H:%M")
    day_of_week = datetime.datetime.now().strftime("%A")

    while time_of_day >= "08:00" and time_of_day <= "11:30": # SET YOUR START AND END TIME HERE
        if day_of_week == "Monday" or day_of_week == "Wednesday":
            for i in loop1:
                playsound([i])
        elif day_of_week == "Tuesday" or day_of_week == "Thursday":
            for i in loop2:
                playsound([i])
        elif day_of_week == "Friday":
            for i in loop3:
                playsound([i])
        else:
            continue

    while time_of_day >= "13:00" and time_of_day <= "16:30": # SET YOUR START AND END TIME HERE
        if day_of_week == "Monday" or day_of_week == "Wednesday":
            for i in loop1:
                playsound([i])
        elif day_of_week == "Tuesday" or day_of_week == "Thursday":
            for i in loop2:
                playsound([i])
        elif day_of_week == "Friday":
            for i in loop3:
                playsound([i])
        else:
            continue
    time.sleep(3600)
