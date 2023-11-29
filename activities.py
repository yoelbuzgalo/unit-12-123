from node import Node

def length(node, count=0):
    if node == None:
        return count
    else:
        count += 1
        return length(node.get_next(), count)

def main():
    seq = Node(3, Node(2, Node(1)))
    print(length(seq))

if __name__ == "__main__":
    main()