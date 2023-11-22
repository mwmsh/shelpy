import sys
import types


def parse_lambda(usage, arg):
    if not arg.startswith("lambda"):
        arg = "lambda " + arg
        arg = arg.replace("->", ":")
        try:
            f = eval(arg)
        except SyntaxError:
            print("Argument is not a lambda function: " + sys.argv[1] + "\n" + usage, file=sys.stderr)
            exit(1)

        if not isinstance(f, types.LambdaType):
            print("Argument is not a lambda function: " + sys.argv[1] + "\n" + usage, file=sys.stderr)
            exit(1)
    func = eval(arg)

    if not isinstance(func, types.LambdaType):
        print("Argument is not a lambda function: " + sys.argv[1] + "\n" + usage, file=sys.stderr)
        exit(1)

    return func


def parse_int(arg, err_msg):
    try:
        return int(arg)
    except ValueError:
        print(err_msg, file=sys.stderr)
        exit(1)
