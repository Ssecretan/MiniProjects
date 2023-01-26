import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Your timer for ' + m + ' is up! ')

t = input('Enter the time in seconds: ')
m = input('What is your timer for: ')

countdown(int(t))