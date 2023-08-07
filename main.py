#______________________________________#
#                                      #
#----------Simple Alarm Clock----------#
#                                      #
#______________________________________#
#Author: Akash Nath (https://github.com/Akash-nath29)#

import time
from pygame import mixer

mixer.init()
mixer.music.load("alarmClock.mp3")

myTime = int(input("Enter time in seconds: "))

for i in range(myTime, 0, -1):
    seconds = i%60
    print(f"00:00:{seconds}")
    time.sleep(1)
    
mixer.music.play()
while mixer.music.get_busy():
    pass