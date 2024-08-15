import os
pwd = os.getcwd()
list_directory = os.listdir(pwd)

for directory in list_directory:
    print('[+]', directory)

# get sub directories below

#for root, directories, files in os.walk(".", topdown=False):
    # iterate over the files
    #for file_entry in files:
        # create the relative path
        #print("[+]", os.path.join(root, file_entry))
    #for name in directories:
        #print("[++]", name)
