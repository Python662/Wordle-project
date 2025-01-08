import random

def choose_secret_word():
    word_list = ["apple", "berry", "mango", "peach", "grape", "banana", "strawberry", "rasberry", "blackberry"]
    return random.choice(word_list)
secret_word=choose_secret_word()
print(secret_word)
    
def give_feedback(guess, secret_word):
    feedback = []

    secret_word_list = list(secret_word)
user_input = list(guess)

for i in range(len(guess)):
        if guess[i]==secret_word[i]:
            feedback.append("green")
            secret_word_list[i] = (None)
            guess_list[i] = (None)
        else:
            feedback.append(None)
    for i in range(len(guess)):
        if feedback[i] is None and guess_list[i] is not None:
            if guess_list[i] in secret_word_list:
                feedback[i] = "yellow"
                secret_word_list[secret_word_list.index(guess_list[i])] = None
        else: feedback[i] = "red"

    return " ".join(feedback)
def wordle():
    print('Welcome to wordle!')
    wordle()
for remaining_guesses in range(5,-1,-1):
    user_input=input('Enter your fruit: ')
    
    if user_input==secret_word:
        print('You win!')
        break
print (f'The answer was:{secret_word}')