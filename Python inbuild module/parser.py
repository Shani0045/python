import argparse
parser=argparse.ArgumentParser()
parser.add_argument("n1",help="first_number",type=int)
parser.add_argument("n2",help="second number",type=int)
parser.add_argument("operation",help="operation perform")
args=parser.parse_args()
print(args)  
print(args.n1)
print(args.n2)
print(args.operation)
