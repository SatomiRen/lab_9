#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print(dictionary)
    swapped = dict(map(reversed, dictionary.items()))
    print(swapped)
