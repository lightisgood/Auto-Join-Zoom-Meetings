
from time import sleep
from keyboard import write
from mouse import move, click
import subprocess
import sys
subprocess.run("your zoom.exe location")
sleep(3)
x = [535, 549, 523, 708, 644, 692]
y = [286, 323, 429, 492, 332, 491]
for i in range(6):
    move(x[i], y[i])
    click()
    if i == 0:
        sleep(3)
        write("your meeting id ") # meeting id
    elif i == 4:
        sleep(5)
        write("your meeting password") # password
    elif i == 5:
        sleep(5)
    sleep(3)
sys.exit(0)