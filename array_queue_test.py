from array_queue import Queue

def test_creation():
    # Setup

    # Invoke
    actual = Queue()

    # Analysis
    assert actual.is_empty()
    assert str(actual) == "[]"