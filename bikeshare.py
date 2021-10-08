import time
from collection import OrderedDict
import pandas as pd
import numpy as np

print ("REFACTORED CODE")

FILES = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

chicago = pd.read_csv(FILES['Chicago'])
ny = pd.read_csv(FILES['New York City'])
washington = pd.read_csv(FILES['Washington'])

DFs = OrderedDict()
DFs['Chicago'] = chicago
DFs['New York City'] = ny
DFs['Washington'] = washington

# MOST POPULAR TIMES OF TRAVEL
print("\n\nMOST POPULAR TIMES OF TRAVEL\n\n")

## MOST POPULAR MONTH ##
print("\nMOST POPULAR MONTH\n")
MOST_POPULAR_MONTH = OrderedDict()
for k,v in DFs.items():
    v['Start Time'] = pd.to_datetime(v['Start Time']) # Convert to datetime
    v['month'] = v['Start Time'].dt.month
    popular_month = v['month'].mode()[0]
    MOST_POPULAR_MONTH[k] = popular_month

for k,v in MOST_POPULAR_MONTH.items():
    print(f"Most popular month in {k}: {v}")

## MOST POPULAR DAY ##
print("\nMOST POPULAR DAY\n")
MOST_POPULAR_DAY = OrderedDict()
for k,v in DFs.items():
    v['Start Time'] = pd.to_datetime(v['Start Time']) # Convert to datetime
    v['day'] = v['Start Time'].dt.day
    popular_day = v['day'].mode()[0]
    MOST_POPULAR_DAY[k] = popular_day

for k,v in MOST_POPULAR_DAY.items():
    print(f"Most popular day in {k}: {v}")

## MOST POPULAR HOUR ##
print("\nMOST POPULAR HOUR\n")
MOST_POPULAR_HOUR = OrderedDict()
for k,v in DFs.items():
    v['Start Time'] = pd.to_datetime(v['Start Time']) # Convert to datetime
    v['hour'] = v['Start Time'].dt.hour
    popular_hour = v['hour'].mode()[0]
    MOST_POPULAR_HOUR[k] = popular_hour

for k,v in MOST_POPULAR_HOUR.items():
    print(f"Most popular hour in {k}: {v}")

# MOST POPULAR STATIONS AND TRIPS #
print("\n\nMOST POPULAR STATIONS AND TRIPS\n\n")

## MOST POPULAR START STATION ##
print("\nMOST POPULAR START STATION\n")
MOST_POPULAR_START = OrderedDict()
for k,v in DFs.items():
    popular_start = v['Start Station'].mode()[0]
    MOST_POPULAR_START[k] = popular_start

for k,v in MOST_POPULAR_START.items():
    print(f"Most popular start station in {k}: {v}")

## MOST POPULAR END STATION ##
print("\nMOST POPULAR END STATION\n")
MOST_POPULAR_END = OrderedDict()
for k,v in DFs.items():
    popular_end = v['End Station'].mode()[0]
    MOST_POPULAR_END[k] = popular_end

for k,v in MOST_POPULAR_END.items():
    print(f"Most popular end station in {k}: {v}")

## MOST POPULAR TRIP STATION ##
print("\nMOST POPULAR TRIP\n")
MOST_POPULAR_TRIP = OrderedDict()
for k,v in DFs.items():
    v['Trip'] = v[['Start Station', 'End Station']].agg(' to '.join, axis=1)
    popular_trip = v['Trip'].mode()[0]
    MOST_POPULAR_TRIP[k] = popular_trip

for k,v in MOST_POPULAR_TRIP.items():
    print(f"Most popular trip in {k}: {v}")

# TRIP DURATION #
print("\n\nTRIP DURATION\n\n")

## TOTAL TRAVEL TIME ##
print("\nTOTAL TRAVEL TIME\n")
TOTAL_TRAVEL_TIME = OrderedDict()
for k,v in DFs.items():
    total_travel_time = v['Trip Duration'].sum()
    TOTAL_TRAVEL_TIME[k] = total_travel_time

for k,v in TOTAL_TRAVEL_TIME.items():
    print(f"Total travel time in {k}: {v}")

## AVERAGE TRAVEL TIME ##
print("\nAVERAGE TRAVEL TIME\n")
AVG_TRAVEL_TIME = OrderedDict()
for k,v in DFs.items():
    avg_travel_time = v['Trip Duration'].mean()
    AVG_TRAVEL_TIME[k] = avg_travel_time

for k,v in AVG_TRAVEL_TIME.items():
    print(f"Average travel time in {k}: {v}")

# USER INFO #
print("\n\nUSER INFO\n\n")

## USER TYPE AND GENDER ##
USER_TYPE = OrderedDict()
GENDER = OrderedDict()
DOB = OrderedDict()
for k,v in DFs.items():
    user_types = v['User Type'].count()
    USER_TYPE[k] = user_types
    if k != "Washington":
        gender = v['Gender'].count()
        GENDER[k] = gender
        earliest_dob = v['Birth Year'].min()
        recent_dob = v['Birth Year'].max()
        most_common = v['Birth Year'].mode()
        DOB[k] = f"Earliest DOB: {earliest_dob}\nRecent DOB: {recent_dob}\nMost Common DOB: {most_common}"

print("\nUSER TYPES\n")
for k,v in USER_TYPE.items():
    print(f"User Types in {k}: ")
    print(v)

print("\nGENDER\n")
for k,v in GENDER.items():
    print(f"Gender count in {k}: ")
    print(v)

print("\nDate of Birth\n")
for k,v in DOB.items():
    print(f"Birth date statistics in {k}: ")
    print(v)