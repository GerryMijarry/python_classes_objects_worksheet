from alarm_clock import AlarmClock
from datetime import datetime

# Done - As a developer, I want to use Python’s proper snake_case for variable names.
# Done - As a developer, I want to create a AlarmClock class.
# Done - As a developer, I want the AlarmClock class to have class properties to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).
# Done - As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.
# Done - As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off. 
# Done - As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.
# Done - As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


ac1 = AlarmClock(current_time)

ac1.set_alarm("00:06:30")
ac1.turn_on_off(True)




