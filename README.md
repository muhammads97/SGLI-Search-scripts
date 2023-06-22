# SGLI-Search-scripts

## files

### __main__
you'll find example usage
you can run by changing the path to the gportal_api (this repo: https://github.com/muhammads97/gportal_search_api_python.git)
and add your token

### search

main search scripts:

1. search -> searchs for level 1
2. search_l2 -> searchs for level 2

#### csv_file_path -> file that contains coordinates and date of desired image
#### api -> gportal_api instance
#### lvl_name -> string for the header in the otput csv
#### no_repeat -> won't search for the the image if the id aleardy exist in the excel sheet

#### the ids will be saved in the same csv input file


### utils
just some helper functions
