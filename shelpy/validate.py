import sys


def validate_arg_count(usage, allowed_arg_counts):
    arg_count = len(sys.argv)

    if arg_count in allowed_arg_counts:
        return

    required_args = " or ".join([str(s) for s in allowed_arg_counts]) + " argument" +\
                    ("s" if len(allowed_arg_counts) > 1 or allowed_arg_counts[0] > 1 else "")

    print("Command requires " + required_args + ". You provided " + str(arg_count) + "\n" + usage,
          file=sys.stderr, flush=True)
    exit(1)
