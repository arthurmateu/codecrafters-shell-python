import os
import subprocess

shell_builtins = ["echo", "exit", "type", "pwd", "cd"]


def exists_in_path(cmd):
    path = os.getenv("PATH", "").split(":")
    for p in path:
        path_location = f"{p}/{cmd}"
        if os.path.exists(path_location):
            return path_location


def echo(arguments):
    print(" ".join(arguments))


def command_type(cmd):
    cmd = cmd[0]
    if cmd in shell_builtins:
        print(f"{cmd} is a shell builtin")
    elif (path_location:=exists_in_path(cmd)):
        print(f"{cmd} is {path_location}")
    else:
        print(f"{cmd}: not found")


def run_command(cmd):
    subprocess.run(cmd) # fuck this


def change_directory(dir):
    if dir == "~":
        dir = os.getenv("HOME")
    try:
        os.chdir(dir)
    except:
        print(f"cd: {dir}: No such file or directory")
