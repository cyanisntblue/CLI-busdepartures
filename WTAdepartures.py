import requests
import json
import time
from datetime import datetime

busstopid = input("Stop ID > ")

prediction_url = "https://api.ridewta.com/stops/" + busstopid + "/predictions"
print("URL IS: " + prediction_url)

# Call API
response = requests.get(prediction_url)

# Print API response code for fun and debug type beat
debugmode = False

if debugmode == True:
    if response.status_code == 200:
        print("Success! Code is " + str(response.status_code))
    else:
        print("Error? Code is " + str(response.status_code))

# print(response.json()) in debug mode
    json_response = response.json()
    pretty_response = json.dumps(json_response, indent=4)
    print(pretty_response)

# Line Break!
print(" ")

# Current time!!!
print("THE TIME IS: ")
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# 24 -> 12 hr
if int(current_time[0:2]) >= 13:
    current_time12hr = str(int(current_time[0:2]) - 12) + current_time[2:] + " PM"
else:
    current_time12hr = current_time + " AM"

print(current_time12hr)

#print("")

# print stop name
stopname = response.json()['bustime-response']['prd'][1]['stpnm']

# little dashed line visual seperation
print("-"*len(stopname + " departures:"))
#print("")
print(stopname + " departures:")
print("")

# attempt at parsing json data and printing relevant info (des+prdtm)
# have to step down json? idk if that makes sense but every arg [] is a step down (9: is literally chopping the date off itll probably break eventually)

xint = 0

# will return up to 12(?) max (API limit) in one request, modify xint range below
for xint in range (3):
    des = response.json()['bustime-response']['prd'][xint]['des']
    prdtm = response.json()['bustime-response']['prd'][xint]['prdtm'][9:]

    # calculate difference between current time and bus arrival time
    hourdelta = int(prdtm[0:2]) - int(current_time[0:2])
    minutedelta = int(prdtm[3:5]) - int(current_time[3:5])
        
    # 24 hr -> 12 hr
    if int(prdtm[0:2]) >= 13:
        prdtm12hr = str(int(prdtm[0:2]) - 12) + prdtm[2:] + " PM"
    else:
        prdtm12hr = prdtm + " AM"

    # add 60 minutes for each hour 
    if hourdelta >= 1: 
        minutedelta = minutedelta + (hourdelta*60)

    # if 1, use minute instead of minutes
    if minutedelta == 1:
        minutestowait = str(minutedelta) + " minute"
    else:
        minutestowait = str(minutedelta) + " minutes"


    # profit
    print(des)
    print(minutestowait)
    print(prdtm12hr)
    print(" ")