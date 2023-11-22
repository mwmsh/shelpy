import sys


def try_convert(arg, arg_type, err_msg):
    try:
        return arg_type(arg)
    except ValueError:
        print(err_msg, file=sys.stderr)
        exit(1)
