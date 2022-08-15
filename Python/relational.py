x = 10
y = 15
z = 10.0

print(x > y)
print(y > x)
print(x == y)
print(x != y)

if(x > y):
    print("X is bigger than y!")
else:
    print("Y is bigger than (or equal to) x!")


print(z == x)

print(z == x and x == y)