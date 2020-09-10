from random import randint
while True:
    guess_name = input("Hello, what's your name? ")
    if guess_name.isalpha():
        break
    else:
        print("Add a proper name with alphabet, for God's sake!")

print(f"okay! {guess_name}, I am guessing a number between 1 and 10")
number_of_guesses = 0
number = randint(1, 10)
while number_of_guesses < 5:
    guess = int(input("your guess? : "))
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too low")
    elif guess == number:
        break
if guess is number:
    print(f"Congrats! You have guessed it in {str(number_of_guesses)} times.")
else:
    print(f"You could not guess the number in 5/5 attempts. Loser!")
