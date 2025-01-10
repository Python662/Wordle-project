import random

def choose_secret_word():
    word_list =["apple","lemon","melon","peach","mango", "grape", "pears"]


    return random.choice(word_list)
secret_word=choose_secret_word()
print(secret_word)
def wordle():
    print('Welcome to wordle!')
wordle()
for remaining_guesses in range(5,-1,-1):
    user_input=input('Enter your five letter word: ')

    for i in range (len(user_input)):
        letter = user_input[i]
        if letter == secret_word[i]:
            print(f"{letter} - 🟩")
        elif letter in secret_word:
            print(f"{letter} - 🟨")    
        else: 
            print(f"{letter} - 🟥")

    if user_input==secret_word:
        print('You win!!!')
        break
print(f"The answer was:{secret_word} ")

