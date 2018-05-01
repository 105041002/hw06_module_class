# -*- coding: utf-8 -*-
from collections import Counter
import string


class count_word():
    def __init__(self, text):
        words = (word.strip(string.punctuation) for word in text.split())
        self.count = Counter(word for word in words if word)

    def __iter__(self):
        for word, count in self.count.most_common():
            yield word, count


# def count_word(text):
#     words = (word.strip(string.punctuation) for word in text.split())

#     # compute word count from all_words
#     return Counter(word for word in words if word).most_common()


if __name__ == '__main__':
    count_word("i_have_a_dream.txt")
