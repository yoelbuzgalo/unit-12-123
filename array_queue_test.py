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