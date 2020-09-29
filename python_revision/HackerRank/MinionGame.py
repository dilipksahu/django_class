'''
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .

Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings. 
Scoring
A player gets +1 point for each occurrence of the substring in the string .

Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
Sample Input
BANANA
Sample Output
Stuart 12
'''

def minion_game(string):
    vowels = "aeiou"
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i].lower() in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i

    if Kevin > Stuart:
        print("Kevin ",Kevin)
    elif Stuart > Kevin:
        print("Stuart ",Stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
