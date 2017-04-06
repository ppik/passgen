import os
import random

import chardet

table = {ord(x): '' for x in ('\n', '|')}

def main(n=5):
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
                w = line.translate(table)
                data.append(w)

    sel = (random.choice(data) for x in range(n))

    print(' '.join(sel))

if __name__ == '__main__':
    main()
