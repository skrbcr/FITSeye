import sys
from scripts.main import FITSeye
from scripts.file import FileDialog

def main():
    fe = FITSeye()
    args = sys.argv
    if len(args) == 2:
        try:
            FileDialog.openFile(args[1])
        except:
            print('Error: cannot open input file.', file=sys.stderr)
    fe.main()

main()

