import os
import subprocess

shell_builtins = ["echo", "exit", "type", "pwd", "cd"]


def exists_in_path(cmd):
    path = os.getenv("PATH", "").split(":")

    for p in path:
        path_location = f"{p}/{cmd}"

        if os.path.exists(path_location):
            return path_location


def clean_args(arguments):
    if arguments[0] == "'" == arguments[-1] or arguments[0] == '"' == arguments[-1]:
        N = len(arguments)

        cleaned_arguments, i = [], 1
        prev, prev_idx = arguments[0], 0

        while i < N:
            if arguments[i] == prev:
                cleaned_arguments.append(arguments[prev_idx+1 : i])
                i += 1

                while i < N and arguments[i] == ' ':
                    i += 1

                if i < N:
                    prev = arguments[i]
                    prev_idx = i

            i += 1
        return cleaned_arguments

    else:
        return list(arguments.split())

def echo(arguments):
    print(' '.join(arguments))


def command_type(cmd):
    cmd = cmd[0]
    if cmd in shell_builtins:
        print(f"{cmd} is a shell builtin")

    elif (path_location:=exists_in_path(cmd)):
        print(f"{cmd} is {path_location}")

    else:
        print(f"{cmd}: not found")


def run_command(cmd):
    subprocess.run(cmd)


def change_directory(dir):
    if not dir or dir == "~":
        dir = os.getenv("HOME")

    try:
        os.chdir(dir)
    except:
        print(f"cd: {dir}: No such file or directory")
