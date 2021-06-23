class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(msg, head):
    print(msg, end='')
    ptr = head
    str=''
    while ptr:
        str+=f'{ptr.data} —> '
        ptr = ptr.next
    str+='None' 
    print(str)
    return str



def zipLists(a, b):

    dummy = Node()
    tail = dummy

    while True:
        if a is None:
            tail.next = b
            break

        elif b is None:
            tail.next = a
            break

        else:
            tail.next = a
            tail = a
            a = a.next

            tail.next = b
            tail = b
            b = b.next

    return dummy.next


if __name__ == '__main__':
    a = b = None
    for i in reversed(range(1, 3, 1)):
        a = Node(i, a)

    for i in reversed(range(2, 5, 1)):
        b = Node(i, b)

    printList("First List: ", a)
    printList("Second List: ", b)

    head = zipLists (a,b)
    printList("After merging: ", head)
