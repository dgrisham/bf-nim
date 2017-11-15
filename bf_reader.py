#!/usr/bin/env python3

import re
import sys

def bf_reader(input):
    commands = ['>', '<', '+', '-', '.', ',', '[', ']']
    bf_code = []
    storage = []
    parens = False
    iter = enumerate(input)
    for i, c in iter:
        if c == '(':
            parens = True
        elif c == ')':
            parens = False
            next = input[i + 1]
            if next.isdigit():
                next = int(next)
            else:
                next = 1
            for j in range(next):
                for k, char in enumerate(storage):
                    bf_code.append(char)
            storage = []
            iter.next()
        elif parens:
            if c.isdigit():
                expand(storage, input[i - 1], int(c) - 1)
            else:
                storage.append(c)
        elif c in commands:
            bf_code.append(c)
        elif c.isdigit():
            expand(bf_code, input[i - 1], int(c) - 1)
        else:
            continue
    return bf_code


def expand(code, char, n):
    for i in range(n):
        code.append(char)


def import_bf(filename):
    file = open(filename, 'r')
    contents = []

    for line in file:
        line = line.rstrip()
        line = re.findall('\d+|\S', line)
        for c in line:
            contents.append(c)
        # contents = [i for list in contents for i in list]

    file.close()
    return contents


def output_bf_file(filename, code):
    file = open(filename, 'w')
    for item in code:
        file.write("%s" % item)


def main(argv):
    filename = argv[1]
    input = import_bf(filename + ".pybf")
    bf_code = bf_reader(input)
    output_bf_file(filename + ".bf", bf_code)

main(sys.argv)
