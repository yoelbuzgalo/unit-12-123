from who_goes_there import Task, parse_file, Crewmate

# Task class test

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

# parse_file function test

def test_invalid_filepath():
    # Setup
    filepath = "invalidpath"

    # Invoke
    result = parse_file(filepath)

    # Analysis
    assert result == None

def test_valid_path():
    # Setup
    filepath = "./tasks_01.csv"

    # Invoke
    result = parse_file(filepath)

    # Analysis
    assert result != None
    assert type(result) == type(set())

# Crewmate class test

def test_crewmate_initialization():
    # Setup
    expected_color = "Blue"
    expected_murdered = False
    
    # Invoke
    result = Crewmate(expected_color)

    # Analysis
    assert result.get_color() == expected_color
    assert result.is_murdered() == expected_murdered
    assert result.get_task() == None # Expect none instead of IndexError (guard clause implemented in code)

def test_crewmate_task_add_get():
    # Setup
    crewmate = Crewmate('RandomColor')
    task = Task('Random_Task', 'Random_Location')

    # Invoke
    crewmate.add_task(task)
    result = crewmate.get_task()

    # Analysis
    assert result == task