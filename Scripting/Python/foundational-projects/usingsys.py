# using sys module
import sys

# getting script name
print("Script name:", sys.argv[0])

# number of arg
print("Number of arguments:", len(sys.argv))

# platform
print("Platform:", sys.platform)

# py v
print("Python version:", sys.version)

# encoding
print("Encoding and default encoding:", sys.getfilesystemencoding(), sys.getdefaultencoding())

# path
print("Environment variable path:", sys.path)
