import json
JSON_FILE_PATH=r"C:\\Users\\db\\Desktop\\intern\\temp.json"

with open(JSON_FILE_PATH,"r") as directoryTree:
    directoryJson=json.load(directoryTree)

def traverseJson(directoryJson):
    if 'children' in directoryJson: # if children present in current folder go inside
        if len(directoryJson['children'])!=0 or directoryJson['children']!=None:
            
            print("Folder Path:",directoryJson['path'])
            #Recursive Call for function to traverse whole JSON file.
            for i in range(len(directoryJson['children'])):
                traverseJson(directoryJson['children'][i])

    else: # if no children found then it is a file.
        #CQL query to create file node
        print("File path",directoryJson['path'])
        print('--------------')

#Recursively Traverses the Json File.
traverseJson(directoryJson)
