"""Small CLI for the calculator package.

Usage examples:
  python -m calculator.cli add 1 2
  python -m calculator.cli div 10 2
"""

import argparse
from calculator import add, sub, mul, div


def main():
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="operation")
    parser.add_argument("a", type=float, help="first operand")
    parser.add_argument("b", type=float, help="second operand")
    args = parser.parse_args()

    ops = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }

    func = ops[args.operation]
    try:
        result = func(args.a, args.b)
    except Exception as e:
        parser.error(str(e))

    print(result)


if __name__ == "__main__":
    main()
