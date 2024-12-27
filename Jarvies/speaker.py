import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
n = "Yes"
while 1 :
    print('Enter the word you want speak it out by computer')
    n = input()
    speaker.Speak(n)
