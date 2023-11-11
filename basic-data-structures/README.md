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
- What is a deque and why is it not spelled "dequeue"?
- How do deques differ from Python lists in both functionality and performance?
- What is the benefit of using a doubly-ended queue (Deque) over a stack or a queue?
- What would be the time complexity of searching for an element in a stack, queue, and deque?
- Can a deque be used as a stack and a queue both? If so, how?
- Distinguish between "list" and "array" in programming terms.
- Differentiate the "add" operation from "append" in the context of an unordered list.
- Define a linked list and discuss the existence and characteristics of unlinked or hashed lists.
- Discuss the significance of the "next" attribute in a Node class when implementing lists in Python, including the implications of leaving it uninitialized or naming it differently.
- Clarify the concept of "grounding the node" and the advantages of using "Null" to indicate an empty list versus having a tail attribute.
- Describe the considerations for placing new items in a list, contrasting ordered and unordered lists.
- Compare direct assignment of values to attributes versus the use of setter methods in object-oriented programming.
- For linked lists, should the "next" property of a Node point forwards or backwards, and from which end should the list be elongated?
- Discuss the concept and potential existence of un-linked lists.
- Explain the process of linked list traversal, including how it differs when the list is empty.
- Define "inchworming" in the context of linked list manipulation, the types of manipulations that require this approach, and the rationale behind it.
- Outline the differences and special considerations when removing the first node, last node, or nodes in other positions from a list.
- Discuss the time complexity of various list operations and the factors that affect this complexity.
- Examine the relevance of the term "index" in an unordered list.
- Contrast the list operations (add, append, pop, search, remove, insert, is_empty) in ordered versus unordered lists.
- Evaluate the appropriateness of using insert, pop, and append operations in an ordered list.
- Assess whether Python uses a linked list to implement its list data structure by analyzing the time complexity of list operations.
- Determine the outcome and potential problems of executing the steps of the linked list "add" method in reverse order.
- Describe the procedure of the linked list "remove" method when the targeted item is in the last node.
- Explain the operation of the "remove" method in a linked list when the item to be removed is within the sole node of the list.
- Evaluate the time complexity of operations of doubly linked list.
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
### Lists
- [Implement an unordered list in python, page 99](./UnorderedList.py)
- [Implement an ordered list in python, page 108](./OrderedList.py)
- [Implement a queue with linked list](./Queue_with_list.py)
- [Implement a stack with linked list](./Stack_with_list.py)
- [Implement a deque with linked list](./Deque_with_list.py)
- [Implement a doubly linked list](./DoublyLinkedList.py)
## Todo pratices at page
3,4,5,6,7,10,11,12,14,15,16,18,23