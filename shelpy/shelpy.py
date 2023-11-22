import os
import sys

from shelpy.parse import parse_lambda
from shelpy.utils import try_convert
from shelpy.validate import validate_arg_count


def hello_world():
    print("Hello from shelpy!")


def _range():
    usage = "Usage:\n$ range 1 5\n> " + "1\n  2\n  3\n  4"
    args = len(sys.argv)
    if args not in [2, 3]:
        print("You provided " + str(args - 1) + " arguments. range accepts 1 or 2 arguments\n" + usage,
              file=sys.stderr, flush=True)
        exit(1)

    start = 0
    end = try_convert(sys.argv[1], int, "Argument " + sys.argv[1] + " is not an integer\n" + usage)
    if args == 3:
        start = end
        end = try_convert(sys.argv[2], int, "Argument " + sys.argv[2] + " is not an integer\n" + usage)

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
