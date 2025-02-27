#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from os import path
from re import sub
from time import perf_counter


class Timer(object):
    """ A simple timer class to measure the elapsed time """

    def __init__(self, precision: int = 5, description: str = None):
        """ Initialize the Timer class with precision and description

        :param precision: the number of decimal places to round the elapsed time
        :param description: the description of the timer
        """
        self._precision: int = precision
        self._description: str = description
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        self._start = perf_counter()
        print(f"{self._description} started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        if self._elapsed is not None:
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        else:
            return f"{self._description} has not been started."


def tokenizer(text: str):
    """ Tokenize the text by removing special characters and lowercasing the text

    :param text: str, the text to be tokenized
    :return: str, the tokenized text
    """
    pattern: str = r"[^A-Za-z0-9 ]+"
    cleaned = sub(pattern, "", text.lower())
    words = cleaned.split()
    return words


def labels_getter() -> list:
    """ Get the labels from the labels.txt file

    :return: list, the list of labels
    """
    with open(path.join(path.dirname(__file__), "labels.txt"), "r") as file:
        labels = file.read().splitlines()
    return labels
