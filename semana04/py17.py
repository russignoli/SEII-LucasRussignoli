"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
#print(dt_mtn)

#for tz in pytz.all_timezone:
#	print(tz)

dt_str = 'July 26, 2016'

dt = datetime.strptime(dt_str, '%B %d, %Y')
print(dt)