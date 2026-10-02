# Day 16 - 100 Days of Code Challenge


#match-case statement 
#multiple value in same same case 
fruit="mango"
match fruit:
    case "apple"|"banana":
        print("comman fruit")
    case "mango"|"litchi":
        print("seasonal fruit")
    case _:
        print("unknown fruit")
    
day=3 
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("twesday")
    
    case _:
        print("invalid day ") 

# pattern matching with variables

point=(1,2) 
match point:
    case (0,0):
        print("orign")  
    case (0,y):
        print(f"On Y-axis at {y}")
    case (x,0):
        print(f"On X-axis at {x}")
    case (x,y):
        print(f"Point at ({x},{y})")

              
    
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")

