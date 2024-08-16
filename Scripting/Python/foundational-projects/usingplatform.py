import platform
current_os = platform.system()
print("Your OS:", current_os)

# use control statements to display commands
# to find IP address info on different platforms
if current_os == "Windows":
    ip_command = "ipconfig /all"
elif current_os == "Linux":
    ip_command = "ipaddr"
elif current_os == "Mac":
    ip_command = "ipconfig getifaddr en1"
print(ip_command)

from platform import python_implementation, python_version_tuple
print(python_implementation())
for attributes in python_version_tuple():
    print(attributes)
