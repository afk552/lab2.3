#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    sent = str(input(
        "Введите одно предложение с \"нн\" или \"Example\" \n"))
    if sent == "Example":
        sent = 'Запомните представленные исключения: '\
                'стеклянный, оловянный, деревянный!'
        print(sent)
    if len(sent.split()) < 2:
        print(
            "Предложение не может состоять из одного слова!",
            file=sys.stderr
        )
        exit(1)
    amount = sent.count('нн') + sent.count('НН')
    comb = ['нн', 'НН']
    print(amount, "вхождений \"нн\" было найдено в предложении!")
    sentsplit = sent.split()
    if amount > 0:
        print("Вхождения были найдены в следующих словах: ")
        for word in sentsplit:
            if comb[0] in word:
                print(word)
            elif comb[1] in word:
                print(word)
