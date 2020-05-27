#!/usr/bin/python3

import sys
import os
import subprocess


class Pusher:
    pass

    def modified(self):

        try:
            files = str(subprocess.check_output(
                "git status -s . | grep ' M '", shell=True))
            files = files.replace("b", '').replace(
                ' M ', '').replace("\\n", "\n").replace("'", '').strip().split()
            print(files)
        except Exception as ex:
            print(ex)

    def force(self):

        try:
            files = subprocess.check_output(
                "git status -s . | grep ' M '", shell=True)
        except expression as identifier:
            pass
        print(files)
        try:
            files += subprocess.check_output(
                "git status -s . | grep '?? '", shell=True)
        except Exception as ex:
            print(ex)

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
test.modified()


""" if __name__ == "__main__":

    get_args() """
