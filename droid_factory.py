import droids
from array_queue import Queue

def unload_shipment(filename, belt):
    with open(filename) as file:
        for line in file:
            part = line.strip()
            belt.enqueue(part)

def install_part(droid, my_belt, their_belt):
    if not my_belt.is_empty():
        part = my_belt.dequeue()
        if droid.needs_part(part):
            droid.install(part)
        else:
            their_belt.enqueue(part)

    return droid.is_complete()

def main():
    p_belt = Queue()
    a_belt = Queue()
    unload_shipment("parts_0001_0001.txt", p_belt)
    print(p_belt)

    astro = droids.Droid(1, droids.ASTRO)
    install_part(astro, p_belt, a_belt)
    print(p_belt)

if __name__ == "__main__":
    main()