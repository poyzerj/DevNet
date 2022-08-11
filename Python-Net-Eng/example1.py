vendor = input("Enter the vendor you wish to automate: ")

if vendor == "cisco":
    print("You have selected Cisco")

elif vendor == "juniper":
    print("You have selected Juniper")

elif vendor == "arista":
    print("You have selected Arista")

elif vendor == "aruba":
    print("You have selected Aruba")

else:
    print("Unrecognized vendor")