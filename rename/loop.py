#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
this is a rename script
i writh this script to rename my wallpaper
author is 8023
https://8023.moe
'''

import os
import sys
import getopt


def show_help():
    """
    show help function
    """
    print(help(__name__))


def rename(path, formatstr='%d', start=0, step=1):
    """
    rename function
    """
    con = start
    for filename in os.listdir(path):
        newfilename = (formatstr % con) + os.path.splitext(filename)[1]
        filename = os.path.join(path, filename)
        newfilename = os.path.join(path, newfilename)
        os.rename(filename, newfilename)
        # print(filename + ' -> ' + newfilename)
        con += step


def main():
    """
    main func
    """

    opts, args = getopt.getopt(
        sys.argv[1:],
        'hp:f:a:b:s:',
        ['help', 'path=', 'format=', 'start=', 'step=']
    )

    path = ''
    formatstr = '%d'
    start = 0
    step = 1
    for name, value in opts:
        if name in ['-h', '--help']:
            show_help()
        elif name in ['-p', '--path']:
            path = value
        elif name in ['-f', '--format']:
            formatstr = value
        elif name in ['-s', '--start']:
            start = int(value)
        elif step in ['--step']:
            step = int(value)

    try:
        rename(path, formatstr, start, step)
    except UnboundLocalError as error:
        show_help()
        print('\n! :', error)
    except FileNotFoundError as error:
        show_help()
        print('\n! :', error)
    finally:
        pass


if __name__ == '__main__':
    main()
