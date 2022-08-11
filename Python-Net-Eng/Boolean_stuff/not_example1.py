my_list_of_protocols = ["RIP", "EIGRP", "OSPF", "ISIS"]

if "OSPF" not in my_list_of_protocols:
    print("No path vector protocols are present")
else:
    print("Path vector detected")