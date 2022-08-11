#name = input("What is your name? ")
#age = input("What is your age? ")

#message1 = "Hello {fname}, your age is {fage}".format(fname=name, fage=age)
#print(message1)

#message2 = "Hello {0}, your age is {1}".format(name, age)
#print(message2)

#message3 = "Hello {}, your age is {}".format(name, age)
#print(message3)

platform = input("What is your platform? ")
show_command = input("What show command do you want to send? ")
platform_to_test = platform.lower()

if platform_to_test == "cisco":
    commands_to_send = f"enable\n{show_command}\n"
    print(commands_to_send)
