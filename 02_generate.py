# -*- coding: utf-8 -*-
from GenerateText import GenerateText

def generate_tweet():
    generator = GenerateText()
    print(generator.generate())

if __name__ == '__main__':
    generate_tweet()
