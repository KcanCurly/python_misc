#! /usr/bin/env python

import argparse
import re
from sys import exit

def parse_lines(file, output):
    # Remove whitespaces from the beginning of each line
    # We put end="" on print because line also includes newline characters
    for line in file:
        print(re.sub(r"^\s+", r"", line), file=output, end="")

def main():
    # We prepare argument parser and add necessary arguments
    # inputfile - required, we will read lines from this file
    # output - optional, we will write lines to this file
    parser = argparse.ArgumentParser(
        prog="remove_spaces",
        description="Remove whitespaces from list of strings in given file",
        epilog="Hope you enjoy"
    )
    
    parser.add_argument("inputfile")
    parser.add_argument("-o","--output", required=False)
    args = parser.parse_args()
    
    # We will add this extension to the output file if it is not specified
    default_file_extension = "_rm_whitespace"
    
    # We open both input and output file (create if it doesn't exist)
    # Exceptions are caught
    # If everything goes well we call the parse_lines function
    try:
        with( 
            open(args.inputfile, mode="r") as f,
            open(args.output or args.inputfile + default_file_extension, mode="w+") as t
        ):
            parse_lines(f, t)
    except FileNotFoundError:
        parser.print_usage()
        exit("\nFile not found.")
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()