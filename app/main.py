import sys

shell_builtins = ["echo", "exit", "type"]


def echo(arguments):
    print(' '.join(arguments))

def type(cmd):
    cmd = cmd[0]
    if cmd in shell_builtins:
        print(f"{cmd} is a shell builtin")
    else:
        print(f"{cmd}: not found")

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = list(input().split())
    main_command = command[0]
    arguments = command[1:]

    if main_command == "exit":
        sys.exit(0)
    elif main_command == "echo":
        echo(arguments)
    elif main_command == "type":
        type(arguments)
    else:
        print(f"{main_command}: command not found")

    main()


if __name__ == "__main__":
    main()
