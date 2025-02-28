#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:18
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :
"""
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
"""

from random import randint

from utilis.database import IMDBDataset, IMDBDataLoader
from utilis.tools import paths_getter, tokenizer, Timer


def main() -> None:
    """ Main Function """
    DATASET_PATH: str = "imdb"
    CATEGORY: str = "train"

    paths: list[str] = paths_getter(DATASET_PATH, CATEGORY)
    index: int = randint(0, len(paths) - 1)
    text = tokenizer(paths[index])
    print(text)

    with Timer(2, "IMDB Dataset Processing") as timer:
        imdb = IMDBDataset(DATASET_PATH, CATEGORY)
        review, position, labels = imdb[index]
        # print(len(imdb))
        print(review)
        print(position)
        print(labels)
    print(timer)

    batch_size: int = 2
    with Timer(2, "IMDB DataLoader Processing") as timer:
        data_loader = IMDBDataLoader(imdb, batch_size)
        print(len(data_loader))
        for review, position, label in data_loader:
            print(len(review))
            print(len(position))
            print(label)
            break
    print(timer)


if __name__ == "__main__":
    main()
