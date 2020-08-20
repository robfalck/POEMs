#!/usr/bin/env python

import argparse
import re
import os
import io
import sys
from typing import Optional, Sequence

PASS = 0
FAIL = 1

re_poem = re.compile(r'POEM_(\d{1,3})\.md')


def parse_poem(file):
    entries = {}
    entries['status'] = 'active'

    with open(file, 'r') as poem:
        lines = poem.readlines()

    for line in lines:
        lu = line.upper()
        if lu.startswith('POEM ID:'):
            entries['id'] = line.split(':')[-1].strip()
            # print('found id', file=sys.stderr)
        elif lu.startswith('TITLE:'):
            entries['title'] = line.split(':')[-1].strip()
            # print('found title', file=sys.stderr)
        elif lu.startswith('AUTHORS:') or lu.startswith('AUTHOR:'):
            entries['authors'] = line.split(':')[-1].strip()
            # print('found authors', file=sys.stderr)
        else:
            pass
            # print('found nothing', file=sys.stderr)

        if lu.startswith('- [X] ACTIVE'):
            entries['status'] = 'active'
        if lu.startswith('- [X] REQUESTING DECISION'):
            entries['status'] = 'requesting decision'
        if lu.startswith('- [X] ACCEPTED'):
            entries['status'] = 'accepted'
        if lu.startswith('- [X] REJECTED'):
            entries['status'] = 'rejected'
        if lu.startswith('- [X] INTEGRATED'):
            entries['status'] = 'integrated'

    return entries


def build_poem_table():
    table_dict = {}
    table = io.StringIO()

    # Collect the information

    for file in os.listdir(os.getcwd()):
        match = re_poem.match(file)
        if match:
            id_str = int(match.groups()[0])
            table_dict[id_str] = parse_poem(file)

    # Write the table

    print('| POEM ID | Title | Author | Status |', file=table)
    print('| ------- | ----- | ------ | ------ |', file=table)

    for id in sorted(table_dict.keys()):
        entries = table_dict[id]
        print(id)
        print(f"| {id:03} | {entries['title']} | {entries['authors']} | {entries['status']} |",
              file=table)

    return table.getvalue()


def update_readme():
    try:
        with open('README.md', 'r') as readme:
            lines = readme.readlines()
    except IOError:
        return 1

    table = build_poem_table()

    try:
        with open('README.md', 'w') as readme:
            for line in lines:
                print(line, file=readme, end='')
                if line.startswith('## List of POEMs'):
                    print('', file=readme)
                    break
            print(table, file=readme)
    except IOError:
        return 1
    return 0


def validate_poems(files):
    retval = PASS
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
        for i in range(6):
            if not lines[i].endswith('  \n'):
                print(
                    'Error: Each line in the header must end with two spaces for proper formatting.')
                retval = FAIL
    return retval


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retval = validate_poems(args.filenames)
    retval = update_readme() | retval

    return retval


if __name__ == '__main__':
    print('updating README.md')
    exit(main())
