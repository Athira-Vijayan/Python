#python program to add two numbers using arguments parser
import argparse
#creating argument parser class objects
parser=argparse.ArgumentParser(description='sum of two numbers')
#add two arguments with names n1 and n2 and type as float
parser.add_argument('n1',type=float,help='Input first number')
parser.add_argument('n2',type=float,help='Input second number')
#retrieve arguments passed to the program
args=parser.parse_args()
result=float(args.n1)+float(args.n2)
print('sum of two=',result)
