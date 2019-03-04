from wrangle import load_in_json, turn_google_location_json_into_pandas, turn_geo_df_into_shp, create_geometry
from spatial import get_way_points_driving
import pandas as pd

# dict_json = load_in_json('data/location_download_20190218.json')
# print('data loaded')
#
# df = turn_google_location_json_into_pandas(dict_json)
# print('data into pd')
#
# df.to_csv('data/locations_df.csv')

#

# df_geom = create_geometry(df)
# print('create geom')
#
# turn_geo_df_into_shp(df_geom, file='data/locations.shp')
# print('saved to shp')

# get_way_points_driving(df)


df = pd.read_csv('data/locations_df.csv')

print(get_way_points_driving(df))
