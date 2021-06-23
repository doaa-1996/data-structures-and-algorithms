# Challenge Summary

Multi-bracket Validation.


## Whiteboard Process
![cc13](code%20challenge13.png)

## Approach & Efficiency


time : O(n)
space:O(n)

## Solution


```
def multi_bracket_validation(str):
      
    open_brackets = tuple('({[')
    close_brackets = tuple(')}]')
    map = dict(zip(open_brackets, close_brackets))
    queue = []
  
    for i in str:
        if i in open_brackets:
            queue.append(map[i])
        elif i in close_brackets:
            if not queue or i != queue.pop():
                return "False"
    if not queue:
        return "True"
    else:
        return "False"
``` 