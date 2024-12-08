import sys
import os
from subprocess import Popen, PIPE, STDOUT


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")

    # Wait for user input
    while (command := input("$ ")):
        
        if "exit" == command.split(" ")[0]:
            sys.exit(int(command.split(" ")[-1])) if len(command) == 2 else sys.exit(0)
            break
        
        elif command.split(" ")[0] == "echo":
            sys.stdout.write(f"{command.removeprefix('echo').strip()}\n")
        elif command.split(" ")[0] == "type":
            if "not" in str(Popen(f"type {command.split(' ')[-1]}", shell=True, stdout=PIPE, stderr=STDOUT).communicate()[0]).split():
                sys.stdout.write(f"{command.split(' ')[-1]} not found\n")
            else:
                sys.stdout.write(f"{command.split(' ')[-1]} is a shell builtin\n")

        else:
            # implementing the handler to handle invalid commands
            sys.stdout.write(f"{command.split(' ')[-1]}: command not found\n")
        
        
        # os.system(command:= input())
        # if command 


if __name__ == "__main__":
    main()
