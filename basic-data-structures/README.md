# CHAPTER THREE | BASIC DATA STRUCTURES
## Review Questions
- How does the choice of using the start or end of a Python list as the top impact the performance of a stack?
- Why is a Python list commonly used to implement a stack? Is it effective?
- What are the common characteristics of problems that are efficiently solved using a stack?
- In what scenarios is a stack usually a more appropriate data structure than a queue or deque?
- In what scenarios would a queue be more appropriate than a stack or deque?
- What do the terms rear and front signify in the context of a queue?
- What are the performance implications of using the start or end of a Python list as the rear/front in a queue?
- Why does a stack typically have a peek() function, while a queue and a deque do not?
- What is a deque and why is it not spelled 'dequeue'?
- How do deques differ from Python lists in both functionality and performance?
- What is the benefit of using a doubly-ended queue (Deque) over a stack or a queue?
- What would be the time complexity of searching for an element in a stack, queue, and deque?
- Can a deque be used as a stack and a queue both? If so, how?

- What's the difference between the term "list" and "array"?
- What's the differnece between add and append in a unordered list structure
- What's the definition of a linked list? are there unlinked list or hashed list?
- Why is it important to define a next attributes for a Node class in the implement list with Python? what if unininitaized a Null for next attributes? Can we use other attribute name?
- explane "grounding the node" what's the advantage use Null as the indicator of a empty list? why not create a tail attributes?
- Where to place new items into a list? What's this matter in an ordered list and in an unordered list?
- what's the difference between assigning value directly(object.attrrib = something) or using a function(object.set_attrib(something))?
- for a linked list, hte "next" property od Node should be point forward or backword? you should elongate a linked list from which end?
- are there un-linked list?
- explain "linked list traversal". What if an empty list? 
- what is "inch worming" in linked list manipulation? what does it mean? what manipulation need this step? and Why?
- what's the difference when removing first node, last node, and other nodes? Are there special considerations when removing those nodes at specific position?
- what's the time complexity for each list operation? what factors influence the complexity?
- what's the meaning of "index" in an unordered list?

## Exercises
### Stacks
- [Implement a stack in python, page 65](./Stack.py)
- [Reverse a string with stacks, page 67](./reverse_a_string_with_stacks.py)
- [Simple blance parentheses, page 67](./simple_balance_parentheses.py)
- [General blace parentheses, page 69](./general_balance_parentheses.py)
- [Convert decimal numbers to binary numbers, page 71](./convert_decimal_to_binary.py)
- [Convert infix expression to postfix expression, page 76](./convert_infix_to_prefix_and_postfix_expressions.py)
- [Conduct calculation for postfix expression, page 79](./postfix_evaluation.py)
### Queues
- [Implement a queue in python, page 83](./Queue.py)
- [Hot potato, page 84](./hot_potato.py)
- [Printer (unsolved), page 86](./printer.py)
### Deques
- [Implement a deque in python, page 94](./Deque.py)
- [Check if a string is palindrome, page 96](./palindrome_checker.py)