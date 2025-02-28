#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/3/1 00:39
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :   

from torch.utils.data import Dataset, DataLoader

from utilis.tools import paths_getter, tokenizer, labels_getter


class IMDBDataset(Dataset):
    """ The IMDB Dataset Class """

    def __init__(self, file_path: str, category: str = "train") -> None:
        super().__init__()
        """ Initialize the IMDB Dataset Class

        :param file_path: str, the file path to the dataset
        """
        self._file_path: str = file_path
        self._category: str = category
        self._paths: list = paths_getter(self._file_path, self._category)

    def __len__(self):
        """ Get the length of the dataset """
        return len(self._paths)

    def __getitem__(self, index: int, category: str = "train") -> tuple[list[str], int, int] | None:
        """ Get the item of the dataset

        :param index: int, the index of the dataset
        :param category: str, the category of the data
        :return: tuple[list[str], int, int], the words, position, and label
        """
        file_path: str = self._paths[index]
        words: list[str] = tokenizer(file_path)
        position, label = labels_getter(file_path)
        label = 0 if label < 5 else 1
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


class IMDBDataLoader(DataLoader):
    """ The IMDB Data Loader Class """

    def __init__(self, dataset, batch: int, shuffle: bool = True) -> None:
        """ Initialize the IMDB Data Loader Class

        :param dataset: Dataset, the dataset to be loaded
        :param batch: int, the batch size
        :param shuffle: bool, the shuffle flag
        """
        super().__init__(
            dataset=dataset,
            batch_size=batch,
            shuffle=shuffle,
            collate_fn=self.collate_fn
        )

    @staticmethod
    def collate_fn(batch) -> tuple[list[list[str]], list[int], list[int]]:
        """ Collate the batch size

        :param batch: list, the batch size
        :return: tuple[list[list[str]], list[int], list[int]], the comments, positions, and labels
        """
        comments, positions, labels = zip(*batch)
        return comments, positions, labels
