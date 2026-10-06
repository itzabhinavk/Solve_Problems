# Day 21 - 100 Days of Code Challenge


# argement and return

def show_info(**data):
    print(type(data))
    for k,v in data.items():
        print(f'{k},{v}')   
show_info(name='Abhinav',age=19,city='Jamui')


def total(*nums):
    print(type(nums))
    return sum(nums)
print(total(1,3,5,7,9))
print(total(2,4,6,8))
print(total(10))
numbers=[1,2,3,4,5]
print(total(*numbers))


def student(name,age,city):
    print(f'{name}, {age}, {city}')
student("Abhinav",19,'banka')
student(age=18, name='Varsha', city='unknown')
student("Abhinav",city='banka',age=19)


def greet(name,msg='good morning'):
    print(f'{msg} {name}!')
greet("Abhinav")
greet("Varsha", "good evening")


# combining All types of arguments in a single function
def demo(a, b, *args, sep='-', **kwargs):
    print(a, b)
    print(args)
    print(sep)
    print(kwargs)
demo(1, 2, 3, 4, 5, sep=':', name='Abhinav', age=19, city='banka')