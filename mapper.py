#!/usr/bin/python3

import sys

def main():
    for line in sys.stdin:
        _, _, key, _, value = line.strip().split(', ')
        map(key, value)


def map(key, value):
    emit(key, str(value))

def emit(key, value):
    sys.stdout.write('{}\t{}\n'.format(key, value))


if __name__ == '__main__':
    main()
