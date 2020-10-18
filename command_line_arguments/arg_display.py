import argparse
#call the ArgumentParser()
parser=argparse.ArgumentParser()
#add arguments to the parser
parser.add_argument('nums',nargs='+')
#retrieve the arguments into args object
args=parser.parse_args()
#display the arguments from the list: args.nums
for x in args.nums:
    print(x)
