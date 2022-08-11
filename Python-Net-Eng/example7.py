login_name = input("Please create your login name: ")

while len(login_name) < 8:
    print("FAILED! Login name must be at least 8 characters")
    login_name = input("Please create your login name: ")