import sys
from scripts.main import FITSeye

def main():
    args = sys.argv
    if len(args) == 1:
        fe = FITSeye()
    elif len(args) == 2:
        fe = FITSeye(args[1])
    else:
        print('Error: too much args.', file=sys.stderr)
        return
    fe.main()

main()

