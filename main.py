from multiprocessing import Pool
import argparse
import math
from time import sleep


def square(x):
    return x**2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="main.py")
    parser.add_argument(
        '-value1',
        type=int,
        default=3,
        help="Provide an integer (default: 3)")
    parser.add_argument(
        '-value2',
        type=int,
        default=4,
        help="Provide an integer (default: 4)")
    args = parser.parse_args()
    with Pool() as p:
        list_squared = list(p.map(square, [args.value1, args.value2]))
    print(math.sqrt(list_squared[0] + list_squared[1]))
