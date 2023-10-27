import random
import string

def hangman():
    
    comp_word = ["cat", "caar", "tee"]
    random_word = (random.choice(comp_word)).upper()
    alphabets = set(string.ascii_uppercase)
    lives = 10

    guessdone = ""
    
    while len(random_word)>0:
        mainword = ""
        
        for letter in random_word:
            if letter in guessdone:
                mainword += letter
            else:
                mainword += "_ "
    
        if random_word == mainword:
            print(mainword)
            print("won")
            break
   
        print("guess the word",mainword)

        guess = input("enter letter: ").upper()

        if guess in alphabets:
            guessdone += guess
        else:
            print("enter valid char: ")
            guess = input("enter letter: ").upper()
    
        if guess not in random_word:
            lives = lives - 1


hangman()



    


