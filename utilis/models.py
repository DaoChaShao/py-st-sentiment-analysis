#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/27 22:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv


class Opener(object):

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
