from stacks import process_file
from list_stack import Stack

def test_invalid_file():
    # Setup
    filepath = "./invalidpath12341a!!"
    
    # Invoke
    try:
        result = process_file(filepath)
    
    # Analysis
    except:
        assert True
        return
    assert result == False

def test_valid_file():
    # Setup
    filepath = "./data/walrus.txt"

    # Invoke
    try:
        result = process_file(filepath)

    # Analysis
    except:
        assert False
        return
    assert type(result) == type(Stack())

def test_main_stack_content():
    # Setup
    filepath = "./data/walrus.txt"

    # Invoke
    result = process_file(filepath)
    peeked_result = result.peek()

    # Analysis
    assert type(peeked_result) == type(Stack())

def test_list_stack_content():
    # Setup
    filepath = "./data/walrus.txt"

    # Invoke
    result = process_file(filepath)
    top_line_in_main = result.peek()
    top_character_in_stack = top_line_in_main.peek()

    # Analysis
    assert top_character_in_stack == "T"