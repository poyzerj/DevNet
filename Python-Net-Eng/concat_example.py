command_string = input("Enter the command you wish to send to the device: ")

commands_to_send = "enable\n" + command_string + "\n"

print(commands_to_send)