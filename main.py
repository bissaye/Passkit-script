import sys
import getopt
from Tools import *

if __name__ == '__main__':
    # control
    aide = False

    options, args = getopt.getopt(
        sys.argv[1:],
        "h",
        [
            "help",
        ]
    )

    for option, arg in options:
        if option in ("-h", "--help"):
            aide = True


    if aide:
        help()