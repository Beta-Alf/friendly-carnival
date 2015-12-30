#!/usr/bin/env python3
import random

from bot import Carnival_bot
from corpus import Corpus
# use a lil matrix for fast construction and (in our case) lookup

if __name__ == '__main__':
    random.seed()

    chat_corpus = Corpus('parsed_corpus.json')
    chat_bot = Carnival_bot(chat_corpus)
    chat_bot.connect('Insert Group Identifier here')
    chat_bot.chat()
