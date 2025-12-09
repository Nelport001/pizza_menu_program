from random import randint
def guessing_game():
    while True:
        numbers = randint(1, 30)
        question = input("Chose a number from 1 - 30: ")
        if question >= '30':
            print("invalid number, choose a number between 1-30")
            continue
        elif numbers == question:
            print("congrats you won!!!")
        else:
            print("sorry you lost!")
            print(f"The correct number is {numbers}")
        keep_playing = input("Would you like to play again? (yes/no): ")
        if keep_playing.lower() == 'yes':
            continue
        elif keep_playing.lower() == 'no':
            print("Thanks for playing!!!")
            break
guessing_game()
