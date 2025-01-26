import sys
import os
from app import funcs as f

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = list(input().split())
    main_command = command[0]
    arguments = command[1:]

    if main_command == "exit":
        sys.exit(0)
    elif main_command == "echo":
        f.echo(arguments)
    elif main_command == "type":
        f.command_type(arguments)
    elif f.exists_in_path(main_command) or os.path.exists(main_command):
        f.run_command(command)
    else:
        print(f"{main_command}: command not found")

    main()


if __name__ == "__main__":
    main()
