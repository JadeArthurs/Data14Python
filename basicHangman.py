from hangman_words import word_list
import random as ran


class Brain:
    def __init__(self):
        self.random_word = ran.choice(word_list)
        self.word_length()

    def chose_word(self):
        return self.random_word

    def word_length(self):
        self.length = len(self.random_word)
        return int(self.length)

    def letter_check(self, guess):
        counter = 0
        index = []
        for letter in self.random_word:
            if guess == letter:
                index.append(counter)
            counter += 1
        return index

class Game:

    def __init__(self):
        self.brain = Brain()
        self.game_board = self.game_board()
        self.guess_index = []
        print(self.brain.random_word)
        self.allowed_guesses = 10
        self.game_play()


    def game_board(self):
        board = "_" * self.brain.word_length()
        return list(board)

    def guess(self):
        user_guess = input("Please guess a letter?\n").upper()
        if user_guess in self.brain.random_word:
            check = self.brain.letter_check(user_guess)
            self.guess_index.append(user_guess)
            print(self.guess_index)
            for i in check:
                self.game_board[i] = user_guess
            print(self.game_board)
        elif user_guess not in self.brain.random_word:
            print("That is not a correct guess")
            self.allowed_guesses -= 1

    def game_play(self):
        while self.allowed_guesses > 0:
            self.guess()
            if self.allowed_guesses == 0:
                print("Game Over you lost")
            elif self.allowed_guesses > 0 and "_" not in self.game_board:
                print("Well Done you win")
                break



hangman = Game()

