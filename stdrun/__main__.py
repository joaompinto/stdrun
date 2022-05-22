import sys
from argparse import ArgumentParser
from stdrun import Run

RED = "\033[0;31m"
BOLD = "\033[1m"
RESET = "\033[0m"


def stdout_print(line):
    print(line)


def stderr_print(line):
    print(f"{BOLD}{RED}{line}{RESET}", file=sys.stderr)


def main():
    parser = ArgumentParser()
    parser.add_argument("command", nargs="+", help="command to be executed")
    args = parser.parse_args()
    process = Run(args.command, stdout_print, stderr_print, shell=True)
    exit_code = process.run()
    print(f"Exit code: {exit_code}")


if __name__ == "__main__":
    main()
