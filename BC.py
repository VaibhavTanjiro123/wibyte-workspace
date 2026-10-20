import datetime as dt
import time
print('Welcome to your birthday countdown!')

yr=int(input('Which Year Were You Born In?\n'))
mnth=int(input('Which month(1 for Jan,2 for Feb,and so on)?)\n'))
day=int(input('Which day?\n'))

date_birth=dt.datetime(yr,mnth,day)

weeknum=date_birth.weekday()

weekday_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print('You were born on a ',weekday_list[weeknum])

c_t=dt.datetime.now()
thyr = c_t.year
thisbday=dt.datetime(thyr,mnth,day)

if thisbday>c_t:
    nxtbday=thisbday
else:
    nxtbday=dt.datetime(thyr+1,mnth,day)

weeknum=nxtbday.weekday()

print('Your next birthday will be a... ',weekday_list[weeknum])
while nxtbday>c_t:
    c_t=dt.datetime.now()
    dd=nxtbday-c_t
    daysleft=dd.days
    totalsecondsleft=dd.seconds
    tml,sl=divmod(totalsecondsleft,60)
    hrs,mins=divmod(tml,60)
    print('Your Birthday is',daysleft,"days",hrs,'hours',mins,'minutes',sl,'seconds away',sep=' ',end='\r')
    time.sleep(1)