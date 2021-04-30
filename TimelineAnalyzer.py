import pandas as pd 
import json
from pandas import json_normalize

from datetime import datetime
from collections import Counter

df = pd.read_json('2021_MARCH.json')["timelineObjects"]

location_list = []
for item in df:
    if "placeVisit" in item:
        place = item["placeVisit"]["location"]["name"]
        start_timeTS = int(item["placeVisit"]["duration"]["startTimestampMs"])/1000
        end_timeTS = int(item["placeVisit"]["duration"]["endTimestampMs"])/1000
        
        start_time = datetime.fromtimestamp(start_timeTS).strftime('%H:%M')
        end_time = datetime.fromtimestamp(end_timeTS).strftime('%H:%M')
        weekday = datetime.fromtimestamp(start_timeTS).weekday()
        
        location_list.append([place,start_time,end_time,weekday])
        #print("장소:"+ place,weekday,start_time,end_time)
        #print(start_time, "~" , end_time)
        #print()

print("mon = 0, sun = 6")
in_weekday = int(input("what day is it? : "))
in_time = input("what time? : ")

possible_action = []
for item in location_list:
    if item[1]<in_time<item[2] and item[3] == in_weekday:
        possible_action.append(item[0])

print(possible_action)


   
