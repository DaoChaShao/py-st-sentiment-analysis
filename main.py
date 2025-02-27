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

from utilis.tools import tokenizer

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


def main() -> None:
    """ Main Function """
    print(tokenizer(TEXT))


if __name__ == "__main__":
    main()
