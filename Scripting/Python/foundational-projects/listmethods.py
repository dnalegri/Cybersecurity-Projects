# Working with lists using various list methods
network_devices = ["Cox Gateway", "Fortinet10", "Linksys07"]
print(network_devices)

# Remove the first device from the list
network_devices.remove("Cox Gateway")
print(network_devices)

# Add device using append
network_devices.append("Cisco01")
print(network_devices)

# Add tuple seg1_switch using extend
seg1_switch = ("NETGEAR04", "NETGEAR05")
print(seg1_switch)
network_devices.extend(seg1_switch)
print("This is using extend: ", network_devices)

# Add tuple seg1_switch using append to see the difference
# tuples are not mutable, comment out rest of code
# it will break because tuples aren't mutable
#network_devices.append(seg1_switch)
#print("This is using append: ", network_devices)

# Count the item
print(network_devices.count("NETGEAR05"))
# Get the position of the item
network_item = network_devices.index("NETGEAR04")
print(network_item)

# Display last item in list
# Assign a variable
network_last = network_devices[-1]
print(network_last)

# or this way
print(network_devices[-1])

# Add Linksys12 to the list at the 3rd index
network_devices.insert(3, "Linksys12")
print(network_devices)

# Sort the list
network_devices.sort()
print(network_devices)
# Display reversed list
network_devices.reverse()
print(network_devices)

# Clear all items from the list
network_devices.clear()
print(network_devices)

