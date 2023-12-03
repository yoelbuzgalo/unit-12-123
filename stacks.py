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
