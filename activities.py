from node import Node

def length(node, count=0):
    if node == None:
        return count
    else:
        count += 1
        return length(node.get_next(), count)

def total(node, total_counted=0):
    if node == None:
        return total_counted
    else:
        total_counted += node.get_value()
        return total(node.get_next(), total_counted)

def main():
    seq = Node(3, Node(2, Node(1)))
    print(length(seq))
    print(total(seq))

if __name__ == "__main__":
    main()