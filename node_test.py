from node_stack import Stack

def test_creation():
    # Setup

    # Invoke
    actual = Stack()

    # Analysis
    assert actual.is_empty()
    assert print(actual)