name1 = "Joe"
name2 = "Poyzer"

#Concatenation
value = name1 + " " + name2
print(value)

#Repitition
value = name1 * 3
print(value)

#Slice
value = name1[0]
print(value)

#Range Slice
value = name1[0:2]
print(value)

#Membership
if "oe" in name1:
    print("It is in the string!")

if "J" not in name1:
    print("Nope not this one")

print(r"Hello\r\nThere")