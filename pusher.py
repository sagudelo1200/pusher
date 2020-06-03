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
            msg.error(
                'You must first run the command:\ntasker <intranet_project_link>')
            exit(1)

    def list_mod(self, files):
        """Modified files are captured"""
        try:
            return str(subprocess.check_output(
                "git status -s {} | grep ' M '".format(files), shell=True)).replace("b'", '').replace(
                ' M ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            msg.warning(
                'There are no modified files that need to be uploaded')
            exit(1)

    def list_new(self, files):
        """New files are captured"""
        try:
            return str(subprocess.check_output(
                "git status -s {} | grep '?? '".format(files), shell=True)).replace("b'", '').replace(
                '?? ', '').replace("\\n", "\n").replace("'", '').strip().split()
        except Exception:
            msg.warning('There are no new files that need to be uploaded')
            exit(1)

    def list_all(self, files):
        """All files are captured"""
        try:
            return str(subprocess.check_output(
                "git status -s {}".format(files), shell=True)).replace("b'", '').replace(
                '?? ', '').replace(' M ', '').replace("\\n", "\n").replace("'", '').replace(' D ', '') .strip().split()

        except Exception:
            msg.warning('There are no files that need to be uploaded')
            exit(1)


class Msg:
    """colors"""
    BLUE = '\033[94m'
    GREEN = '\033[92m'

    """settings"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    """custom msg types"""
    OK = '\n\033[92m☑ Pusher:\033[0m '
    WARNING = '\n\033[93m⚠ Pusher:\033[0m '
    FAIL = '\n\033[91m⛔ Pusher:\033[0m '

    def error(self, message):
        """[Error message]"""
        print(self.FAIL + message + '\n')

    def warning(self, message):
        """[Warning message]"""
        print(self.WARNING + message + '\n')

    def ok(self, message):
        """[Ok message]"""
        print(self.OK + message + '\n')


def get_args():

    count = len(sys.argv[1:])
    usage = Msg.BLUE + \
        '\nUsage: pusher <option> [files]\n\nOptions:\n    -m (modified)\n    -n (new)\n    -a (all)\n'

    if count is 0:
        print(usage)
        exit(1)

    option = sys.argv[1]
    files = ['.']
    if count > 1:
        files = sys.argv[2:]
    files = " ".join(files).strip()

    if option == '-m':
        return pusher.list_mod(files)
    elif option == '-n':
        return pusher.list_new(files)
    elif option == '-a':
        return pusher.list_all(files)
    else:
        print(usage)
        exit(1)


if __name__ == "__main__":

    msg = Msg()
    pusher = Pusher()
    files = get_args()

    if len(files) == 0:
        msg.error('There are no files that need to be uploaded')
        exit(1)

    tasksfile = open('.tasks', 'r')
    tasks = tasksfile.read().splitlines()

    changecommit = input(
        Msg.BLUE + '\nHow should you handle commits?\n0 - Default\n1 - Edit\nOpt: ' + Msg.RESET)
    if changecommit not in ['0', '1']:
        msg.error('Invalid option ' + changecommit)
        exit(1)
    if changecommit is '0':
        for itemname in files:
            commit = '{} added'.format(itemname)
            for task in tasks:
                if task.find('./' + itemname) >= 0:
                    commit = task.replace('./' + itemname, '')

            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))

        push = True if input(Msg.BLUE + '\n\n⍰ ' + Msg.RESET + 'You want to upload the files now? [Y/n]\n-> ') in [
            'Y', 'y'] else False
        if push:
            print(Msg.GREEN + '\nUploading files...\033[0m')
            os.system('git push -u origin master')
            msg.ok(
                'Files uploaded with their respective commit or filename per commit\n')
        else:
            msg.warning(
                'You will need to use "git push" to publish your local commits')

    else:
        for itemname in files:
            commit = input(
                Msg.BLUE + '\nFile: \033[0m{}\n\033[94mInsert commit: \033[0m'.format(itemname))
            os.system('git add {}'.format(itemname))
            os.system("git commit -m '{}'".format(commit))

        push = True if input(Msg.BLUE + '\n\n⍰ ' + Msg.RESET + 'You want to upload the files now? [Y/n]\n-> ') in [
            'Y', 'y'] else False
        if push:
            print(Msg.GREEN + '\nUploading files...\033[0m')
            os.system('git push -u origin master')
            msg.ok('Files uploaded with custom commit\n')
        else:
            msg.ok(
                'You will need to use "git push" to publish your local commits')
