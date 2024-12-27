import time

# Program of alarm clock working
import winsound


def alarm():
    print("Time formate (HH:MM:SS)")
    alarm_timer = input("Set alarm(24 hour formate):")
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time {current_time}", end='\r')
        time.sleep(1)
        if current_time == alarm_timer:
            print("Alarm!Time Up.")
            winsound.Beep(1000, 2000)
            break


alarm()
