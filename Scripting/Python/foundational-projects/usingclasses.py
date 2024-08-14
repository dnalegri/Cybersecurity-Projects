# define class
class Devices:
    "Common base class for network devices"

    # variable shared among instances
    device_count = 0

    # class constructor
    def __init__(self, name, IPaddress):
        self.name = name
        self.IPaddress = IPaddress
        Devices.device_count += 1

    # member methods
    def displayCount(self):
        print("Total Devices:", Devices.device_count)

    def displayDevices(self):
        print("Name: ", self.name, "IP Address: ", self.IPaddress)

# create instances
dev1 = Devices("Cisco Router", "192.100.0.10")
dev2 = Devices("Netgear Switch", "10.10.0.29")

# access objects' attributes
dev1.displayDevices()
dev2.displayDevices()
print("Total Devices: ", Devices.device_count)
