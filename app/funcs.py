import os
import subprocess
import hashlib

shell_builtins = ["echo", "exit", "type"]


def echo(arguments):
    print(" ".join(arguments))


def command_type(cmd):
    cmd = cmd[0]
    if cmd in shell_builtins:
        print(f"{cmd} is a shell builtin")
    else:
        path = os.getenv("PATH", "").split(":")
        for p in path:
            path_location = f"{p}/{cmd}"
            if os.path.exists(path_location):
                print(f"{cmd} is {path_location}")
                break
        else:
            print(f"{cmd}: not found")


def run_command(cmd):
    main_cmd = cmd[0]
    arg_cnt = len(cmd)

    print(f"{main_cmd} was passed {arg_cnt} args (including program name).")
    for idx, arg in enumerate(cmd):
        print(f"Arg #{idx}", end="")
        if idx == 0: print(" (program name)", end="")
        print(f": {arg}")

    signature = hashlib.sha1(main_cmd.encode()).hexdigest()
    print(f"Program Signature: {signature}")

    subprocess.run(cmd)
