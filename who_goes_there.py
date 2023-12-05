import csv

class Task:
    """
    This is a task class that stores in a name and location of the task itself
    """
    __slots__ = ['__name', '__location']

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def set_name(self, name):
        self.__name = name
    
    def set_location(self, location):
        self.__location = location

    def __repr__(self):
        return self.__name + " in " + self.__location

def parse_file(filename):
    """
    This function parses a .csv file and returns a list of tasks
    """
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Skip the current header
            list_of_tasks = set()
            for record in csv_reader:
                name, location = record
                list_of_tasks.add(Task(name,location))
            return list_of_tasks
    except FileNotFoundError:
        print("Could not open or find file:", filename)

def main():
    parse_file("./tasks_01.csv")

if __name__ == "__main__":
    main()