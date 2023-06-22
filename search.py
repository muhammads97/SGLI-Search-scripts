import pandas as pd
from dateutil import parser
from Store_matching_gportal_data import store_data

def search(csv_file_path, api, lvl_name, no_repeat=False):
  df = pd.read_csv(csv_file_path)
  for index, row in df.iterrows():
    print("searching for data at index %d"%index)
    if no_repeat and len(str(row["%s_gportal_id"%lvl_name])) == 41:
      continue
    try:
      date = parser.parse(row["Date"])
    except:
      print("couldn't process date")
      continue
    date = date.strftime("%Y/%m/%d")
    lat = row["lat"]
    long = row["lon"]
    if lat == 0 or long == 0:
      print("bad lat and long")
      continue
    res = api.search(date, date, coordinates=(long,lat), cloud=20,count = 1000, resolution="250m")
    print("found %d results"%len(res))
    if len(res) > 0:
      store_data(df, index, res[0], lvl_name)
    if (index+1) % 100 == 0:
      df.to_csv("./results.csv")
  df.to_csv("./results.csv")

def search_l2(csv_file_path, api, lvl_name, no_repeat=False):
  df = pd.read_csv(csv_file_path)
  for index, row in df.iterrows():
    print("searching for data at index %d"%index)
    if no_repeat and len(str(row["%s_gportal_id"%lvl_name])) == 41:
      continue
    try:
      date = parser.parse(row["Date"])
    except:
      print("couldn't process date")
      continue
    date = date.strftime("%Y/%m/%d")
    lat = row["lat"]
    long = row["lon"]
    if lat == 0 or long == 0:
      print("bad lat and long")
      continue
    l1b = str(row["l1b_gportal_id"])
    if l1b != "nan":
      print("level 1 id: %s"%l1b)
      path_number = l1b[20:23]
      scene_number = l1b[23:25]
      print("path: %s, scene: %s"%(path_number, scene_number))
    else:
      path_number=None
      scene_number=None
    res = api.search(date, date, coordinates=(long,lat), cloud=20,count = 1000,path_number=path_number, scene_number=scene_number, resolution="250m")
    print("found %d results"%len(res))
    if len(res) > 0:
      store_data(df, index, res[0], lvl_name)
    if (index+1) % 100 == 0:
      df.to_csv("./results.csv")
  df.to_csv("./results.csv")
