import pandas as pd
import datetime as dt


def get_way_points_driving(df, minutes=5):

    # 'date', 'time', 'timeperth', 'latitude', 'longitude', 'accuracy', 'altitude', 'vert_acc', 'mode', 'geometry'
    df = df.loc[df['mode'] == 'IN_VEHICLE'].sort_values('time').reset_index()

    start_long = []
    start_lat = []
    end_long = []
    end_lat = []
    time_taken = []
    time_start = []

    for index, row in df.head(100).iterrows():

        if index == 0:
            continue

        # Format dates
        # 2019-02-18 04:21:02 UTC+0000
        format_str = "%Y-%m-%d %H:%M:%S %Z%z"

        time_c = dt.datetime.strptime(df['time'].loc[index], format_str)
        time_l = dt.datetime.strptime(df['time'].loc[index-1], format_str)

        time_difference = (time_c - time_l).total_seconds()/60

        if time_difference <= minutes:

            start_long.append(df['longitude'].loc[index-1])
            start_lat.append(df['latitude'].loc[index-1])
            end_long.append(row.longitude)
            end_lat.append(row.latitude)
            time_taken.append(time_difference)
            time_start.append(time_l)

    trips = pd.DataFrame({'start_longitude':start_long, 'start_latitude': start_lat,
                          'end_longitude':end_long, 'end_latitude': end_lat,
                          'time_taken':time_taken, 'start_time': time_start})
    return trips
