from datetime import datetime

odds = [x for x in range(1, 60) if x % 2 != 0]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print('this minute seem a little odd.')
else:
    print('Not an odd minute.')


