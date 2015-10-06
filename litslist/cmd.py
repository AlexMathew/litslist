"""
Usage:
    litslist (-h | --help | --version)
    litslist create <count>

Options:
    -h, --help
        Show this help message and exit
    --version
        Display the version of Scrapple
"""

from __future__ import print_function
from docopt import docopt

from . import commands

def runCLI():
    """
    CLI controller for litslist command
    """
    args = docopt(__doc__, version='0.1.0')
    try:
        commands.run_create(int(args['<count>']))
    except Exception as e:
        print('\n', e, '\n')


if __name__ == '__main__':
    runCLI()
