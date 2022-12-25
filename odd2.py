from datetime import datetime
import random
import time

odds = [x for x in range(1, 60) if x % 2 != 0]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print('this minute seem a little odd.')
    else:
        print('Not an odd minute.')
        wait_time = random.randint(1, 3)
        time.sleep(wait_time)

