# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, matches):
        word_arr = []
        return_arr = []
        for char in self.word:
            word_arr.append(char)

        for match in matches:
            match_arr = []
            for char in match:
                match_arr.append(char)

            if sorted(match_arr) == sorted(word_arr):
                return_arr.append(match)

        return return_arr