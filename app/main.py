import sys
import os
from app import funcs as f

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input().strip()
    separator = command.find(' ')

    if separator > 0:
        main_command = command[:separator]
        arguments = f.clean_args(command[separator+1:])

    else:
        main_command = command
        arguments = []

    match main_command:
        case "exit":
            sys.exit(0)

        case "echo":
            f.echo(arguments)

        case "type":
            f.command_type(arguments)

        case "pwd":
            print(os.getcwd())

        case "cd":
            f.change_directory(arguments)

        case _:
            if f.exists_in_path(main_command) or os.path.exists(main_command):
                f.run_command([main_command] + arguments)
            else:
                print(f"{main_command}: command not found")

    main()


if __name__ == "__main__":
    main()
