import string

WORD_LENGTH = 5
def read_dictionary(filename):
    new_dictionary_list = []
    dictionary=open(filename)
    dictionary_list=dictionary.readlines()
    for word in dictionary_list:
        word=word[:-1].lower()
        new_dictionary_list.append(word)
    dictionary.close()
    return new_dictionary_list  # a list of strings with lowercase letters

def enter_a_word(word_type, num_letters):
    a_word=input(f'Enter the {num_letters}-letter {word_type} word: ')
    a_word=a_word.lower()
    return a_word  # a string with lowercase letters

def is_it_a_word(input_word, dictionary_list): #D
    if input_word in dictionary_list:
        is_word=True
    else:
        is_word=False
    return is_word

def enter_and_check(word_type, dictionary_list): #E
    in_word=enter_a_word(word_type, WORD_LENGTH)
    in_dict=is_it_a_word(in_word, dictionary_list)
    length=len(in_word)
    nott=''
    while length != WORD_LENGTH or in_dict==False:
        if in_dict==False:
            nott=' not '
        else:
            nott=' '
        print(f'You entered a {length}-letter word that is{nott}in the dictionary. Please try again!')
        in_word=enter_a_word(word_type,WORD_LENGTH)
        in_dict=is_it_a_word(in_word,dictionary_list)
        length=len(in_word)
        nott=''
    return in_word  # a string - valid input word


def compare_words(player, secret): #F
    global remaining_alphabet
    global in_secret_word_correct_spot
    global in_secret_word_somewhere
    global not_in_secret_word

    final = ''
    in_correct_spot = 0
    for letter in player:
        num_letter=secret.count(letter)
        if num_letter > 0:
            if player.find(letter) == secret.find(letter): #check in secret word and correct spot
                final += letter
                in_correct_spot += 1
                if letter not in in_secret_word_correct_spot:
                    in_secret_word_correct_spot.append(letter) #keep in append if the letter is not yet show up
            else: #in word but wrong spot
                final += '(' + letter + ')'
                if letter not in in_secret_word_somewhere:
                    in_secret_word_somewhere.append(letter)
        else: #not in word
            final += '_'
            if letter not in not_in_secret_word:
                not_in_secret_word.append(letter)
        if letter in remaining_alphabet:
            remaining_alphabet.remove(letter) #remove letter from alphabet if already used
    return final, in_correct_spot  # returns a string and an integer

# program code
print('Welcome to new and improved Wordle - CECS 174 edition!')
alphabet_string = string.ascii_lowercase  # Create a string of all lowercase letters
remaining_alphabet = list(alphabet_string)  # Create a list of all lowercase letters


in_secret_word_correct_spot = []
in_secret_word_somewhere = []
not_in_secret_word = []
words_list = read_dictionary('project4_dictionary')
secret_word= enter_and_check('secret',words_list)
N=int(input('Input allowed number of attempts: '))
if N>0:
    attempts=1
    print('Enter your attempt #' + str(attempts))
    player_word = enter_and_check('player',words_list)
    while attempts <= N:
        final_word, letter_in_correct_spot = compare_words(player_word,secret_word)
        print('letter in the right spot:',letter_in_correct_spot)
        print('You guessed letters of the secret_word:',final_word)
        print('Previously attempted letters that are in the correct spot of secret_word:','\n'+str(in_secret_word_correct_spot))
        print('Previously attempted letters that are in some spot of secret_word:','\n'+str(in_secret_word_somewhere))
        print('Previously attempted letters that are not in the secret_word:','\n'+str(not_in_secret_word))
        print('Remaining letters of the alphabet that have not been tried:','\n'+str(remaining_alphabet))
        if player_word == secret_word:
            print('Congrats you won using',attempts,'attempt(s)')
            break
        attempts += 1
        if attempts > N:
            print('You already used #'+str(N),'attempts. Better luck tomorrow!')
        else:
            print('Enter your attempt #' + str(attempts))
            player_word = enter_and_check('player', words_list)
