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
                "git status -s . | grep ' M '", shell=True)).replace("b'", '').replace(
                ' M ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            print('Pusher: There are no modified files that need to be uploaded')
            exit(1)

    def list_new(self):
        try:
            """New files are captured"""
            return str(subprocess.check_output(
                "git status -s . | grep '?? '", shell=True)).replace("b'", '').replace(
                '?? ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            print('Pusher: There are no new files that need to be uploaded')
            exit(1)

    def list_all(self):

        try:
            """All files are captured"""
            return str(subprocess.check_output(
                "git status -s .", shell=True)).replace("b'", '').replace(
                '?? ', '').replace(' M ', '').replace("\\n", "\n").replace("'", '').replace(' D ', '') .strip().split()

        except Exception:
            print('Pusher: There are no files that need to be uploaded')
            exit(1)


class Message:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_args():

    args = sys.argv[1:]
    count = len(args)
    usage = 'Usage: pusher [OPTION]\n    -m (modified)\n    -n (new)\n    -a (all)'

    if count is 0 or count > 1:
        print(usage)
        exit(1)
    if args[0] == '-m':
        return pusher.list_mod()
    elif args[0] == '-n':
        return pusher.list_new()
    elif args[0] == '-a':
        return pusher.list_all()
    else:
        print(usage)
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
                if task.find('./' + itemname) >= 0:
                    commit = task

            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))

        push = True if input('You want to upload the files now? Y/N\n>> ') in [
            'Y', 'y'] else False
        if push:
            os.system('git push -u origin master')
            print(
                '\n  -> Files uploaded with their respective commit or filename per commit')
        else:
            print('You will need to use "git push" to publish your local commits')

    else:
        for itemname in files:
            commit = input('\n[{}]\nInsert commit: '.format(itemname))
            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))

        push = True if input('\n[=====================================]\nYou want to upload the files now? Y/N\n>> ') in [
            'Y', 'y'] else False
        if push:
            os.system('git push -u origin master')
            print('\n  -> Files uploaded with custom commit')
        else:
            print('You will need to use "git push" to publish your local commits')
