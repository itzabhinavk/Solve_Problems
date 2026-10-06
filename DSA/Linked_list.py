# The code is explained in detail below the code. please read it carefully to understand how linked list works in python.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# list banate hain: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


# FIXED print_list: loop se saare nodes print karta hai, chahe list kitni bhi badi ho
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")



# ========== Linked List Operations ==========

# 1. Traverse karna
def traverse(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

# 2. Sum of nodes
def sum_of_nodes(head):
    current = head
    total = 0
    while current is not None:
        total += current.data
        current = current.next
    return total

# 3. Count of nodes

def count_nodes(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    return count

# 4. Insert at beginning, end, or specific position

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# 5. Insert at end

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

# 6. Insert at specific position

def insert_at_position(head, data, position):
    if position < 0:               # negative position invalid hai
        return head
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if current is None:
            return head
        current = current.next
    if current is None:
        return head
    new_node.next = current.next
    current.next = new_node
    return head

# 7. Reverse the linked list

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head of the reversed list 

 # ========Explain how the reverse_linked_list function works:=================
   # isme hamne 3 pointers use kiye hain: prev, current, aur next_node.
   # 1. prev ko None se initialize kiya, kyunki reverse karne ke baad last node ka next None hoga.
   # 2. current ko head se initialize kiya, jo ki abhi ke linked list ka pehla node hai.
   # 3. while loop tab tak chalega jab tak current None na ho jaye
   # ye logic yese work karta hai:
     # pahale next_node me current ka next store karte hain, fir current
     #  ka next ko prev se point karte hain, fir prev ko current pe move
     #  karte hain aur current ko next_node pe move karte hain. isse linked 
     # list reverse ho jata hai.




#                   ---------- Test ----------
print("Original list:")
print_list(head)  # print_list function ko call karte hain, jo ki linked list ke saare nodes print karega

print("Sum of nodes:", sum_of_nodes(head))  # sum_of_nodes function ko call karte hain, jo ki linked list ke saare nodes ka sum calculate karega
print("Count of nodes:", count_nodes(head))  # count_nodes function ko call karte hain, jo ki linked list ke saare nodes ka count calculate karega

head = insert_at_beginning(head, 5)
print("After inserting 5 at beginning:")
print_list(head)                             # print_list function ko call karte hain, jo ki linked list ke saare nodes print karega
print("Sum of nodes:", sum_of_nodes(head))
print("Count of nodes:", count_nodes(head))

head = insert_at_end(head, 40)
print("After inserting 40 at end:")
print_list(head)                           # print_list function ko call karte hain, jo ki linked list ke saare nodes print karega
print("Sum of nodes:", sum_of_nodes(head))
count = count_nodes(head)
print("Count of nodes:", count)

head = insert_at_position(head, 25, 3)
print("After inserting 25 at position 3:")
print_list(head)                           # print_list function ko call karte hain, jo ki linked list ke saare nodes print karega
sum = sum_of_nodes(head)
print("Sum of nodes:", sum)
count = count_nodes(head)
print("Count of nodes:", count)

# --------Reverse the linked list----------
head = reverse_linked_list(head)
print("After reversing the list:")
print_list(head)



#==================Explain how all functions work in the linked list code in details =========================
# first i am creating a Node class which has two attributes: data and next. The data attribute stores the value of the node, and the next attribute points to the next node in the linked list.
# Then, I am creating a linked list with three nodes: 10 -> 20 -> 30. The head variable points to the first node of the linked list.
# The print_list function takes the head of the linked list as an argument and prints all the nodes in the linked list. It uses a while loop to traverse the linked list until it reaches the end (when current is None).
# The traverse function is similar to print_list, but it only prints the data of each node without the arrows.
# The sum_of_nodes function calculates the sum of all the nodes in the linked list. It initializes a total variable to 0 and adds the data of each node to total as it traverses the linked list.
# The count_nodes function counts the number of nodes in the linked list. It initializes a count variable to 0 and increments it for each node as it traverses the linked list.
# The insert_at_beginning function inserts a new node at the beginning of the linked list. It creates a new node with the given data, sets its next attribute to the current head, and returns the new node as the new head of the linked list.
# The insert_at_end function inserts a new node at the end of the linked list. It creates a new node with the given data, traverses the linked list to find the last node, and sets the next attribute of the last node to the new node. If the linked list is empty (head is None), it returns the new node as the head.
# The insert_at_position function inserts a new node at a specific position in the linked list. It takes the head of the linked list, the data for the new node, and the position as arguments. If the position is 0, it inserts the new node at the beginning. Otherwise, it traverses the linked list to find the node at the specified position and inserts the new node after it. If the position is invalid (negative or greater than the length of the list), it returns the original head without making any changes.
# The reverse_linked_list function reverses the linked list. It uses three pointers: prev, current, and next_node. It initializes prev to None and current to the head of the linked list. In a while loop, it stores the next node in next_node, sets the next attribute of current to prev, moves prev to current, and moves current to next_node. This process continues until current becomes None, at which point prev points to the new head of the reversed linked list. The function returns prev as the new head of the reversed list.


# This code provides a comprehensive implementation of a singly linked list in Python, including various operations such as traversal, summation, counting nodes, insertion at different positions, and reversing the linked list. Each function is designed to handle specific tasks related to linked lists, making it a useful reference for understanding how linked lists work in practice.
#------------------------- Thanks for reading the code and explanation. If you have any questions or need further clarification, feel free to ask!


 #My name is Abhinav Kumar and i am a software engineer. I have written this code to help you understand how linked lists work in Python. If you have any questions or need further clarification, feel free to ask!