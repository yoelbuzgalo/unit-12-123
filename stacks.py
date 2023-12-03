from list_stack import Stack

def process_file(filename):
    """
    This function takes in a file path, opens and returns a main stack with line stacks.
    """
    try:
        with open(filename) as file:
            main_stack = Stack() # Create a main stack
            for line in file:
                line_stack = Stack() # Create a line stack
                line = line.strip() # Strips off trailing whitespaces or new-lines
                for character in line:
                    line_stack.push(character) # Add characters to the line stack
                main_stack.push(line_stack) # Add line stack to main stack
        return main_stack
    except FileNotFoundError:
        print("Could not find or open:", filename)
        return False
    
def process_stack(main_stack):
    """
    This function takes in a main stack and prints & removes every line until complete.
    """
    while len(main_stack) > 0:
        line_stack = main_stack.pop() # Get the line
        string = "" # Initialize empty string container
        while len(line_stack) > 0:
            string += line_stack.pop()
        print(string)
    return

def main():
    processed_file = process_file("./data/walrus.txt")
    process_stack(processed_file)

if __name__ == "__main__":
    main()