import droids
from array_queue import Queue
from node_stack import Stack

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

def assemble_droids(worker_belt, coworker_belt):

    p_count = 0
    a_count =0

    done = False

    ship = Stack()
    container = Stack()

    p_droid = droids.Droid("P"+str(p_count), droids.PROTO)
    a_droid = droids.Droid("A"+str(a_count), droids.ASTRO)

    while (not worker_belt.is_empty()) or (not coworker_belt.is_empty()):
        if install_part(p_droid, worker_belt, coworker_belt):
            print(p_droid)
            p_count += 1
            container.push(p_droid)
            p_droid = droids.Droid("P"+str(p_count), droids.PROTO)
            if len(container) == 5:
                ship.push(container)
                container = Stack()
        if install_part(a_droid, worker_belt, coworker_belt):
            print(a_droid)
            container.push(a_droid)
            a_count += 1
            a_droid = droids.Droid("A"+str(a_count), droids.ASTRO)
            if len(container) == 5:
                ship.push(container)
                container = Stack()
        

    return ship

def main():
    p_belt = Queue()
    a_belt = Queue()
    unload_shipment("parts_0001_0001.txt", p_belt)

    astro = droids.Droid(1, droids.ASTRO)
    install_part(astro, p_belt, a_belt)

    ship = assemble_droids(p_belt, a_belt)

    print(ship)

if __name__ == "__main__":
    main()