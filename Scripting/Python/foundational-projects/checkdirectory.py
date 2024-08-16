# get current working directory
import os
pwd = os.getcwd()
list_directory = os.listdir(pwd)

for directory in list_directory:
    print('[+]', directory)
# get sub directories
# import os
for root, directories, files in os.walk(".", topdown=False):
    # iterate over the files
    for file_entry in files:
        # create the relative path
        print("[+]", os.path.join(root, file_entry))
    for name in directories:
        print("[++]", name)
# use os.walk() and Count() in collections to count items in current directory
from collections import Counter
counts = Counter()
for currentdir, dirnames, filenames in os.walk("."):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
for extension, count in counts.items():
    print(f"{extension:8}{count}")
