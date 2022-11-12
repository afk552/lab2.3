#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    option = str(input("Введите \"Ввести слова\" или \"Пример\": "))
    if option == "Пример" or option == "пример":
        words = ["Программа", "Непредвиденный", "Тттесссст"]
        print(' '.join(words))
    else:
        print("Введите три слова:")
        words = []
        for i in range(3):
            words.append(str(input()))
            if not (words[i].isalpha()):
                print(
                    "Слова не должны содержать цифр или пробелов!",
                    file=sys.stderr
                )
                exit(1)
    print("Неповторяющиеся буквы в словах: ")
    for z in range(3):
        word = words[z].lower()
        # Список повторяющихся букв
        repeat = []
        # Слово в список для проверки побуквенно
        word_lst = list(word)
        for i in range(len(word)):
            # Если в слове буква повторяется, заносим в список повторений
            if word.count(word[i]) > 1:
                repeat.append(word[i])
        if len(repeat) <= 0:
            print("Неповторяющихся букв в этом слове нет!")
        else:
            print(''.join(set(word_lst) - set(repeat)))
