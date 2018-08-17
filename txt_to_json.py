#Goal: convert regular text into more readable json for WOz prototype

# Use: python3 txt_to_json.py input_file.txt output_file.json

#GIVEN
#Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#Break into
#Lorem Ipsum is simply dummy text of the printing and typesetting industry
#Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book
#Find all .

import re,json,sys

if len(sys.argv) == 3:
    input_file = sys.argv[1] #input file
    out_file = sys.argv[2] #output file

sentence_RE = r'[^.?!\n]+'
pattern = re.compile(sentence_RE)

#remove whitespace, new lines
trim = lambda s: s.strip()
breakdown = lambda s: s.split()
with open(input_file) as file:
    file_contents = file.read()
    file_contents = file_contents.replace('\n', ' ').replace('\r', '')    
    sentences = list(map(trim,pattern.findall(file_contents)))
    sentence_breakdowns = list(map(breakdown,sentences))
    json_results = json.dumps({'sentences':sentences, 'sentence_breakdowns':sentence_breakdowns})
    
    out_f = open(out_file, "w+")
    out_f.write(json_results)
    out_f.close()
