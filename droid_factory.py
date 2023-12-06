from droids import Droid
from array_queue import Queue

def unload_shipment(filename, belt):
    with open(filename) as file:
        for line in file:
            part = line.strip()
            belt.enqueue(part)

def main():
    belt = Queue()
    unload_shipment("parts_0001_0001.txt", belt)
    print(belt)

if __name__ == "__main__":
    main()