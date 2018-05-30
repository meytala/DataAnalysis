from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
import os

event_types = ['Rain', 'Thunderstorm', 'Snow', 'Fog']
num_events = len(event_types)


def event2int(event):
    return event_types.index(event)


##test
##print(event2int("Snow"))


#####I change this function to match python 3 needed to change the format of data_str to utf8 (https://stackoverflow.com/questions/21689365/python-3-typeerror-must-be-str-not-bytes-with-sys-stdout-write)
def date2int(date_str):
    date_str = date_str.decode('utf-8')  ##this is the line I added
    date = datetime.strptime(date_str, '%d/%m/%Y')
    return date.toordinal()


##test (before changing)
##print(date2int("2016-02-25"))

def r_squared(actual, ideal):
    actual_mean = np.mean(actual)
    ideal_dev = np.sum([(val - actual_mean) ** 2 for val in ideal])
    actual_dev = np.sum([(val - actual_mean) ** 2 for val in actual])

    return ideal_dev / actual_dev


###test
##a= [1,3,6,3,5,9]
##b= [3,5,8,1,2,3]
##print(r_squared(a,b))


def read_weather(file_name):
    dtypes = np.dtype({'names': ('timestamp', 'max temp', 'mean temp', 'min temp', 'events'),
                       'formats': [np.int, np.float, np.float, np.float, 'S100']})

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
                      converters={0: date2int},
                      usecols=(0, 1, 2, 3, 21), dtype=dtypes)

    return data


# --------------------------------------------------


data = read_weather('weather.csv')
print (data)

####################We have data###################

####giving names to the data:

max_temps = data['max temp']
mean_temps = data['mean temp']
min_temps = data['min temp']
events = data['events']

#### converting the integers back to dates again
dates = [datetime.fromordinal(d) for d in data['timestamp']]

######print the date (as month and day) and mean temp
# for date, temp in zip(dates, mean_temps):
#    print ('{0:%b %d}: {1}'.format(date, temp))


###changing the dates to days
year_start = datetime(2012, 1, 1)
days = [(d - year_start).days + 1 for d in dates]

####ploting the mean temp vs. the day of the year
plt.title("Mean temp over 2012 (F)")
plt.xlabel("Day of the year")
plt.ylabel("Mean temp")
plt.plot(days, mean_temps, "b-o")

###adding a trend line
z = np.polyfit(days, mean_temps, 1)
p = np.poly1d(z)

plt.plot(days, p(days), 'r--')
# regression = intercept + slope*days
# plt.plot(days, regression)


plt.show()


