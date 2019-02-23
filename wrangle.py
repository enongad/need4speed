import json
import pandas as pd
from pytz import timezone
from datetime import datetime as dt
from shapely.geometry import Point

def load_in_json(file):
    with open(file) as json_data:
        d = json.load(json_data)
    return d

def turn_google_location_json_into_pandas(json_dictionary):

    # variables to extract from json
    date = []
    time = []
    time_perth = []
    latitude = []
    longitude = []
    accuracy = []
    altitude = []
    vertical_acc = []
    mode = []
    utc = timezone('UTC')
    perth = timezone('Australia/Perth')

    # iterate through all point locations in the dictionary
    for point in json_dictionary['locations']:
        time_temp = dt.utcfromtimestamp(int(point['timestampMs']) / 1000)
        time.append(utc.localize(time_temp).strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        time_perth.append(utc.localize(time_temp).astimezone(perth).strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        date.append(dt.utcfromtimestamp(int(point['timestampMs']) / 1000).strftime("%Y-%m-%d"))
        latitude.append(point['latitudeE7'] / 10000000)
        longitude.append(point['longitudeE7'] / 10000000)
        accuracy.append(point['accuracy'])
        if 'altitude' in point.keys():
            altitude.append(point['altitude'])
        else:
            altitude.append('NaN')
        if 'verticalAccuracy' in point.keys():
            vertical_acc.append(point['verticalAccuracy'])
        else:
            vertical_acc.append('NaN')
        if 'activity' in point.keys():
            # print(point['activity'][0])
            mode.append(point['activity'][0]['activity'][0]['type'])
        else:
            mode.append(" ")

    df = pd.DataFrame(
        {'date': date, 'time': time, 'timeperth': time_perth, 'latitude': latitude, 'longitude': longitude,
         'accuracy': accuracy, 'altitude': altitude, 'vert_acc': vertical_acc, 'mode': mode})

    df['geometry'] = df.apply(lambda x: Point((float(x.longitude), float(x.latitude))), axis=1)

    return df