# # l = [1,5,4,2,7]
# # any(x==5 for x in l)
# # #print(min(l))
# # print(min(l, key=lambda x: x%7))
# data =[{'name': 'a', 'salary': 10},
#        {'name': 'b', 'salary': 8},
#        {'name': 'c', 'salary': 15},
#        {'name': 'd', 'salary': 9}]
# print(max(data[i]['salary'] for i in range(len(data))))
# print(max(data, key=lambda x:x['salary']))
#
# import os
# file_address = os.getcwd()
# file_name = "file1.txt"
# with open(f"{file_address}\\{file_name}","w") as file:
#        file.write("my text.\nMy text2")

# l = 'jhgjhgjhg'
# n = 465464
# f = 125654.24555
#
# print('{x:.5s}'.format(x = l))
# print('{}'.format(n))
# print('{x:.2f}'.format(x = f))
# import logging
#
# logger = logging.getLogger(__name__)
#
# from typing import Final
# PI: Final = 13.14
# print(PI)
# import functools
# def add_message(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kwargs):
# 		print(f'calling function : {func.__name__}')
# 		print(f'{args = }')
# 		print(f'{kwargs = }')
# 		return func(*args, **kwargs)
# 	return wrapper
# @add_message
# def gfunc(name=None , age=0):
# 	print(f'yes {name}')
#
#
# # gfunc("Ali" , age= 123)
# square = lambda x: (x, x**2)
# A =[1, 2, 3, 4]
# print(list(map( square, A)))
#
# print(list(map(lambda x: (x, x**2), A)))


# def get_input():
#     return input("Enter something: ")
# # ایجاد یک iterator که تا زمان دریافت '*' از get_input تکرار می‌شود
# for item in iter(get_input, '*'):
#     print("You entered:", item)


# a = [1,20,30,40,2,20,30,40,3,20,30,40,4,20,30,40]
# # it = iter(a)
# # print(list(zip(it,it,it)))
#
# slice(3,7,2)
# print(a[slice(0,5,2)])
# A = [1,2,5,8,7,9]
# f = [min , max]
# print(list(map(lambda f: f(A) , f)))


from student import *

student1 = Student("Ali","Aali",32)
student1.print_first_name()
w = person("a","b",18)
w.print_first_name()
