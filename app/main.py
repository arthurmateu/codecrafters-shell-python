import sys
import os
from app import funcs as f

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    separator = command.find(" ")

    if separator > 0:
        main_command = command[:separator]
        arguments = command[separator+1:]
    else:
        main_command = command
        arguments = ''


    if main_command == "exit":
        sys.exit(0)

    elif main_command == "echo":
        f.echo(arguments)

    elif main_command == "type":
        f.command_type(arguments)

    elif main_command == "pwd":
        print(os.getcwd())

    elif main_command == "cd":
        if len(arguments) == 0:
            arguments = ["~"]
        f.change_directory(arguments[0])

    elif f.exists_in_path(main_command) or os.path.exists(main_command):
        f.run_command(command)

    else:
        print(f"{main_command}: command not found")

    main()


if __name__ == "__main__":
    main()
