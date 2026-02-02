import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "computer"]
hard_words = ["elephant", "diamond", "umberalla", "fantastic","outstanding","consequences"]

print("Welcome To Password Gaming Game")
print("Choose The Difficulty Level (easy , medium, hard)")

level = input("Enter Difficluty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalide Choice!, Defualt: Easy")
    secret = random.choice(easy_words)
attempts = 0
print("\n Guess The Secret Word")

while True:
    guess = input("Enter Your Guess: ").lower()
    
    if guess == "exit":
        print("Thanks for playing! Game Over")
        break
    
    attempts += 1

    if guess == secret:
        print(f"Congretulations! You Guessed The Word In {attempts} Attempts")
        break
    
    hint=""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
    else:
        hint += "_"
    print("Hint: ", hint)
print("Game Over")