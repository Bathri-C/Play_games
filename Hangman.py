from data_games import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''




import random
print(logo)
word=random.choice(word_list)
word_length=len(word)
game_over=False
lives=6
display=[]
for _ in range(word_length):
    display+="_"

while not game_over:
    guess=input("Guess the letter : ").lower()
    if guess in display:
        print(f"you have already chosen the letter {display}")
    for position in range(word_length):
        letter=word[position]
        if letter==guess:
            display[position]=letter
    if guess not in word:
        print(f"your guess is incorrect and you lose one life.")
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose.")
    if "_" not in display:
        game_over=True
        print("You Win.")
    
    
    print(f"{' '.join(display)}")
    print(stages[lives])

print(f"The solution is {word}")
