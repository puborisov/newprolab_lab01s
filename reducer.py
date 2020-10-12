#!/usr/bin/python3

import sys

def main(): # Reducer

    prev_key = None
    values = []

    for line in sys.stdin:
        key, value = line.split('\t')
        if key != prev_key and prev_key is not None:
            reduced_key, reduced_value = reduce(prev_key, values)
            emit(reduced_key, str(reduced_value))
            values = []
        values.append(float(value))
        prev_key = key


def reduce(key, values):
    return key, sum(values)

def emit(key, value):
    sys.stdout.write('{}\t{}\n'.format(key, value))

if __name__ == '__main__':
    main()
