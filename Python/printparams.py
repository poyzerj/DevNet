fileObject = open("output.txt", mode="w")
print("Hello Joe!", file=fileObject)

print("Hello", "Joe", "ThirdValue",sep=":")

print("Hello",end="")
print("Goodbye")

print("Hello", "Joe", "ThirdValue",end="",sep=":")

print("Hello", "Joe", "ThirdValue",sep="-", end="xx")