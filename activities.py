from node import Node

def length(node, count=0):
    # if node == None:
    #     return count
    # else:
    #     count += 1
    #     return length(node.get_next(), count)
    count = 0
    while node is not None:
        count += 1
        node = node.get_next()
    return count

def total(node, total_counted=0):
    # if node == None:
    #     return total_counted
    # else:
    #     total_counted += node.get_value()
    #     return total(node.get_next(), total_counted)
    total = 0
    while node is not None:
        total += node.get_value()
        node = node.get_next()
    return total



"""
Activity 12.7, Visualizing Stack Operations:
[5]
[5,8]
[5]
[5,3]
[5]
[5,1]

Activity 12.16, Visualizing Queue:
[5]
[5,8]
[8]
[8,3]
[3]
[3,1]
"""

def main():
    seq = Node(3, Node(2, Node(1)))
    print(length(seq))
    print(total(seq))

if __name__ == "__main__":
    main()