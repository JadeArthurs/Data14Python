
from input_trial import take_input
from io import StringIO


from scrabble_word import PlayScrabble
test_scrabble = PlayScrabble()

def test_correct_number():
    assert len(test_scrabble.user_letters) == 7

def test_letter():
    assert "a" in test_scrabble.score.keys()
    assert "d" in test_scrabble.score.keys()
    assert "f" in test_scrabble.score.keys()
    assert "k" in test_scrabble.score.keys()
    assert "b" in test_scrabble.score.keys()

# def number_letters():
#     assert test_scrabble.number("k") <= 1
#     assert test_scrabble.number("b") <= 2
#     assert test_scrabble.number("g") <= 3
#     assert test_scrabble.number("d") <= 4
#     assert test_scrabble.number("n") <= 6
#     assert test_scrabble.number("o") <= 8
#     assert test_scrabble.number("a") <= 9
#     assert test_scrabble.number("e") <= 12
#


def test_word(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("cactus"))
    assert test_scrabble.score_calculator() == 10




# def valid_word():
#     assert test_scrabble.word in test_scrabble.user_letters
#     assert for i in word:
#         (test_scrabble.word).count(i) <= test_scrabble.number













