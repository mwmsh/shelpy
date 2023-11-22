import sys
from shelpy.utils import try_convert


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
