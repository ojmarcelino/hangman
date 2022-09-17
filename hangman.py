import os
import random
import sys

class Hangman:
    game_header = 'Shall we play Hangman? I dare you.'
    words = []
    challenge_word = ''
    filled_word = []
    input_characters = []
    attempt_count = 0
    hangman_length = 8
    hangman_array = \
        ['    --',
         '    | ',
         '    O ',
         '    | ',
         '   \\|/',
         '    | ',
         '    | ',
         '   / \\']
    hangman_stick = \
        ['--|  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '__|__']

    def __init__(self, filename='cars.txt'):
        try:
            with open(filename, 'r') as f:
                self.words = [x.strip() for x in f.readlines()]
        except IOError as e:
            print('Error:', e)
            print('Initiating default list - Volkswagen, Toyota, Ford')
            self.words = ['Volkswagen', 'Toyota', 'Ford']

    def pick_next_word(self):
        self.challenge_word = random.choice(self.words)

    def initiate_blanks(self):
        self.filled_word = []
        self.input_characters = []
        self.attempt_count = 0
        for x in self.challenge_word:
            self.filled_word.append('_' if x != ' ' else ' ')

        print(self.game_header)
        print('\nInput characters \nJust waiting your letter')
        print('\nGuess the car brand (from the top 50 worldwide)\n', *self.filled_word,'\n')
        self.draw_hangman()

    def update_hangman(self, input_character):
        self.attempt_count += 1
        all_blanks_filled = False
        print(self.game_header)
        self.input_characters.append(input_character)
        print('\nInput characters \n', *self.input_characters)
        if input_character.upper() in self.challenge_word.upper():
            i = 0
            for x in self.challenge_word:
                if x.upper() == input_character.upper():
                    self.filled_word[i] = x
                i += 1
            print('Guess the car brand -\n', *self.filled_word,'\n')
            if '_' not in self.filled_word:
                all_blanks_filled = True
        else:
            print('Guess the car brand -\n', *self.filled_word)
        if self.attempt_count <= self.hangman_length:
            self.draw_hangman()
            if self.attempt_count == self.hangman_length:
                print('Too bad, you died, the brand was ', self.challenge_word)
                return '1'
        else:
            print('Too bad, you died, the brand was ', self.challenge_word)
            return '1'
        if all_blanks_filled:
            print('So far, so good, you live')
            return '1'
        else:
            return input_character

    def draw_hangman(self):
        i = 0
        for x in self.hangman_stick:
            if i < self.attempt_count:
                print(self.hangman_array[i], x)
            else:
                print('      ', x)
            i += 1

    def play_hangman(self):
        self.pick_next_word()
        self.initiate_blanks()
        input_char = ''
        while input_char != '1':
            input_char = input('\nPick a character\nPress 1 if you want to quit\nPress 2 to change the brand\n')
            if input_char == '1':
                pass
            elif input_char == '2':
                os.system('clear')
                self.pick_next_word()
                self.initiate_blanks()
            elif input_char.isalpha() and len(input_char) == 1:
                os.system('clear')
                input_char = self.update_hangman(input_char)
            else:
                print('Please only enter alphabet')

if __name__ == '__main__':
    try:
        hangman = Hangman(sys.argv[1])
    except IndexError as e:
        os.system('clear')
        hangman = Hangman()
    hangman.play_hangman()