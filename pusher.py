#!/usr/bin/python3

import sys
import os
import subprocess


class Pusher:
    pass

    def __init__(self):
        if os.path.isfile('.tasks'):
            pass
        else:
            print('Pusher: you must first run the command:')
            print('tasker <project_link>')
            exit(1)

    def list_mod(self):

        try:
            """Modified files are captured"""
            return str(subprocess.check_output(
                "git status -s . | grep ' M '", shell=True)).replace("b", '').replace(
                ' M ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            print('Pusher: There are no modified files that need to be uploaded')
            exit(1)

    def list_new(self):

        try:
            """New files are captured"""
            return str(subprocess.check_output(
                "git status -s . | grep '?? '", shell=True)).replace("b", '').replace(
                '?? ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            print('Pusher: There are no new files that need to be uploaded')
            exit(1)

    def list_all(self):

        try:
            """All files are captured"""
            return str(subprocess.check_output(
                "git status -s .", shell=True)).replace("b", '').replace(
                '?? ', '').replace(' M ', '').replace("\\n", "\n").replace("'", '').strip().split()

        except Exception:
            print('Pusher: There are no files that need to be uploaded')
            exit(1)

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

    if count > 1:
        print('Usage: pusher [OPTIONS]')
        exit(1)

    if count is 0:
        if input('Are you sure you want to upload all new and changed files? Yes/No\n') == 'Yes':
            return pusher.list_all()
        else:
            exit(0)

    if count is 1:
        method = args[0]

        if method == '-m':
            return pusher.list_mod()
        elif method == '-n':
            return pusher.list_new()
        else:
            print('Invalid option', method)
            exit(1)


if __name__ == "__main__":

    pusher = Pusher()
    files = get_args()

    tasksfile = open('.tasks', 'r')
    tasks = tasksfile.read().splitlines()

    changecommit = input(
        'How should you handle commits?\n0 - Default\n1 - Edit\nOpt: ')
    if changecommit not in ['0', '1']:
        print('Pusher: Invalid option')
        exit(1)
    if changecommit is '0':
        for itemname in files:
            commit = '{} added'.format(itemname)
            for task in tasks:
                if task.find(itemname) >= 0:
                    commit = task

            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))

        os.system('git push -u origin master')
        print('\n  -> Files uploaded with their respective commit or filename per commit')
    else:
        for itemname in files:
            commit = input('\n\n[{}]\nInsert commit: '.format(itemname))
            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))
        os.system('git push -u origin master')
        print('\n  -> Files uploaded with custom commit')
