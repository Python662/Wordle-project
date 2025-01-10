import random

def choose_secret_word():
    word_list = ["apple", "berry", "mango", "peach", "grape", "banana", "strawberry", "rasberry", "blackberry"]
    return random.choice(word_list)

def wordle():
    print('Welcome to Wordle!')

secret_word = choose_secret_word()
wordle()

for remaining_guesses in range(5, -1, -1):  # 6 attempts (5 down to 0)
    user_input = input(f'Guess #{6 - remaining_guesses}: Enter your fruit: ').lower()  # Ensure case-insensitivity

    if user_input == secret_word:
        print('You win!')
        break
    
    # Provide feedback for each letter in the user's guess
    for i in range(len(user_input)):
        letter = user_input
        
       