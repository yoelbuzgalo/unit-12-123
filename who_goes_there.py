import csv
import random
from node_stack import Stack
from array_queue import Queue

CREW_COLORS = ['Black', 'Blue', 'Brown', 'Cyan', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow']

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

class Crewmate:
    """
    This class represents a crewmate object which will consist their unique color identifier and associated tasks assigned to them
    """
    __slots__ = ['__color', '__murdered', '__tasks']
    
    def __init__(self, color):
        self.__color = color
        self.__murdered = False
        self.__tasks = Stack()

    def __repr__(self):
        return "Crewmate:"\
        + "\n color=" + self.__color\
        + "\n murdered=" + str(self.__murdered)\
        + "\n tasks=" + str(self.__tasks)\
    
    def __str__(self):
        if self.is_murdered():
            return self.__color + " Crewmate (deceased)"
        return self.__color + " Crewmate"

    def get_color(self): # Returns crewmate's color
        return self.__color
    
    def get_tasks(self): # Returns the entire stack
        return self.__tasks
    
    def get_task(self): # Returns a copy of most priority (LIFO)
        if len(self.__tasks) > 0:
            return self.__tasks.peek()
    
    def complete_task(self): # If crewmate's task is marked complete, pop out of his stack
        return self.__tasks.pop()
    
    def add_task(self, task): # Add a given task to crewmate's tasks todo
        self.__tasks.push(task)
        return
    
    def is_murdered(self): # Checks if the crewmate is murdered or not, returns True if murdered
        if self.__murdered == True:
            return True
        return False

    def murder(self): # Kill the crewmate if this function is called.
        self.__murdered = True

class Imposter:
    __slots__ = ['__location']
    def __init__(self, location=None):
        self.__location = location

    def __repr__(self):
        return "Imposter:"\
        + "\n location=" + str(self.__location)
    
    def __str__(self):
        return "Imposter"

    def get_location(self):
        return self.__location
    
    def set_location(self, location):
        self.__location = location

class Ship:
    """
    This class represents the entire ship's available tasks throughout the journey, whereas locations are derived from each tasks
    """
    __slots__ = ['__tasks', '__locations', '__crew']

    def __init__(self, tasks):
        self.__tasks = [task for task in tasks] # Make a copy of new seperate list, rather than referencing to original list
        self.__locations = set()
        self.__crew = {
            'crewmates': list(),
            'imposters': list()
        }
        for task in self.__tasks:
            self.__locations.add(task.get_location())
    
    def get_tasks(self):
        # Returns the object containing the tasks list
        return self.__tasks
    
    def get_locations(self):
        # Returns all of the unique locations in a set
        return self.__locations
    
    def get_crew(self):
        return self.__crew

    def __create_crew(self, imposters):
        """
        Helper function to create a set of crewmates
        """
        colors = set(CREW_COLORS) # Initialize a set of unique colors available for selection
        count = 0 # Initialize counter variable
        amount_to_create = 10 - imposters
        
        while count < amount_to_create:
            random_color = CREW_COLORS[random.randrange(0, len(CREW_COLORS))] # Select a random color
            if random_color in colors: # If selected color is available, go ahead use it
                self.__crew['crewmates'].append(Crewmate(random_color))
                colors.remove(random_color) # Once used, remove it from available colors
                count += 1
            else:
                continue
        
        for _ in range(imposters):
            self.__crew['imposters'].append(Imposter())

        return
    
    def __assign_tasks(self):
        task_list = self.__tasks
        for i in range(len(self.__crew['crewmates'])):
            for _ in range(0, random.randint(3, 6)):
                random_task = task_list[random.randrange(0, len(task_list))]
                self.__crew['crewmates'][i].add_task(random_task)
        return
    
    def start_journey(self, imposters):
        self.__create_crew(imposters)
        self.__assign_tasks()

        cafeteria = Queue()
        for crewmate in self.__crew['crewmates']:
            cafeteria.enqueue(crewmate)

        death_roll = set()
        survived = set()

        while not cafeteria.is_empty():
            
            # Send out a crewmate to complete a task
            crewmate = cafeteria.dequeue()

            if (crewmate in death_roll) or (crewmate in survived):
                continue
            
            # Assign new locations for imposters and attempt to kill the crewmate
            for imposter in self.__crew['imposters']:
                iterate_locations = [location for location in self.__locations] # Had to do this because I needed to unpack the 'unique locations' set stored in object and be able to iterate and get specific locations at an index
                select_random_location = iterate_locations[random.randrange(0, len(iterate_locations))]
                imposter.set_location(select_random_location)

                if imposter.get_location() == crewmate.get_task().get_location():
                    crewmate.murder()
                    death_roll.add(crewmate)
                    print("Oof! Imposter has killed", crewmate, "death roll is at:", len(death_roll))
                    break
            
            # If the crewmate is murdered, skip to next queue
            if crewmate.is_murdered():
                continue

            completed_task = crewmate.complete_task()
            if crewmate.get_task() == None:
                print(crewmate, "has survived the game!")
                survived.add(crewmate)
            else:
                print(crewmate, "has completed his task without being killed:", completed_task)
                cafeteria.enqueue(crewmate) # Put back to cafeteria and make them work again next round

        if len(survived) == 0:
            print("Imposters have won the game, killing all of the crewmates!")
        else:
            print("Crewmates have won the game!")
            print("Although, these are are the crewmates that died during the game,", death_roll)            

        return self.__crew # Only for testing purpose
 

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
    tasks = parse_file("./tasks_01.csv")
    while True:
        ship = Ship(tasks)
        try:
            user_input = input("Enter amount of imposters (1-4): ")
            
            if user_input == "": # Quit if user input is blank
                return
            
            amount_of_imposters = int(user_input)

            if amount_of_imposters > 4 or amount_of_imposters < 1:
                raise ValueError()
            
            ship.start_journey(amount_of_imposters)
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()