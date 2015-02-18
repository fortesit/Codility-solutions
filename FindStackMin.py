#!/usr/bin/env python

data = []
aux = []
minimum = 999999

def push(e):
    global data
    global aux
    global minimum

    data.append(e)
    if e < minimum:
        aux.append(e)
        minimum = e
    else:
        aux.append(minimum)
    return

def pop():
    global data
    global aux
    global minimum

    data.pop()
    aux.pop()
    minimum = aux[-1]
    
    return

def min():
    global aux
    return aux[-1]

