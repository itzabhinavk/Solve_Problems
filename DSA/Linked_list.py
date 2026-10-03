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


def traverse(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


def sum_of_nodes(head):
    current = head
    total = 0
    while current is not None:
        total += current.data
        current = current.next
    return total


def count_nodes(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    return count


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head


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

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head of the reversed list 

 # *** Explain how the reverse_linked_list function works:
   # isme hamne 3 pointers use kiye hain: prev, current, aur next_node.
   # 1. prev ko None se initialize kiya, kyunki reverse karne ke baad last node ka next None hoga.
   # 2. current ko head se initialize kiya, jo ki abhi ke linked list ka pehla node hai.
   # 3. while loop tab tak chalega jab tak current None na ho jaye
                 # ye logic yese work karta hai:
     # pahale next_node me current ka next store karte hain, fir current
     #  ka next ko prev se point karte hain, fir prev ko current pe move
     #  karte hain aur current ko next_node pe move karte hain. isse linked 
     # list reverse ho jata hai.



# ---------- Test ----------
print("Original list:")
print_list(head)

print("Sum of nodes:", sum_of_nodes(head))
print("Count of nodes:", count_nodes(head))

head = insert_at_beginning(head, 5)
print("After inserting 5 at beginning:")
print_list(head)
print("Sum of nodes:", sum_of_nodes(head))
print("Count of nodes:", count_nodes(head))

head = insert_at_end(head, 40)
print("After inserting 40 at end:")
print_list(head)
print("Sum of nodes:", sum_of_nodes(head))
count = count_nodes(head)
print("Count of nodes:", count)

head = insert_at_position(head, 25, 3)
print("After inserting 25 at position 3:")
print_list(head)
sum = sum_of_nodes(head)
print("Sum of nodes:", sum)
count = count_nodes(head)
print("Count of nodes:", count)

# Reverse the linked list
head = reverse_linked_list(head)
print("After reversing the list:")
print_list(head)