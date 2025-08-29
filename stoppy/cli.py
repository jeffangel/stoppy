import sys

from stoppy.legacy import Automovement as Automovement_legacy
from stoppy.modern import Automovement as Automovement_modern

def main(args=None):
    
    if args is None:
        args = sys.argv[1:]

    if args[0] == "legacy":
        automovement = Automovement_legacy(
            absolute_ref=True
        )
    else:
        automovement = Automovement_modern()

    automovement.run()

if __name__ == "__main__":
    sys.exit(main())