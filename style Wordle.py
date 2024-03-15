import nltk
nltk.download('words')
from nltk.corpus import words

## Function to check word
##Part is used to determine if checking secret word or a guess
def c_word(word, part): 
    man = False
    if part == 0:
        x = 'Enter the secret 5-letter word: '
        while (man == False):
            if word in words.words():
                if len(word) == 5:
                    man = True
                else:
                    print('Not a valid word, try again!')
                    word = str(input(x))
            else:
                print('Not a valid word, try again!')
                word = str(input(x))
    else:
        x = f'Enter your attempt #{N}\n'
        while (man == False):
            if word in words.words():
                if len(word) == 5:
                    print ('You entered a 5-letter word')
                    man = True
                else:
                    print(f'You entered a {len(word)}-letter word, but a 5-letter word is needed. Try again')
                    word = str(input(x))
            else:
                print('Not a valid word, try again')
                word = str(input(x))
    return word

##Setting up Variables
N = 1
letter_in_the_right_spot = 0
same_let = False
c_spot = False
is_word = False

##Start Game
print ('Welcome to Wordle - CECS 174 edition!')
secret_word = str(input('Enter the secret 5-letter word: '))
secret_word = c_word(secret_word, 0)
secret_list = list(secret_word)

##Stopping code if the attempt is 0

cont = True
attempts = int(input('Input allowed number of attempts: '))
if attempts == 0:
    cont = False

if cont == False:
    print(end='')
else:
    player_word = input(f'Enter your attempt #{N}\n')
    player_word = c_word(player_word, 1)
  ##Word check
while N <= attempts and cont == True:   
        letter_in_the_right_spot = 0
        in_word = False
        c_spot = False

        for i in range(0,5):
            in_word = False
            if player_word[i] == secret_word[i]:
                letter_in_the_right_spot += 1
                print (f'{player_word[i]} is in the secret_word and in the correct spot #{i+1}')
                print (f'Correct letters in the correct spot: {letter_in_the_right_spot}')
            else:
                in_word = False
                for o in secret_list:
                    if o == player_word[i]:
                        in_word = True
                if in_word == True:
                    print(f'{player_word[i]} is in the secret_word but not in the correct spot')
             
        if player_word == secret_word:
            print (f'Congrats you won using {N} attempt(s)')
            is_word = True
            break

        if N == attempts:
            break
        N += 1
        player_word = input(f'Enter your attempt #{N}\n')
        player_word = c_word(player_word, 1)
        
if is_word == False and cont == True:
    print (f'You already used #{attempts} attempts. Better luck tomorrow!')
