# Health Potion Python
# Brian Snitzer
# July 5, 2019

import random
import datetime
import math


health = 50
potion_health = random.randint(25, 50)

starttime = datetime.datetime.now()
print(starttime)
print("Welcome Player.  Your health is", health)
print("Please enjoy this fine potion.")

health = health + potion_health
print("Now your health is", health)
endtime = datetime.datetime.now()
print("Execution time = ",
       starttime.microsecond - endtime.microsecond,
       "microseconds.")
