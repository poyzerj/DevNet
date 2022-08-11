my_list_of_devices = ["R1", "R2", "R3", "R4", "CoreSwitch", "Distroswitch1", "Distro2", "Access1", "Access2"]

for device in my_list_of_devices:
    print(f"I have device {device} in my network")

#################################################################################################################

intf_list = ["interface g0/0", "interface g0/1", "loopback0"]

for int in intf_list:
    print(f"{int}\n ip ospf 1 area 0")