from array_queue import Queue

def test_creation():
    # Setup

    # Invoke
    actual = Queue()

    # Analysis
    assert actual.is_empty()
    assert str(actual) == "[]"

def test_enqueue():
    # Setup
    queue = Queue()

    # Invoke
    queue.enqueue(5)

    # Analysis
    assert not queue.is_empty()
    assert str(queue) == "[5]"
    assert len(queue) == 1

def test_front_empty():
    # Setup
    queue = Queue()
    
    # Invoke
    try:
        front = queue.front()
    
    # Analysis
    except IndexError:
        assert True
        return
    assert False, "Expected IndexError got " + str(front)

def test_front_enqueued():
    # Setup
    queue = Queue()
    expected = 1
    
    # Invoke
    queue.enqueue(expected)
    front = queue.front()

    # Analysis
    assert front == expected

def test_dequeue_empty():
    # Setup
    queue = Queue()
    
    # Invoke
    try:
        popped = queue.dequeue()
    
    # Analysis
    except IndexError:
        assert True
        return
    assert False, "Expected IndexError got " + str(popped)

def test_dequeue():
    # Setup
    queue = Queue()
    expected = 2
    
    # Invoke
    queue.enqueue(1)
    queue.enqueue(expected)
    queue.dequeue()
    popped = queue.dequeue()

    # Analysis
    assert popped == expected
    assert str(queue) == "[]"
    assert len(queue) == 0