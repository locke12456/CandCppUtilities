import argparse , sys
from Creator.CFunction import CFunction
from Creator.GoogleTest import GoogleTest
from Creator.CHeader import CHeader
parser = None
def init(parser):
    parser = argparse.ArgumentParser(description='c function generator.')
    parser.add_argument('--test', action='store_true' , 
                       help='generate google test file')
    parser.add_argument('--header', 
                        type=str, default=str('foo.h'),
                        help='generate header file if the file is not exist , whitout insert one line to header')
    parser.add_argument('--func',required=True,
                       type=str, default=str('foo'),
                       help='function name')
    parser.add_argument('ret', metavar='ret',
                        type=str,  default=str('void'),
                        nargs=1,
                        help=' return type ' )
    parser.add_argument('args', metavar='args',
                        type=str,  default=str('void'),
                        nargs='+',
                        help=' function args ' )
    return parser
def usage(parser):
    parser.print_help()
def main(argv):
    parser = None
    parser = init(parser)
    try:
        args = parser.parse_args()
        header = CHeader(args.ret[0],args.func,args.args)
        header.generate(args.header)
        create = CFunction(args.ret[0],args.func,args.args)
        create.generate(args.header)
        test = GoogleTest(args.ret[0],args.func,args.args)
        test.generate(args.header)
    except:
        usage(parser)


    
if __name__ == "__main__":
    main(sys.argv[1:])