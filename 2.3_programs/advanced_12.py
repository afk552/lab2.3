#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    option = str(input("Введите \"Ввести слова\" или \"Пример\": "))
    if option.lower() == "пример":
        words = ["Программа", "Непредвиденный", "Абвгд"]
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
    for item in words:
        word = item.lower()
        # Список повторяющихся букв
        repeat = []
        # Слово в список для проверки побуквенно
        word_lst = list(word)
        for i, item2 in enumerate(word):
            if word.count(word[i]) > 1:
                repeat.append(item2)
        if len(repeat) <= 0:
            print("Повторяющихся букв в этом слове нет!")
        else:
            # Вычитанием множеств избавляемся от повторяющихся букв
            print(''.join(set(word_lst) - set(repeat)))
