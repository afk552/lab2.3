#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = "прроцесор"
    tmp = a
    a = a.replace("р", "", 1)
    a = list(a)
    a.insert(-2, 'с')
    print(tmp, ">>" ,''.join(a))

    b = "теекстовыйфайл"
    tmp = b
    b = b.replace("е", "", 1)
    b = list(b)
    b.insert(-4, ' ')
    print(tmp, ">>" ,''.join(b))

    c = "програма и аллгоритм"
    tmp = c
    c = c.replace("л", "", 1)
    c = list(c)
    c.insert(6, 'м')
    print(tmp, ">>" ,''.join(c))

    d = "процесор и паммять"
    tmp = d
    d = d.replace("м", "", 1)
    d = list(d)
    d.insert(6, 'с')
    print(tmp, ">>" ,''.join(d))
