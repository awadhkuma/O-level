# count=0
# while count<=5:
#     # print(count)
#     count=count+1
# #     print(count)


def have_common_item(list1,list2):
    return any (item in list1 for item in list2)

list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
print(have_common_item(list1,list2))
list3=['a','b','c']
list4=['x','y','z']
print(have_common_item(list3,list4))




def add(a,b):
    print(a+b)
try:
    a=int(input("enter any number:"))
    b=int(input("enter any number:"))
    add(n1,n2)
except:
    print("errrrrrrrrrrr")    


    