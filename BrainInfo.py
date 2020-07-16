from hangman_words import word_list
import random as ran


class Brain:
    def __init__(self):
        self._random_word = ran.choice(word_list)
        self.word_length = self.word_length()
        self.name = input("What is your name?\n")
        print(f"Welcome to hangman {self.name}")


    def chose_word(self):
        return self._random_word

    def word_length(self):
        self.length = len(self._random_word)
        return int(self.length)

    def letter_check(self, guess):
        counter = 0
        index = []
        for letter in self._random_word:
            if guess == letter:
                index.append(counter)
            counter += 1
        return index
