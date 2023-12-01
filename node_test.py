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

def test_push_three():
    # Setup
    stack = Stack()

    # Invoke
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Analysis
    assert not stack.is_empty()
    assert str(stack) == "[3, 2, 1]"

def test_len_0():
    # Setup
    stack = Stack()

    # Invoke
    length = len(stack)

    # Analysis
    assert length == 0

def test_len_2():
    # Setup
    stack = Stack()

    # Invoke
    stack.push(1)
    stack.push(2)
    length = len(stack)

    # Analysis
    assert length == 2

def test_peek_empty():
    # Setup
    stack = Stack()
    
    # Invoke
    try:
        peek = stack.peek()
    
    # Analysis
    except IndexError:
        assert True
        return
    assert False, "Expected IndexError got " + str(peek)

def test_peek_2():
    # Setup
    stack = Stack()
    expected = 1
    
    # Invoke
    stack.push(2)
    stack.push(expected)
    peek = stack.peek()

    # Analysis
    assert peek == expected

def test_pop_empty():
    # Setup
    stack = Stack()
    
    # Invoke
    try:
        popped = stack.pop()
    
    # Analysis
    except IndexError:
        assert True
        return
    assert False, "Expected IndexError got " + str(popped)

def test_pop_2():
    # Setup
    stack = Stack()
    expected = 1
    
    # Invoke
    stack.push(expected)
    stack.push(2)
    popped = stack.pop()
    popped = stack.pop()

    # Analysis
    assert popped == expected
    assert str(stack) == "[]"
    assert len(stack) == 0