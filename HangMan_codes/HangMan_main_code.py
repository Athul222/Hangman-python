#taking random words and checking

import random 
from HangMan_codes import HangMan_words
from HangMan_codes import HangMan_stages
# from replit import clear()


print("---Welcome to HungMan-----")
print(HangMan_stages.logo)
choosen_word = random.choice(HangMan_words.word_list).lower()
print(choosen_word)
display = []
for _ in range(len(choosen_word)):
    display += "_"
print(display)
Lives = 6 

not_there = []
#for i in range(len(choosen_word)):
end_of_game = False
while not end_of_game:
    user_input = input("Enter the letter: ").lower()
    
    #telling the user the word is already entered
    if user_input in display:
        print("The word {} is already entered.".format(user_input))     
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_input:
            display[position] = letter
    #Joining all the elements in the list and turn it into string
    print(f"{''.join(display)}")
    if user_input not in choosen_word:
        not_there += user_input
        print(f"The letter {user_input} is not in word: ",not_there)
        Lives -= 1 
        if Lives == 0:
            end_of_game = True
            print("You died.") 
    print(f"Left out  lives: {Lives}")
    if '_' not in display:
        end_of_game = True
        print("You won the game")
    
    #Printing the stages live[6] = same as stage[6] so
    print(HangMan_stages.stages[Lives])


    
        
        

