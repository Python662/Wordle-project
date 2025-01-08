import random

def choose_secret_word():
    word_list = ["apple", "berry", "mango", "peach", "grape", "banana", "strawberry", "rasberry", "blackberry"]
    return random.choice(word_list)

secret_word=choose_secret_word()


def wordle():

   print('Welcome to wordle! You have 5 guesses and the word must have only 5 letters.')
for remaining_guesses in range(4,-1,-1):

     print('Welcome to wordle! You have 5 guesses and the word must have only 5 letters.')
 
user_input=input('Enter your five letter word: ')
    
if user_input==secret_word:
        print('You win!')


print (f'The answer was:{secret_word}')

for i in range(5):
    if user_input[i] == secret_word:
        print == '🟩'  
    elif user_input[i] in secret_word:
        print == '🟨'  
else:
    print == '🟥'  