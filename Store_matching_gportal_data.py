def get_download_link(feature):
  return feature["properties"]["product"]["fileName"]

def get_size(feature):
  return feature["properties"]["product"]["size"]

def get_id(feature):
    return feature["properties"]["identifier"]

def store_data(csv, index, feature, lvl_name):
  index = csv.index[index]
  # if "gportal_id" not in csv.columns:
  #   csv["gportal_id"] = ""
  # if "gportal_link" not in csv.columns:
  #   csv["gportal_link"] = ""
  # if "gportal_size" not in csv.columns:
  #   csv["gportal_size"] = ""
  csv.loc[index, "%s_gportal_id"%lvl_name] = get_id(feature)
  csv.loc[index, "%s_gportal_link"%lvl_name] = get_download_link(feature)
  csv.loc[index, "%s_gportal_size"%lvl_name] = get_size(feature)
  return csv


  
