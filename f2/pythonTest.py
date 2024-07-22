# # l = [1,5,4,2,7]
# # any(x==5 for x in l)
# # #print(min(l))
# # print(min(l, key=lambda x: x%7))
# data =[{'name': 'a', 'salary': 10},
#        {'name': 'b', 'salary': 8},
#        {'name': 'c', 'salary': 15},
#        {'name': 'd', 'salary': 9}]
# print(max(data[i]['salary'] for i in range(len(data))))
# print(max(data,key= lambda x:x['salary']))

import os
file_address = os.getcwd()
file_name = "file1.txt"
with open(f"{file_address}\\{file_name}","w") as file:
       file.write("my text.\nMy text2")