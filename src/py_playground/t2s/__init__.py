import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser(prog='py_playground.t2s')
    parser.add_argument("path", help="The path files need translation live.")
    parser.add_argument("-s", "--suffixes", nargs="*",
                        help="Target suffixes of files that need to be processed. Process all files by default.")
    return parser
