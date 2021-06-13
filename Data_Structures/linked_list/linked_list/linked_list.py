class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    def include(self, value):
        inc = False
        current = self.head
        if not current:
            return inc
        else:
            while(current.next != None):
                if current.value == value:
                    inc = True
                    break
                current = current.next
            else:
                if(current.value == value):
                    return True
            return inc
    def __str__(self):
        out = ''
        current = self.head
        if not current:
            return 'None'
        else:
            while current.next != None:
                out = out + '{ ' + str(current.value) + ' } -> '
                current = current.next
            else:
                out += '{ ' + str(current.value) + ' } -> None'
            return out
    def insertBefore(self, targetValue, value):
        # create new node
        newNode = Node(value)
        # find target node to append
        node = self.head
        if node == None:
            print('There aren\'t any nodes to append before!')
        else:
            found = False
            # search nodes
            while node:
                if node.next == None:
                    break
                if node.next.value == targetValue:
                    found = True
                    newNode.next = node.next
                    node.next = newNode
                    break
                else:
                    node = node.next
            if found != True:
                print('Your target node of {} was not found in the list!'.format(
                    targetValue))



    def insert(self, new_data):
 
    # 1 & 2: Allocate the Node &
    #        Put in the data
     new_node = Node(new_data)
         
    # 3. Make next of new Node as head
     new_node.next = self.head
         
    # 4. Move the head to point to new Node
     self.head = new_node

    def display(self):
        # variable for iteration
        x = self.head
        # iterating until we reach the end of the linked list
        while x != None:
            # printing the node data
            print(x.value, end='->')
            # moving to the next node
            x = x.next
        print('Null')
    def insertAfter(self,old_data,new_data):
        d_new=Node(new_data)
        temp=self.head
        while(temp):
            if temp.value==old_data:
                d_new.next = temp.next
                temp.next = d_new
                break    
if __name__ == "__main__":
    linklist = LinkedList()

# linklist.append(1)
# linklist.append(2)
# linklist.append(3)
# linklist.append(4)
# linklist.append(5)
# linklist.append(4)
# linklist.insertBefore(4, 9)
# linklist.insertAfter(1,10)
# linklist.insert(0)
# linklist.display()