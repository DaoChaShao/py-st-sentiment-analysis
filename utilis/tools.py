#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from os import path, listdir
from re import sub, search
from time import perf_counter
from torch.utils.data import Dataset, DataLoader


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


def tokenizer(file_path: str) -> list[str]:
    """ Tokenize the text by removing special characters and lowercasing the text

    :param file_path: str, the file path to be tokenized
    :return: list[str], the list of words
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        text = file.read()

    pattern: str = r"[^A-Za-z0-9 ]+"
    cleaned = sub(pattern, "", text.lower())
    words = cleaned.split()
    return words


TEXT: str = ("Once again Mr. Costner has dragged out a movie for far longer than necessary. "
             "Aside from the terrific sea rescue sequences, "
             "of which there are very few I just did not care about any of the characters. "
             "Most of us have ghosts in the closet, and Costner's character are realized early on, "
             "and then forgotten until much later, "
             "by which time I did not care. The character we should really care about is a very cocky, "
             "overconfident Ashton Kutcher. "
             "The problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a cluttered closet. "
             "His only obstacle appears to be winning over Costner. "
             "Finally when we are well past the half way point of this stinker, "
             "Costner tells us all about Kutcher's ghosts. "
             "We are told why Kutcher is driven to be the best with no prior inkling or foreshadowing. "
             "No magic here, it was all I could do to keep from turning it off an hour in.")


def labels_getter(file_path: str) -> tuple[int, int]:
    """ Get the position and label from the file path

    :param file_path: str, the file path to be processed
    """
    match = search(r"(\d+)_(\d+)", file_path)
    return int(match.group(1)), int(match.group(2))


class IMDBDataset(Dataset):
    """ The IMDB Dataset Class """

    def __init__(self, file_path: str) -> None:
        """ Initialize the IMDB Dataset Class

        :param file_path: str, the file path to the dataset
        """
        self._file_path: str = file_path
        self._train: list = []
        self._test: list = []
        self._train_paths: list = []
        self._test_paths: list = []
        self._ignore: list = [".DS_Store", ".gitignore"]

    def path_getter(self, category: str = "train") -> None:
        """ Get the file paths for the training and testing data

        :param category: str, the category of the data
        """
        if path.exists(self._file_path):
            imdb: list = [path.join("imdb/", file) for file in listdir(self._file_path) if file not in self._ignore]
            # print(imdb)

            for file in imdb:
                if file.endswith("train"):
                    self._train = [path.join(file, group) for group in listdir(file) if group not in self._ignore]
                    # print(f"Training Data: {self._train}")
                elif file.endswith("test"):
                    self._test = [path.join(file, group) for group in listdir(file) if group not in self._ignore]
                    # print(f"Testing Data: {self._test}")

            match category:
                case "train":
                    for file in self._train:
                        self._train_paths.extend(
                            [path.join(file, data) for data in listdir(file) if data not in self._ignore])
                    # print(f"The length of Training Paths: {len(self._train_paths)}")
                    # print(f"The example of Training Paths: {self._train_paths[:3]}")
                case "test":
                    for file in self._test:
                        self._test_paths.extend(
                            [path.join(file, data) for data in listdir(file) if data not in self._ignore])
                    # print(f"The length of Testing Paths: {len(self._test_paths)}")
                    # print(f"The example of Testing Paths: {self._test_paths[:3]}")
        else:
            raise FileNotFoundError(f"{self._file_path} does not exist.")

    def __len__(self):
        """ Get the length of the dataset """
        return len(self._train_paths) + len(self._test_paths)

    def __getitem__(self, index: int, category: str = "train") -> tuple[list[str], int, int] | None:
        """ Get the item of the dataset

        :param index: int, the index of the dataset
        :param category: str, the category of the data
        :return: tuple[list[str], int, int], the words, position, and label
        """
        match category:
            case "train":
                file_path: str = self._train_paths[index]
                words: list[str] = tokenizer(file_path)
                position, label = labels_getter(file_path)
                return words, position, label
            case "test":
                file_path: str = self._test[index]
                words: list[str] = tokenizer(file_path)
                position, label = labels_getter(file_path)
                return words, position, label

    def labels_checker(self) -> tuple[int, int, int]:
        """ Check the labels of the dataset """
        pos_labels: list[int] = [1, 2, 3, 4]
        neg_labels: list[int] = [7, 8, 9, 10]
        pos: list[int] = []
        neg: list[int] = []
        nan: list[int] = []

        for index in range(len(self)):
            _, _, label = self[index]
            if label in pos_labels:
                pos.append(label)
            elif label in neg_labels:
                neg.append(label)
            else:
                nan.append(label)
        return len(pos), len(neg), len(nan)

# def set_seed(seed: int = 42):
#     """ 设置 PyTorch 及相关库的随机种子，保证实验可复现 """
#     random.seed(seed)  # 设置 Python 内置 random 模块的随机种子
#     np.random.seed(seed)  # 设置 NumPy 的随机种子
#     torch.manual_seed(seed)  # 设置 PyTorch 的 CPU 随机种子
#     torch.cuda.manual_seed(seed)  # 设置 PyTorch 的 GPU 随机种子（单个 GPU）
#     torch.cuda.manual_seed_all(seed)  # 设置所有 GPU 的随机种子（多个 GPU）
#     torch.backends.cudnn.deterministic = True  # 确保每次卷积计算都是确定性的
#     torch.backends.cudnn.benchmark = False  # 可能会降低运行速度，但保证结果一致
