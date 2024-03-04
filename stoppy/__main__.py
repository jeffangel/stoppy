import sys

from stoppy.mybreak import MyBreak

def main(args=None):
    
    if args is None:
        args = sys.argv[1:]
    mybreak = MyBreak()
    mybreak.run()

if __name__ == "__main__":
    sys.exit(main())