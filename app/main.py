import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
