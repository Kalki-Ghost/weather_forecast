# This is the simple program of countdown timer
import time
import winsound


def timer(seconds):
    print(f"starting countdown for {seconds} seconds")
    while seconds:
        minute, seconds = divmod(seconds, 60)
        timer_formate = f"{minute:02}:{seconds:01}"
        print(timer_formate)
        time.sleep(1)
        seconds -= 1
    print("Time is up.")
    winsound.Beep(2000,20000)


sec = int(input("Enter the seconds:"))
timer(sec)
