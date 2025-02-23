import os
import subprocess
import shlex

shell_builtins = ["echo", "exit", "type", "pwd", "cd"]
quote_identifiers = ["\"", "'"]

def exists_in_path(cmd):
    path = os.getenv("PATH", "").split(":")

    for p in path:
        path_location = f"{p}/{cmd}"

        if os.path.exists(path_location):
            return path_location


def echo(arguments):

    for i in range(len(arguments)):
        if arguments[i][0] == arguments[i][-1] and arguments[0] in quote_identifiers:
            arguments[i] = arguments[i][1:-1]

    print(" ".join(arguments))



def command_type(cmd):
    cmd = ''.join(cmd)

    if cmd in shell_builtins:
        print(f"{cmd} is a shell builtin")

    elif (path_location:=exists_in_path(cmd)):
        print(f"{cmd} is {path_location}")

    else:
        print(f"{cmd}: not found")


def run_command(cmd):
    subprocess.run(shlex.split(cmd))


def change_directory(dir):
    if not dir or dir == ["~"]:
        dir = os.getenv("HOME")

    try:
        dir = ''.join(dir)
        os.chdir(dir)
    except:
        print(f"cd: {dir}: No such file or directory")
