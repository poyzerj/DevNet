name = "Joe"
age = 36

print("Hello",name,", you are",age, "years old.")

print("Hello " + name + ", you are " + str(age) + " years old.")

print("Hello %s, you are %s years old" % (name,age))

print("Hello {}, you are {} years old.".format(name,age))

print(f"Hello {name}, you are {age} years old!")

print(f"Hello {name}, in ten years, you'll be {age + 10} years old!")

message = (
    f"Hello {name}, "
    f"You are {age} years old. "
    f"In ten years, you'll be {age + 10} years old!"
)

print(message)