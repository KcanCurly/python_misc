#! /usr/bin/env python

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from sys import exit

def main():
    parser = ArgumentParser(
        prog="find_uniques",
        description="Find unique lines in a file and write to a new file",
        epilog= "Hope you enjoy\n \
        WARNING: Order of the given list is not preserved!",
        formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("inputfile")
    parser.add_argument("-o", "--output", required=False)
    args = parser.parse_args()
    
    default_file_extension = "_unique"
    try:

        with( 
            open(args.inputfile, mode="r") as f,
            open(args.output or args.inputfile + default_file_extension, mode="w+") as o
        ):
            uniques = set(map(str.rstrip, f))
            o.write("\n".join(uniques))
    except FileNotFoundError:
        parser.print_usage()
        exit("\nFile not found.")
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()