import random


class PlayScrabble:

    def __init__(self):
        print("Welcome to Scrabble")
        self.score = {
         "a": 1, "b": 3, "c": 3, "d": 2,
         "e": 1, "f": 4, "g": 2, "h": 4,
         "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3,
         "q": 10, "r": 1, "s": 1, "t": 1,
         "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10
    }
        # self.number = {
        #  "a": 9, "b": 2, "c": 2, "d": 4,
        #  "e": 12, "f": 2, "g": 3, "h": 2,
        #  "i": 9, "j": 1, "k": 1, "l": 4,
        #  "m": 2, "n": 6, "o": 8, "p": 2,
        #  "q": 1, "r": 6, "s": 4, "t": 6,
        #  "u": 4, "v": 2, "w": 2, "x": 1,
        #  "y": 2, "z": 1
    # }
        self.alphabet = (
            "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z"
        )

        self.num_letters = 0
        self.user_letters = []
        self.pick_letters()
        self.user_word = self.user_word()
        self.score_calculator()
        # self.play_again()


    def pick_letters(self):
        while self.num_letters < 7:
            letter = random.choice(self.alphabet)
            self.user_letters.append(letter)
            self.num_letters += 1
        print(self.user_letters)


    def user_word(self):
        self.user_word = input("Please enter your scrabble word").lower()
        for letter in self.user_word:
            if letter not in self.user_letters:
                print("you do not have all those letters")
            else:
                self.user_letters.remove(letter)
                self.num_letters -= 1
                self.pick_letters()
        return self.user_word

    def score_calculator(self):
        total_score = 0
        for i in self.user_word:
            total_score += self.score[i]
        print(total_score)

    # def play_again(self):
    #     play_again = input(print("Would you like to play again? Y/N\n")).upper()
    #     while play_again != "Y" and play_again != "N":
    #         play_again = input("Please enter Y(Yes) or N(no)\n").upper()
    #     if play_again == "Y":
    #         PlayScrabble()
    #     elif play_again == "N":
    #         quit(PlayScrabble)


    

game = PlayScrabble()
