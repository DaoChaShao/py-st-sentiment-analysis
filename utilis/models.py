#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from torch import nn


class Opener(object):
    """ The OpenAI API Class """

    def __init__(self, temperature: float = 0.7, top_p: float = 0.9) -> None:
        """ Initialize the OpenAI API

        :param temperature: float, default=0.7
        :param top_p: float, default=0.9
        """
        load_dotenv(find_dotenv())
        self._temperature = temperature
        self._top_p = top_p
        # self._api_key = load_dotenv(".env")["API_KEY"]

    def client(self, content: str, prompt: str, model: str) -> str:
        """ Initialize the OpenAI API Client

        :param content: str, the content to be generated
        :param prompt: str, the prompt to be used
        :param model: str, the model to be used
        :return: str, the generated content
        """
        # client = OpenAI(api_key=self._config["API_KEY"], base_url="https://api.openai.com/v1")
        # print(len(config["API_KEY"]))  # 164-digit key
        client = OpenAI(base_url="https://api.openai.com/v1")

        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": prompt},
        ]

        completion = client.chat.completions.create(
            model=model,
            store=False,
            messages=messages,
            stream=False,
            temperature=self._temperature,
            top_p=self._top_p,
        )
        return completion.choices[0].message.content


class IMDBEmbedding(nn.Module):
    """ The IMDB Embedding Class """

    def __init__(self, dictionary, max_len: int, dimensions: int = 256, division: int = 2) -> None:
        """ Initialize the IMDB Embedding Class

        :param dictionary: the dictionary of the dataset
        :param max_len: the maximum length of the dataset
        :param dimensions: the dimensions of the dataset
        :param division: the division of the dataset
        """
        super().__init__()
        self._embedding = nn.Embedding(
            num_embeddings=len(dictionary),
            embedding_dim=dimensions,
            padding_idx=dictionary.TAG_PAD,
        )

        self.fc = nn.Linear(max_len * dimensions, division)

    def forward(self, x):
        """ Forward the input through the network

        :param x: the input x: [batch_size, max_len, dimensions]
        :return: the output of the network
        """
        x = self._embedding(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return nn.functional.log_softmax(x, dim=-1)


def trainer():
    pass


def tester():
    pass
