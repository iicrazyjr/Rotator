#!/usr/bin/python3

import argparse
import sys

def rot(message, key):
    result = []
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base + key) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(
        prog="{}".format(sys.argv[0]),
        description="Rotate any text file and string using caesar cipher",
        formatter_class=argparse.HelpFormatter,
        exit_on_error=True,
        add_help=True
    )

    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help="text file to rotate")
    parser.add_argument('-s', '--string', type=str, help="string to rotate")
    parser.add_argument('-k', '--key', type=int, default=13, help='number of rotations (default: %(default)s)')
    parser.add_argument('-o', '--output', type=str, help='filename output (includes .rot extension)')
    args = parser.parse_args()

    if not args.file and not args.string or args.file and args.string:
        parser.error("Give me a filename or a string (:")

    # Give me data
    if args.file:
        data = args.file.read()
        args.file.close()
    else:
        data = args.string
    rotated_data = rot(data, args.key)

    if args.string and not args.output:
        print(rotated_data)
        sys.exit(0)

    if args.file and not args.output:
        print(rotated_data)
        sys.exit(0)

    if args.output:
        filename = args.output+'.rot'
        with open(filename, 'w') as f:
            f.write(rotated_data)
            f.write('\n')
        print(f'Data rotated on {filename}')


if __name__ == '__main__':
    main()

