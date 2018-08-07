from sys import argv

def main():
    if len(argv) != 3:
        usage()
        exit()
    
    fin_name = argv[1]
    fout_name = argv[2]

    if not fout_name.endswith('.sh'):
        fout_name += '.sh'
    
    out_lines = []

    with open(fin_name, 'r') as fin:
        for line in fin:
            if line.endswith('\n'):
                line = line[:-1]
            alias = line[:line.index(' ')]
            cmd = line[line.index(' ') + 1:]
            out_lines.append('git config --global {} "{}"'.format(alias, cmd))
    
    with open(fout_name, 'w') as fout:
        fout.write('\n'.join(out_lines))


def usage():
    usage_text = [
        'Usage: {} IN OUT',
        '',
        '\tIN    Name of config file to read from',
        '\tOUT   Name of .sh file to output to'
    ]
    print('\n'.join(usage_text))


if __name__ == '__main__':
    main()

