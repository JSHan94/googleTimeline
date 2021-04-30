import pandas as pd 
import json
from pandas import json_normalize

from datetime import datetime

df = pd.read_json('2021_MARCH.json')["timelineObjects"]

for item in df:
    if "placeVisit" in item:
        place = item["placeVisit"]["location"]["name"]
        start_timeTS = int(item["placeVisit"]["duration"]["startTimestampMs"])/1000
        end_timeTS = int(item["placeVisit"]["duration"]["endTimestampMs"])/1000
        
        start_time = datetime.fromtimestamp(start_timeTS).strftime('%y-%m-%d %H:%M')
        end_time = datetime.fromtimestamp(end_timeTS).strftime('%y-%m-%d %H:%M')
        print("장소:"+ place,)
        print(start_time, "~" , end_time)
        print()
#with open('2021_MARCH.json') as json_file :
    
