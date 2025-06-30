# for i in range(10,100):
#     if i%10==7 or i//10==7:
#         print(i,end=" ")
# list1=[10,20,False]
# print(sum(list1))
n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
list2=[x for x in range(n) if x%2==1]
print(list2)
