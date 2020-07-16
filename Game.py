from hangman_words import word_list
import random as ran
from BrainInfo import Brain

class Game:

    def __init__(self):
        self.brain = Brain()
        self.game_board = self.game_board()
        self.guess_index = []
        print(f"Your word is {self.game_board}{self.brain.word_length} letters long")
        self.allowed_guesses = 10
        self.game_play()
        self.play_again()

    def game_board(self):
        board = "_" * self.brain.word_length
        return list(board)

    def guess(self):
        user_guess = input("Please guess a letter?\n").upper()
        if user_guess in self.guess_index:
            self.allowed_guesses -= 1
            print(f"You have already guessed that letter, you have {self.allowed_guesses} guesses remaining\n")
        elif len(user_guess) > 1 or user_guess.isnumeric():
            self.allowed_guesses -= 1
            print(f"Please enter a SINGLE LETTER guess\n, you have {self.allowed_guesses} guesses remaining\n")
        elif user_guess not in self.guess_index:
            self.guess_index.append(user_guess)

            if user_guess in self.brain._random_word:
                check = self.brain.letter_check(user_guess)
                print(f"Your guesses so far {self.guess_index}")
                for i in check:
                    self.game_board[i] = user_guess
                print(f"Your correct letters {''.join(self.game_board)}")
            elif user_guess not in self.brain._random_word:
                self.allowed_guesses -= 1
                print(f"Incorrect guess, you have {self.allowed_guesses} guesses remaining")
                print(f"So far you have guessed the letters {self.guess_index}")

    def game_play(self):
        while self.allowed_guesses > 0:
            self.guess()
            if self.allowed_guesses == 0:
                print(f"Game Over you lost {self.brain.name}, the correct answer was {self.brain._random_word}")
                self.play_again()
            elif self.allowed_guesses > 0 and "_" not in self.game_board:
                print(f"Well Done {self.brain.name} you win")
                self.play_again()

    def play_again(self):
        play_again = input(print("Would you like to play again? Y/N\n")).upper()
        while play_again != "Y" and play_again != "N":
            play_again = input("Please enter Y(Yes) or N(no)\n").upper()
        if play_again == "Y":
            Game()
        elif play_again == "N":
            quit(Game)




