'''
file name   : directoryTree_toJson.py

description : This file converts directory structure into its 
            corresponding json format.

input       :
        path of directory,
        variable.py file contains details of files and folders that 
        are to be excluded while creating the json format.

output      :
        directoryTree.json: json file format for a given directory.

author      : Aryan Mehta <aryancountry@gmail.com>

'''
import os
import json
#from variable import *

JSON_FILE_PATH='directoryTree.json'
DIRECTORY_PATH='.\RootFolder'

def path_to_dict(path):
    '''
    function name: path_to_dict
    description  : A recursive function to generate a dynamic dictionary 
                  which holds folder structure.
    input        : path of directory
    output       : returns dictionary (d)
    author       : Aryan Mehta <aryancountry@gmail.com>
    '''
    name=os.path.basename(path)
    d={}
    if name in excludeFolders or name in excludeFiles:
        return None
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['path']=path
        d['features']=[]
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d['path']=path
        filename=os.path.basename(path)
        if filename.endswith('.c') or filename.endswith('.cpp'):
            d['features']=[]
    print(d)
    return d

with open(JSON_FILE_PATH,'w') as directoryTree:
    json.dump(path_to_dict(DIRECTORY_PATH),directoryTree,indent=4)
