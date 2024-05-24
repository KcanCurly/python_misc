#! /usr/bin/env python

import argparse
from sys import exit

def main():
    parser = argparse.ArgumentParser(
        prog="separate_ip_port",
        description="Separates given ip:port format",
        epilog="Hope you enjoy"
    )
    parser.add_argument("input_file")
    parser.add_argument("-oI", "--output-ip-file", required=False)
    parser.add_argument("-oP", "--output-port-file", required=False)
    args = parser.parse_args()
    
    default_ip_file_name = "_ip"
    default_port_file_name = "_port"
    try:
        with(
            open(args.input_file, "r") as input,
            open(args.output_ip_file or args.input_file + default_ip_file_name, "w+") as output_ip,
            open(args.output_port_file or args.input_file + default_port_file_name, "w+") as output_port,
        ):
            for line in input:
                ip, port = line.split(":")
                output_ip.write(ip + "\n")
                output_port.write(port)
    except FileNotFoundError:
        parser.print_usage()
        exit("\nFile not found.")
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()