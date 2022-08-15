
#The secred word the player is trying to guess
secretWord = "CBTNuggets"
lettersGuessed = ""

#The number of turns before the player loses
failureCount = 6

#Loop until the player has made too many failed attempts
#Will 'break' loop if they succed instead
while failureCount > 0:

    #Get a guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secretWord:
        #Player guessed a correct letter!
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect. There are {guess} in the secret word. {failureCount} turn(s) left.")

    #Maintain a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
    print("")
    #If there were no wrong letters, then the player won!
    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secretWord}. You won!")
        break

else:
    print("Sorry, you didn't win it this time. Try again!")