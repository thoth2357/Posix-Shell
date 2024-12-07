import sys
import os


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")

    # Wait for user input
    while (command := input("$ ")):
        
        if "exit" ==  command.split(" ")[0]:
            sys.exit(int(command.split(" ")[-1]))
            break
        
        elif command.split(" ")[0] == "echo":
            sys.stdout.write(f"{command.removeprefix('echo').strip()}\n")
        else:
            # implementing the handler to handle invalid commands
            sys.stdout.write(f"{command}: command not found\n")
        
        
        # os.system(command:= input())
        # if command 


if __name__ == "__main__":
    main()
