device_list = ["G0/1", "G0/2", "G0/3", "G0/4", "Loopback0", "Loopback1"]

#for device in device_list:
#    if device == "G0/2":
#        continue
#    print(device)

for device in device_list:
    if device.startswith("L"):
        continue
    print(device)