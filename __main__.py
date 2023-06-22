from search import search, search_l2
import sys

"""
repo: https://github.com/muhammads97/gportal_search_api_python.git
clone the repo and change the path bellow
"""
sys.path.append("/Users/salah/workspace/gportal_api") ## change this to the path of gportal api
from gportal_api import GportalApi

if __name__ == "__main__":
  # csv = "/Users/salah/workspace/data/in-situ-chla-2018-2020.csv"
  token = "7726524198fa59edb5564f6d939d5b168f1ed1d3288434f000028e2d1d982695f88f11a240a224e75516bca03d3aa9ec38d8dbf918b329733c0329003e9ec10f"
  # api = GportalApi(token, "l1b_VNR")
  api_l2_rrs = GportalApi(token, "l2_NWLR")
  api_l2_prods = GportalApi(token, "l2_IWPR")
  lvl1_name = "l1b"
  lvl2_rrs_name = "l2_rrs"
  lvl2_prod_name = "l2_prod"
  # print("=========level 1========")
  # search(csv, api, lvl1_name)
  csv = "./results.csv" ## change to the csv file
  print("=========level 2 Rrs========")
  search_l2(csv, api_l2_rrs, lvl2_rrs_name)
  print("=========level 2 Products========")
  search_l2(csv, api_l2_prods, lvl2_prod_name)