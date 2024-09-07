import random


words = ["hello", "world", "python", "hangman", "game", " coding", "challenge", "adventure"]

word = random.choice(words)

underscores = ["_"] * len(word)

incorrect_guesses_allowed = 3

print("Welcome to Hangman!")
print("I'm thinking of a word that has", " ".join(underscores), "letters.")
print("You have", incorrect_guesses_allowed, "chances to guess incorrectly.")

while True:
   
    guess = input("What's your next guess? ").lower()

    if len(guess) != 1:
        print("Please enter a single letter!")
        continue

    if guess in word:
        
        for i, letter in enumerate(word):
            if letter == guess:
                underscores[i] = guess
    else:
        
        incorrect_guesses_allowed -= 1
        print("Incorrect guess! You have", incorrect_guesses_allowed, "chances left.")

    
    print(" ".join(underscores))
    

    if "_" not in underscores:
        print(" Congratulations! You won!")
        break
    elif incorrect_guesses_allowed == 0:
        print(" Sorry, you lost! The word was", word)
        break