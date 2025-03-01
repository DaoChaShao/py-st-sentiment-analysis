#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/3/1 00:58
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   word2sequence.py
# @Desc     :

from torch import save, load as pt_load
from pickle import dump, load as pkl_load


class Word2Sequence(object):
    TAG_UNK: str = "<UNK>"
    TAG_PAD: str = "<PAD>"
    INDEX_UNK: int = 0
    INDEX_PAD: int = 1

    def __init__(self):
        self._dictionary = {
            self.TAG_UNK: self.INDEX_UNK,
            self.TAG_PAD: self.INDEX_PAD,
        }
        # Initialize the word frequency counter
        self._words_freq = {}
        # Initialize the reverse dictionary to convert the index to the word
        self._index_words = {}

    def __len__(self):
        return len(self._dictionary)

    def freq_count(self, words: list):
        for word in words:
            self._words_freq[word] = self._words_freq.get(word, 0) + 1

    def vocab_builder(self, freq_min: int = 1, freq_max: int = None, dictionary_size: int = None):
        """ Build the vocabulary of the reviews of the IMDB dataset

        :param freq_min: int, the minimum frequency of the word, normally ignore the words with frequency less than 1
        :param freq_max: int, the maximum frequency of the word, could use to ignore the words with high frequency
        :param dictionary_size: int, the maximum size of the dictionary
        """
        if freq_min is not None:
            self._words_freq = {word: freq for word, freq in self._words_freq.items() if freq >= freq_min}
        if freq_max is not None:
            self._words_freq = {word: freq for word, freq in self._words_freq.items() if freq <= freq_max}
        if dictionary_size is not None:
            self._words_freq = dict(sorted(
                self._words_freq.items(),
                key=lambda item: item[-1],
                reverse=True,
            )[:dictionary_size])

        # Build the dictionary to convert the word to the index
        self._dictionary.update({word: index + 2 for index, word in enumerate(self._words_freq.keys())})

        # Build the reverse dictionary to convert the index to the word
        self._index_words = {index: word for word, index in self._dictionary.items()}

    def transform(self, words: list, max_len: int) -> list[int]:
        """ Transform the words to the index

        :param words: list, the list of words
        :param max_len: int, the maximum length of the sentence
        :return: list, the list of index
        """
        # Get the index of the word if the word is in the dictionary, otherwise return the index of the unknown word
        return [self._dictionary.get(word, self.INDEX_UNK)
                for word in words[:max_len]] + [self.INDEX_PAD] * (max_len - len(words))

    def inverse_transform(self, indices: list) -> list:
        """ Transform the index to the words

        :param indices: list, the list of indices
        :return: list, the list of words
        """
        return [self._index_words.get(index, self.TAG_UNK) for index in indices]


def vocab_loader(file_path: str = "dictionaries/imdb.vocab", lines: int = 20) -> None:
    """ Load the vocabulary from the file

    :param file_path: str, the file path to the vocabulary
    :param lines: int, the number of lines to be displayed
    """
    with open(file_path, "r", encoding="utf-8") as vocab:
        for i, line in enumerate(vocab):
            if i < lines:
                print(line.strip())


def torch_dict_saver(dictionary, file_name: str = "torch") -> None:
    """ Save the dictionary to the file

    :param dictionary: dict, the dictionary to be saved
    :param file_name: str, the file path to the dictionary
    """
    save(dictionary, f"dictionaries/{file_name}.pt")


def torch_dict_loader(file_name: str = "torch") -> dict:
    """ Load the dictionary from the file

    :param file_name: str, the file path to the dictionary
    :return: dict, the dictionary
    """
    return pt_load(f"dictionaries/{file_name}.pt", weights_only=False)


def pickle_dict_saver(dictionary, file_name: str = "pickle"):
    """ Save the dictionary to the file

    :param dictionary: dict, the dictionary to be saved
    :param file_name: str, the file path to the dictionary
    """
    with open(f"dictionaries/{file_name}.pkl", "wb") as pkl:
        dump(dictionary, pkl)


def pickle_dict_loader(file_name: str = "pickle") -> dict:
    """ Load the dictionary from the file

    :param file_name: str, the file path to the dictionary
    :return: dict, the dictionary
    """
    with open(f"dictionaries/{file_name}.pkl", "rb") as pkl:
        return pkl_load(pkl)
