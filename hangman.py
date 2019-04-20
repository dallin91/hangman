# This is a simple hangman game
# Created by Dallin Reeves
# April 9, 2019 1:36 PM

answer = ''

def display_board(board):
    '''
    This function is to prepare the playing board for hangman
    '''

    print('______________________')
    print('|                     |')
    print('|                     |')
    print('|                    ' + board[1])
    print('|                    ' + board[2])
    print('|                    ' + board[3])
    print('|                   ' + board[4] + ' ' + board[5] + ' ' + board[6])
    print('|                    ' + board[7])
    print('|                   ' + board[8] + ' ' + board[9])
    print('|')
    print('|')
    print('|')

def random_string():
    import random
    import requests

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    answer = random.choice(WORDS)
    anslen = int(len(answer))

    return '_' * anslen

random_string()