# A guess game of 1o attempts
import random
secret_number = random.randint(1, 30)
attempt = 0
max_attempt = 10
print("Welcome to Guess Game")
print("I'd think of a number between 1 and 30")
print("Can u guess it within {} attempt".format(max_attempt))

while attempt < max_attempt:
    print("\nYour remaining attempt is:", max_attempt-attempt)
    guess = int(input("Enter your number:"))
    if guess < secret_number:
        print("Too low, try again")
    elif guess > secret_number:
        print("Too high, try again")
    else:
        print("Congratulations, you guessed the number {} correctly.".format(secret_number) )
        break
    attempt +=1
    if attempt == max_attempt:
        print("Unfortunately you are run out of the total number of attempts the number is", secret_number)