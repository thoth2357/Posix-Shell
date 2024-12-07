import sys
import os


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    
    # implementing the handler to handle invalid commands
    sys.stdout.write(f"{command}: command not found\n")

    # os.system(command:= input())
    # if command 


if __name__ == "__main__":
    main()
