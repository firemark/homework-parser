from homework_parser.file_parser import detect_plugin

from sys import argv, stdin, stdout, stderr, exit

if __name__ == "__main__":
    in_format = argv[1]
    out_format = argv[2]
    out_plugin = detect_plugin(out_format)

    if out_plugin is None:
        print >> stderr, ('out-plugin %s not found' % out_format)
        exit(-1)

    in_plugin = detect_plugin(in_format)
    if in_plugin is None:
        print >> stderr, ('in-plugin %s not found' % in_format)
        exit(-1)
     
    if len(argv) == 4:
        with open(argv[3]) as f:
            data = in_plugin.read_from_file(f)
    else:
        data = in_plugin.read_from_file(stdin)
    
    out_plugin.write_to_file(stdout, data)
