# Challenge Summary

fifo_animal_shelter

Create a class called animal shelter that keeps a queue of cats and dogs. It has 2 methods


## Whiteboard Process


![cc12](code%20challenge12.png)


## Approach & Efficiency


Enqueue: time: O(n) space: O(1)
Dequeue: time: O(1) space: O(1)


## Solution

```
   
class FifoAnimalShelter(Queue):
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0


  def enqueue_dog_or_cat(self, animal): 
    if animal == 'Dog' or animal == 'Cat':
      print(f'Thanks for dropping off your {animal}')
      self.enqueue(animal)
      return 
    raise Exception('Invalid entry. Only Dogs and Cats allowed')

  def dequeue_dog_or_cat(self, pref=None): 

    if pref == None:
      removed = self.dequeue()
      print(f'Congrats! You adopated a {removed}')
      return removed

    if pref == "Cat" or pref == 'Dog':
      temp = self.front 

      while (temp.next is not None and 
              temp.next.value != pref): 
          temp = temp.next
            
      if temp.next is None: 
          print(f'Sorry, we are out of {pref}s') 
            
      else: 
          print('temp', temp.next)
          removed = temp.next
          temp.next = temp.next.next
          self.length -=1
          return removed
          
    else:
      print(f"Sorry, don't have any {pref}s. Just cats and dogs here")
      return None

```