list1 = [1,5,0,4,0,0,0,0,0,10]
target = 15
from datetime import datetime

# def get_number():
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i]+list1[j] == 10:
#                 return ([i,j])
                

# start_time = datetime.now()
# print(get_number())
# print("first_function",datetime.now()- start_time)

# num1,num2 = 0
# while(num1+num2==0):
def fun1():
    list2 = []
    for i in range(len(list1)):
        remaning = target - list1[i]
        if remaning in list2:
            print([i,list1.index(remaning)])
            break
        else:
            list2.append(list1[i])


def fun2():
    for i in range(len(list1)):
        remaning  = target - list1[i]
        if remaning in list1:
            print(i,list1.index(remaning))
            break


start_time = datetime.now()
fun2()
print(datetime.now()- start_time)
start_time = datetime.now()
fun1()
print(datetime.now()- start_time)