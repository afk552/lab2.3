#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    sent = str(input(
        "Введите одно предложение с одной или двумя запятыми "
        "или \"Example1\" / \"Example2\": \n"))
    if sent == "Example1":
        sent = "Тестовое предложение, слова после первой запятой, " \
               "слова после второй запятой."
        print(sent)
    elif sent == "Example2":
        sent = "Тестовое предложение, эти символы должны быть выведены."
        print(sent)
    amount = sent.count(',')
    if amount > 0:
        sentsplit = sent.split(',')
        pos1 = sent.find(',')
        if amount >= 2:
            pos2 = sent.find(',', sent.find(',') + 1)
            print(sent[pos1 + 1:pos2])
        else:
            print(sent[pos1 + 1:len(sent)])
    else:
        print(
            "В введенном предложении нет запятых!",
            file=sys.stderr
        )
        exit(1)