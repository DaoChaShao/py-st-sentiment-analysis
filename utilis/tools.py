#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from json import load
from os import path, listdir
from re import sub, search
from time import perf_counter

from random import seed
from numpy import random
from torch import manual_seed, cuda, backends, initial_seed


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


def tokenizer(file_path: str, normalization: str = "utilis/contraction.json") -> list[str]:
    """ Tokenize the text by removing special characters and lowercasing the text

    :param file_path: str, the file path to be tokenized
    :param normalization: str, the file path to the normalization file
    :return: list[str], the list of words
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        text = file.read()

    with open(normalization, "r", encoding="UTF-8") as nor:
        contractions = load(nor)

    for pattern, replacement in contractions.items():
        text = sub(pattern, replacement, text)

    pattern: str = r"[^A-Za-z0-9 ]+"
    cleaned = sub(pattern, "", text.lower())
    words = cleaned.split()
    return words


def labels_getter(file_path: str) -> tuple[int, int]:
    """ Get the position and label from the file path

    :param file_path: str, the file path to be processed
    """
    match = search(r"(\d+)_(\d+)", file_path)
    return int(match.group(1)), int(match.group(2))


def paths_getter(root_file_path: str, category: str) -> list[str] | None:
    """ Get the file paths for the training and testing data

    :param root_file_path: str, the file path to the dataset
    :param category: str, the category of the data
    """
    if not path.exists(root_file_path):
        raise FileNotFoundError(f"{root_file_path} does not exist.")

    ignore: list = [".DS_Store", ".gitignore"]

    paths = []
    for file in listdir(root_file_path):
        if file not in ignore:
            sub_path = path.join("imdb/", file)
            if category == "train" and file.endswith("train"):
                for file_type in listdir(sub_path):
                    if file_type not in ignore:
                        type_path = path.join(sub_path, file_type)
                        paths.extend([path.join(type_path, data) for data in listdir(type_path) if data not in ignore])
            elif category == "test" and file.endswith("test"):
                for file_type in listdir(sub_path):
                    if file_type not in ignore:
                        type_path = path.join(sub_path, file_type)
                        paths.extend([path.join(type_path, data) for data in listdir(type_path) if data not in ignore])
    return paths


class SeedSetter(object):

    def __init__(self, randomness: int = 9527, description: str = None):
        """ Initialize the Seed class

        :param randomness: int, the random seed
        :param description: str, the description of the seed
        """
        self._randomness: int = randomness
        self._description: str = description

    def __enter__(self):
        """ Set the seed for the random number generators """
        seed(self._randomness)  # Set the Python random seed
        random.seed(self._randomness)  # Set the NumPy random seed
        manual_seed(self._randomness)  # Set the PyTorch CPU random seed

        backends.cudnn.deterministic = True  # Ensure the results are reproducible
        backends.cudnn.benchmark = False  # Ensure the results are reproducible; however, the performance may be slower

        if cuda.is_available():
            cuda.manual_seed(self._randomness)  # Set the PyTorch GPU random seed, single GPU
            cuda.manual_seed_all(self._randomness)  # Set the PyTorch GPU random seed, all GPUs
        print(f"The seed of {self._description} is IN.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Reset the seed for the random number generators """
        seed(None)  # Reset Python's random seed
        random.seed(None)  # Reset NumPy's random seed
        manual_seed(initial_seed())  # Reset PyTorch's seed

        backends.cudnn.deterministic = False  # Restore normal performance
        backends.cudnn.benchmark = True  # Allow optimization

        if cuda.is_available():
            cuda.manual_seed(initial_seed())  # Reset PyTorch GPU seed
            cuda.manual_seed_all(initial_seed())  # Reset PyTorch GPU seed for all GPUs

    def __repr__(self):
        return f"The seed of {self._description} is {self._randomness} and OUT."
