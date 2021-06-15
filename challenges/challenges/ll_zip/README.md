# Challenge Summary
 Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Whiteboard Process
![cc8](code%20challenge%208.png)


## Approach & Efficiency
The strategy here uses a temporary dummy node as the start of the result list. The pointer tail always points to the last node in the result list. The dummy node gives tail something to point to initially when the result list is empty. . The loop proceeds, removing one node from either a or b and adding it to tail. When we are done, the result is in dummy.next.

efficiency O(n)

## Solution
```

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
 
```

**result**
ll1 : 1->2->3

ll2 : 4->5->6

after

1->4->2->5->3->6
