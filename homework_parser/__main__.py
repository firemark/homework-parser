from homework_parser.file_parser import detect_plugin

from sys import argv, stdin, stdout, stderr, exit
from argparse import ArgumentParser, FileType

parser = ArgumentParser(description='parse file/stdint and write to file/stdout')
parser.add_argument('in_format', help='plugin to load file/stdin')
parser.add_argument('out_format', help='plugin to write to file/stdout')

parser.add_argument(
    '--infile',
    nargs='?',
    type=FileType('r'),
    default=stdin,
    help='file to load data (optional)'
)
parser.add_argument(
    '--outfile',
    nargs='?',
    type=FileType('w'),
    default=stdout,
    help='file to save data (optional)'
)

if __name__ == "__main__":
    args = parser.parse_args()
    out_plugin = detect_plugin(args.out_format)

    if out_plugin is None:
        print >> stderr, ('out-plugin %s not found' % args.out_format)
        exit(-1)

    in_plugin = detect_plugin(args.in_format)
    if in_plugin is None:
        print >> stderr, ('in-plugin %s not found' % args.in_format)
        exit(-1)
     
    data = in_plugin.read_from_file(args.infile)
    out_plugin.write_to_file(args.outfile, data)

