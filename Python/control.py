# for x in range(0,10):
#     print(f"Value of x: {x}")
#     answer = input("Press y then enter to end.")
#     if answer == "y":
#         break #End the loop early

x = 10
y = 15

while x < y:
    print(f"Value of x is: {x}")
    answer = input("Press y then enter to end.")

    if answer == "y":
        pass
        #Do some code in the future

        # continue #Iterate a loop early
        # break

    x += 1
else: #Execute when a loop is finished
    print("The whole loop ran.")
    
print("This is the end of my code")
y