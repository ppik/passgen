import argparse
import os
import random

import chardet

table = {ord(x): '' for x in ('|')}

def parse_args():
    """Create argument parser and parse command line arguments."""
    parser = argparse.ArgumentParser(description='A simple random word picker')
    parser.add_argument('-n', type=int, default=4,
                        help='number of random words to pick')
    parser.add_argument('-m', '--max', type=int,
                        help='maximum length of a word')

    return vars(parser.parse_args())

def main(n=None, max=None):
    data = []
    for fname in os.listdir('./data'):
        if fname.startswith('_'):
            continue

        # Read in first 100 bytes for detecting encoding
        with open(f'./data/{fname}', 'rb') as f:
            blob = f.read(100)
            encoding = chardet.detect(blob)['encoding']

        with open(f'./data/{fname}', encoding=encoding) as f:
            for line in f:
                # Strip whitespace
                w = line.strip()

                # Remove extra characters
                w = w.translate(table)

                # Skip long words if max length given
                if max is not None and len(w) > max:
                    continue

                data.append(w)

    sel = random.choices(data, k=n)

    print(' '.join(sel))

if __name__ == '__main__':
    # Parse arguments
    args = parse_args()

    main(**args)
