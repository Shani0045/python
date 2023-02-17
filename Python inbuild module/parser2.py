import argparse
parser=argparse.ArgumentParser()
parser.add_argument("n1",help="first_number",type=int)
parser.add_argument("n2",help="second number",type=int)
parser.add_argument("operation",help="operation perform")
args=parser.parse_args()
if args.operation=="+":
    result=args.n1+args.n2
    print(result)
elif args.operation=="-":
    print(args.n1-args.n2)
elif args.operation=="*":
    print(args.n1*args.n2)
elif args.operation=="/":
    print(args.n1/args.n2)
else:
    print("bad arguments ")
