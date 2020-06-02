
# Passing by value Vs passing by Ref
import time
import statistics
# define a doubling function that passes args by value
def mult2(x):
    return x * 2

# define a doubling function that passes args by reference
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


# # try out the functions
# a = 12

# new_number = mult2(a)
# print(new_number)

# lst = [2, 4, 6, 8] # mutable
# mult2_list(lst)

# for num in lst:
#     print(num)


# Centered Average functions

def centered_avg1(ints):
    pass

def centered_avg2(ints):
    pass

# tests


numbers = [1, 41, 34, 29, 50, 50]

import time

start = time.time()
for i in range(1000):
    centered_avg1(numbers)
end = time.time()

print(end - start)

print("-----------------------")

start = time.time()
for i in range(1000):
    centered_avg2(numbers)
end = time.time()

print(end - start)
# a = 41 + 34 + 29 + 50
# print(a)

# b = a // 4

# print(b)