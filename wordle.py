import random

def choose_secret_word():
    word_list = ["apple", "berry", "mango", "peach", "grape", "banana", "strawberry", "rasberry", "blackberry"]
    return random.choice(word_list)
secret_word=choose_secret_word()

def wordle():
     
    for remaining_guesses in range(5,-1,-1):
     user_input=input('Enter a fruit: ')
    
    if user_input==secret_word:
        print('You win!')
    


print (f'The answer was:{secret_word}')

