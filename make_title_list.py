#Goal: Compile list of titles of json files and make a json file of titles titled titles.json

#Format 
# {"titles":["title0","title1","title2",...]}
#
#

# Use: python3

#GIVEN
#Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#Break into
#Lorem Ipsum is simply dummy text of the printing and typesetting industry
#Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book
#Find all .

import sys,re, json
from os import listdir

out_file = "titles.json"
#Not for every character
out_file_re = "^((?!titles.json).)*$"

#regex to find .json files
json_re = re.compile('\w*\.json')
re_not_out_file = re.compile(out_file_re)

json_fns = list(filter(json_re.match, listdir()))
json_fns = list(filter(re_not_out_file.match, json_fns))

json_titles = json.dumps({'titles':json_fns})


out_f = open(out_file, "w+")
out_f.write(json_titles)
out_f.close()
