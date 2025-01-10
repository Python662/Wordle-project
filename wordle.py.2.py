import random

def choose_secret_word():
    word_list = ["apple", "cheer","pause", "berry", "mango", "legal" "melon", "train" "grape", "lemon","truck"]
    return random.choice(word_list)
secret_word=choose_secret_word()
    
def wordle():
    print('Welcome to wordle!')
wordle()
for remaining_guesses in range(5,-1,-1):
    user_input=input('Enter your five letter word: ')

    for i in range (len(user_input)):
        letter = user_input[i]
        if letter == secret_word[i]:
            print(f"{letter} - Green")
        elif letter in secret_word:
            print(f"{letter} - Yellow")    
        else: 
            print(f"{letter} - red")

    if user_input==secret_word:
        print('You win!!!')
        break
print(f"The answer was:{secret_word} ")

