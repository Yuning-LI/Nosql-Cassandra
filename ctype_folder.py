import json
def dataReform (input_json_file, output_json_file):
    file_in = open(input_json_file, "r")
    file_out = open(output_json_file, "w")
    data = file_in.readlines() # read each json line in the dataset

    for line in data:
        json_data = json.loads(line) # get the json object
        newjson = {}
        newjson['id'] = json_data['_id']['$oid']
        newjson['ctype'] = json_data['ctype']
        newjson['folder'] = json_data['folder']

        oldline = json.dumps(newjson) # transform the json object to string

        # add the CQL insert command
        newline = 'INSERT INTO ctype_folder JSON \'' + oldline + '\';' + '\n' # add CQL command
        file_out.writelines(newline)
    
    file_in.close()
    file_out.close()

dataReform('/Users/liyuning/Desktop/nosql/enron.json', '/Users/liyuning/Desktop/nosql/ctype_folder.json')