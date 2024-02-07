# Passagem de ano EX021
from time import sleep
import winsound
frequency = 2500
duration = 1000
winsound.Beep(frequency, duration)
for c in range(10, 0, -1):
    print(c)
    sleep(1)

    if c == 1:
        print("Feliz ano novo!")