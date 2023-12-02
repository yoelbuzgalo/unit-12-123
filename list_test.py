from list_stack import Stack

def test_empty_stack():
    # Setup
    expected = "[]"
    expected_len = 0

    # Invoke
    result = Stack()

    # Analysis
    assert result.is_empty()
    assert str(result) == expected
    assert len(result) == expected_len

def test_push_stack():
    # Setup
    expected = "[3, 2, 1]"

    # Invoke
    result = Stack()
    result.push(1)
    result.push(2)
    result.push(3)

    assert not result.is_empty()
    assert str(result) == expected
    assert len(result) == 3

def test_peek_stack():
    # Setup
    stack = Stack()
    expected = 1
    stack.push(1)
    stack.push(expected)

    # Invoke
    result = stack.peek()

    # Analysis
    assert not stack.is_empty()
    assert len(stack) == 2
    assert result == expected

def test_pop_stack():
    # Setup
    stack = Stack()
    expected = 1
    stack.push(1)
    stack.push(expected)

    # Invoke
    result = stack.pop()

    # Analysis
    assert not stack.is_empty()
    assert len(stack) == 1
    assert result == expected

def test_pop_empty_stack():
    # Setup
    stack = Stack()

    # Invoke
    try:
        result = stack.pop()

    # Analysis
    except:
        assert stack.is_empty()
        assert True
        return
    assert False, "Expected IndexError, got " + str(result)

def test_peek_empty_stack():
        # Setup
    stack = Stack()

    # Invoke
    try:
        result = stack.peek()

    # Analysis
    except:
        assert stack.is_empty()
        assert True
        return
    assert False, "Expected IndexError, got " + str(result)