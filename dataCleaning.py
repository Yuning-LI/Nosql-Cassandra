import json
def dataCleaning (input_json_file, output_json_file):
    file_in = open(input_json_file, "r")
    file_out = open(output_json_file, "w")
    data = file_in.readlines() # read each json line in the dataset

    for line in data:
        json_data = json.loads(line) # get the json object
        json_data['id'] = json_data['_id']['$oid'] # rewrite the key "_id"
        del json_data['_id']
        
        json_data['toaddress'] = json_data['to'] # rewrite the key "to"
        del json_data['to']

        json_data['fname'] = int(json_data['fname'][:-1]) # rewrite the key "fname"

        oldline = json.dumps(json_data) # transform the json object to string

        newline = 'INSERT INTO emails JSON \'' + oldline + '\';' + '\n' # add CQL command
        file_out.writelines(newline)
    
    file_in.close()
    file_out.close()

dataCleaning('/Users/liyuning/Desktop/nosql/enron.json', '/Users/liyuning/Desktop/nosql/enronClean.json')