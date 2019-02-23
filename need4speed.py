from wrangle import load_in_json, turn_google_location_json_into_pandas, turn_geo_df_into_shp, create_geometry

dict_json = load_in_json('data/location_download_20190218.json')

df = turn_google_location_json_into_pandas(dict_json)

df_geom = create_geometry(df)

turn_geo_df_into_shp(df_geom, file='data/locations.shp')
