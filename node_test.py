from node_stack import Stack

def test_creation():
    # Setup

    # Invoke
    actual = Stack()

    # Analysis
    assert actual.is_empty()
    assert str(actual) == "[]"

def test_push_one():
    # Setup
    stack = Stack()

    # Invoke
    stack.push(1)

    # Analysis
    assert not stack.is_empty()
    assert str(stack) == "[1]"