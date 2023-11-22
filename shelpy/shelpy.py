import os
import sys

from shelpy.parse import parse_lambda, parse_int
from shelpy.validate import validate_arg_count


def hello_world():
    print("Hello from shelpy!")


def _range():
    usage = "Usage:\n$ range 1 5\n> " + "1\n  2\n  3\n  4"

    validate_arg_count(usage, [2, 3])

    args = [sys.argv[1], sys.argv[2]] if len(sys.argv) == 3 else ["0", sys.argv[1]]
    start, end = [parse_int(arg, "Argument " + arg + " is not an integer\n" + usage) for arg in args]

    for i in range(start, end):
        print(i, flush=True)


def _map():
    usage = "Usage:\n $ range 5 | map 'x -> x + 10'\n>10\n  11\n  12\n  13\n  14"

    validate_arg_count(usage, [2])
    func = parse_lambda(usage, sys.argv[1])

    for item in sys.stdin:
        print(func(item), flush=True)


def _filter():
    usage = "Usage:\n $ range 5 | filter 'x -> x > 0'\n> 1\n  2\n  3\n  4"

    validate_arg_count(usage, [2])
    func = parse_lambda(usage, sys.argv[1])

    for item in sys.stdin:
        item = item.removesuffix(os.linesep)
        if func(item):
            print(item, flush=True)
