# define class
class Device:
    def __init__(self, name, IPaddress):
        self.name = name
        self.IPaddress = IPaddress
        print("Device name:", name)
        print("Device IP:", IPaddress)

class Location(Device):
    def __init__(self, name, IPaddress, location):
        super().__init__(name, IPaddress)
        print("Device location:", location)
      
c = Location("Cisco Switch", "10.0.10.2", "IT Department")
