from wrangle import load_in_json, turn_google_location_json_into_pandas


dict_json = load_in_json('data/location_download_20190218.json')

turn_google_location_json_into_pandas(dict_json)

