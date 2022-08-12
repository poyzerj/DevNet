#Ask a user their name and age and tell them some things about themself

userName = (input("What is your name? "))
userAge = (input("How old are you? "))
userAgeInt = int(userAge)

print("Hello there " + userName)

userAgeTenTime = userAgeInt * 10
print("Your age times ten is " + (str(userAgeTenTime)) + ".")

if (userAgeInt >= 18):
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")
