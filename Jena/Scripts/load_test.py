from os import system
import argparse
import time

parser = argparse.ArgumentParser(description='BSBM TDB Data Loading Script')
parser.add_argument('-loc', '--location', help='Database directory', required=True)
parser.add_argument('-o', '--outputfile', help='Output file location', required=False)
parser.add_argument('input', help='Data file location')
args = parser.parse_args()

if not args.location or not args.input:
    parser.print_help()
    exit(1)

if __name__ == "__main__":
    start_time = time.time()
    system('tdb2_tdbloader -loc %s %s' % (args.location, args.input))
    end_time = time.time()
    load_time = end_time - start_time
    output = f'LOAD TIME:\n\tLoad start time = {start_time}\n\tLoad end time = {end_time}\n\tLoad time = {load_time}\n'
    print(output)

    if args.outputfile is not None:
        with open(args.outputfile, 'w+') as f:
            f.write(output)