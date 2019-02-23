from wrangle import load_in_json, turn_google_location_json_into_pandas, turn_geo_df_into_shp, create_geometry

dict_json = load_in_json('data/location_download_20190218.json')
print('data loaded')

df = turn_google_location_json_into_pandas(dict_json)
print('data into pd')

df_geom = create_geometry(df)
print('create geom')

turn_geo_df_into_shp(df_geom, file='data/locations.shp')
print('saved to shp')
