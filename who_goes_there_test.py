from who_goes_there import Task

def test_task_get():
    # Setup
    expected_name = "somename"
    expected_location = "somelocation"

    # Invoke
    result = Task(expected_name, expected_location)

    # Analysis
    assert expected_name == result.get_name()
    assert expected_location == result.get_location()

def test_task_set():
    # Setup
    task = Task("randomname", "randomlocation")

    # Invoke
    task.set_name("newname")
    task.set_location("newlocation")

    assert task.get_name() == "newname"
    assert task.get_location() == "newlocation"

def test_task_repr():
    # Setup
    task = Task("randomname", "randomlocation")

    # Invoke
    result = str(task)

    # Analysis
    assert "randomname in randomlocation" == result