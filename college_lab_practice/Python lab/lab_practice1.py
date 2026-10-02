#  List Operation: insert, replace, remove, search, and sort 

def insert(list,item,pos):
    print("Before inserting the item: ", list)
    list.insert(pos-1,item)
    print("After inserting the item:",list)

def replace(list,item,pos):
    print("Before replace the item", list)
    list[pos-1] = item
    print("After replacing the item:",list)

def remove(list,item):
    print("Before removing the item:",list)
    list.remove(item)
    print("After removing the item:",list)

def search(list,item):
    print("Search for the item in the list: ", list)
    if item in list:
        print("Item found at position:",list.index(item)+1)
    else:
        print("Item not found")

def sort(list):
    list.sort()
    print("After sorting the list:",list)

# Example usage
my_list = [5, 2, 9, 1, 5, 6]

insert(my_list, 10, 3)
replace(my_list, 7, 2)
remove(my_list, 5)
search(my_list, 9)
sort(my_list)


# dictionary operation: Add, Acces , Replace, and Remove Keys
 
def Add_key(dict,key,value):
    print("Before adding the key-value pair:",dict)
    dict[key]= value
    print("After adding the key-value pair:",dict)

def Access_key(dict,key):
    if key in dict: 
        print("Value for tne key", key,"is: ", dict[key])
    else:
        print("key not found")

def replace_key(dict,key,value):
    print("before replacing the value for the key ", key,":",dict)
    dict[key]=value
    print("After replacing the value for the key ", key,":",dict)

def remove_key(dict,key):
    print("Before removing the key-value pair:",dict)
    if key in dict:
        del dict[key]
        print("After removing the key-value pair: ", dict)

# Example usage 

my_dict = {'a': 1,
           'b': 2, 
           'c': 3,
           'd': 4
           }
Add_key(my_dict,'e',5)
Access_key(my_dict,'c')
replace_key(my_dict,'b',20)
remove_key(my_dict,'a')


