#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = "прроцесор"
    print(a)
    a = a.replace("р", "", 1)
    a = list(a)
    a.insert(-2, 'с')
    print(''.join(a))

    b = "теекстовыйфайл"
    print(b)
    b = b.replace("е", "", 1)
    b = list(b)
    b.insert(-4, ' ')
    print(''.join(b))

    c = "програма и аллгоритм"
    print(c)
    c = c.replace("л", "", 1)
    c = list(c)
    c.insert(6, 'м')
    print(''.join(c))

    d = "процесор и паммять"
    print(d)
    d = d.replace("м", "", 1)
    print(d)
    d = list(d)
    d.insert(6, 'с')
    print(''.join(d))
