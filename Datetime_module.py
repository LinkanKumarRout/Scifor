'''
import datetime as dt

now = dt.datetime.now() # gives both date and time
print(now)

print(dt.date.today()) # gives current date
print(dt.datetime.now().time()) # gives current time

# Formatting a datetime object as a string
dt = datetime.datetime.now()
formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)
# Parsing a string into a datetime object
str_date = '2022-12-31 23:59:59'
parsed_date = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(parsed_date)

import pytz  # Python Timezone library
tz = pytz.timezone('America/New_York')
ny_time = datetime.datetime.now(tz)
print(ny_time)
'''