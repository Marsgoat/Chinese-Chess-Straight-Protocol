import argparse
from utils import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Chinese Chess Straight Protocol')
    parser.add_argument('--bin', type=str, required=True)

    args = parser.parse_args()

    print(binary_to_move(args.bin))
