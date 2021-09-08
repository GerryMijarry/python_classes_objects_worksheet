class AlarmClock:
    def __init__(self, current_time, alarm_time="00:00:00", on_off=False):
        self.current_time = current_time
        self.alarm_time = alarm_time
        self.on_off = on_off
        print("The current time is " + self.current_time)

    def change_time(self, new_time):
        self.current_time = new_time
        print("The time has been changed to " + self.current_time)

    def turn_on_off(self, requested_state):
        self.on_off = requested_state

        print("The alarm is set to " + str(self.on_off))

    def set_alarm(self, new_time):
        self.alarm_time = new_time
        print("The alarm is now set for " + self.alarm_time)


