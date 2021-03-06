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
        newNode = Node(value)
        node = self.head
        if node == None:
            print('There aren\'t any nodes to append before!')
        else:
            found = False
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

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        x = self.head
        while x != None:
            print(x.value, end='->')
            x = x.next
        print('Null')

    def insertAfter(self, old_data, new_data):
        d_new = Node(new_data)
        temp = self.head
        while(temp):
            if temp.value == old_data:
                d_new.next = temp.next
                temp.next = d_new
                break

    def kthFromEnd(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    print ("% d is greater than the no. pf nodes in list" %(n))
                    return

                ref_ptr = ref_ptr.next
                count += 1

        if(ref_ptr is None):
            self.head = self.head.next
            if(self.head is not None):
                 print ("Node no. % d from last is % d "
                                   %(n, main_ptr.value))
        else:

          while(ref_ptr is not None):
              main_ptr = main_ptr.next
              ref_ptr = ref_ptr.next
          print ("Node no. % d from last is % d " %(n, main_ptr.value))

    

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


# linklist.append(1)
# linklist.append(2)
# linklist.append(3)
# linklist.append(4)
# linklist.append(5)
# linklist.kthFromEnd(1)
# linklist.display()
