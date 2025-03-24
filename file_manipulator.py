import sys
import os

def error_exit(message="Invalid argument."):
     print(f"Error: {message}")
     sys.exit(1)

def validate_args(arglist, expected_length):
    if len(arglist) != expected_length:
        error_exit(f"Expected {expected_length - 1} arguments, but got {len(arglist) - 1}.")

def validate_input_files(inputpath):
    if not os.path.isfile(inputpath):
        error_exit(f"Input file '{inputpath}' not found.")

def validate_output_files(outputpath):
    if os.path.isdir(outputpath):
        error_exit(f"Output path '{outputpath}' is a directory, not a file.")
    try:
        with open(outputpath, "w") as f:
            pass
    except OSError:
        error_exit(f"Cannot write to output file '{outputpath}'.")

def read_file(inputpath):
    with open(inputpath, "r") as f:
        return f.read()

def write_file(outputpath, contents):
    with open(outputpath, "w") as f:
        f.write(contents)

# --- main --- 
arglist = sys.argv

if len(arglist) < 2:
    error_exit("No command provided.")

command = arglist[1]
            
match command:
    case "reverse" | "copy":
        validate_args(arglist, 4)
        inputpath = arglist[2]
        outputpath = arglist[3]

        validate_input_files(inputpath)
        validate_output_files(outputpath)

        contents = read_file(inputpath)

        if command == "reverse":
            contents = contents[::-1]

        write_file(outputpath, contents)
    
    case "duplicate-contents":
        validate_args(arglist, 4)

        inputpath = arglist[2]
        validate_input_files(inputpath)

        n_str = arglist[3]

        if not n_str.isdigit():
            error_exit("The third argument must be a positive integer.")

        n = int(n_str)
        if n <= 0:
            error_exit("The third argument must be a positive integer.")
        
        contents = read_file(inputpath) * n
        write_file(inputpath, contents)
    
    case "replace-string":
        validate_args(arglist, 5)

        inputpath = arglist[2]
        validate_input_files(inputpath)

        old_string = arglist[3]
        new_string = arglist[4]

        if not old_string.strip():
            error_exit("Replacement target cannot be an empty or whitespace-only string.")

        contents = read_file(inputpath).replace(old_string, new_string)
        write_file(inputpath, contents)

    case _:
        error_exit(f"Unknown command: '{command}'. Available commands: reverse, copy, duplicate-contents, replace-string.")