#!/usr/bin/python3

import sys
import os
import subprocess


class Pusher:
    pass

    def force(self):
        files = subprocess.check_output("git status -s . | grep ' M '")
        print(files)
        files += subprocess.check_output("git status -s . | grep '?? '")
        print(files)


def get_args():

    args = sys.argv[1:]
    count = len(args)

    if count is 2:
        method = args[0]

        print(method)
        if method is '-m':
            pass


test = Pusher()
test.force()


""" if __name__ == "__main__":

    get_args() """
