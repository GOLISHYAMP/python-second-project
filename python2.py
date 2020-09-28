from word import word_list
import random

def getRandom():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    print("LETS PLAY HANGMAN GAME !")
    guessed = False
    guessed_letter = []
    guessed_word = []
    tries = 6
    word_completion = "-"*len(word)
    print(word_completion) 

    while not guessed and tries > 0 :
        print(displayhangman(tries))

        guess = input("enter your guess: ").upper()
        if len(guess)==1 :
           
            if guess in guessed_letter :
               print("already used this letter "+ guess)
            elif guess not in word :
                print("ooo! you missed, go for another")
                guessed_letter.append(guess)
                tries -= 1 
            else :
                print("Good! go head")    
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i , letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:

                    guessed = True
                        
                     

        elif len(guess)==len(word) and guess.isalpha() :

            if guess in guessed_word :
                print(guess," is already guessed")

            elif guess != word:
                print(guess," is not a word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word

        else :
            print("invalid word")

        print(word_completion) 
        if guessed :
            print("congratulations you have won!")
        if tries == 0 :
            print("Sorry! you ran out tries,the word is ",word," try again!")
            print(displayhangman(tries))           

def displayhangman(tries) :
    stages = [
        """

                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\


        """,
        """

                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 


        """,
        """

                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     


        """,
        """

                --------
                |      |
                |      O
                |     \\|/
                |      
                |     


        """,
        """

                --------
                |      |
                |      O
                |      |
                |      
                |     


        """,
        """

                --------
                |      |
                |      
                |     
                |      
                |     


        """,
        """

                --------
                |      
                |      
                |     
                |      
                |     


        """]
    return stages[tries]    

    

               


def main():
    word = getRandom()
    play(word)

go = True
while go :
    main()
    choice = input("want to play again press \nY for yes \nN for no\n").upper()
    
    if choice == 'N' :
        go = False


    