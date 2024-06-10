import array as arr

# a = arr.array('i',[10,20,30,50,345,40,60,70,80,90,100])
# b = list(a)
# b.sort()
# c = arr.array('i',b)
# print(c)


#2) create list and write python script to remove all non int element

# a = 5
# b = [1,3,5,'hello','hi',2,76,'how']
# c = []
# for i in b:
#     if type(i) == type(a):
#         c.append(i)

# print(c)

#3) write py script to print average for list element

# def avg(l):
#     n = 0
#     for i in l:
#         n += i
        
#     return n/len(l)
    
# mylist = [1,2,3,4,500,60,70,80,90,100]
# result = avg(mylist)

# print(result)

# 4) write py script to create list of first n prime number.
# import math
# def prime(n):
#     if n == 1:
#         return 'not prime'
#     for i in range(2,round(math.sqrt(n))+1):
#         if n % i == 0:
#             return 'not prime'
#         else:
#             return 'prime'
        

# num = prime(float(input("check your prime number :")))

# print(num)

# 5) write py script to create list of first n fibonacci number.

# n = int(input("enter positive number : "))
# x = 0
# y = 1
# z = 0

# while z <= n:
#     print(z)
#     x = y
#     y = z
#     z = x+y
