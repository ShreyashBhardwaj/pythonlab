list1=[1,2,3,4,5,6]

print("Slicing")
start=int(input("enter Start:"))
stop=int(input("enter stop:"))
step=int(input("enter step:"))

print(list1[start:stop:step])

print("appending")
list1.append(5)
list1.extend([1,2,3])
print(list1)

list2=[1,2,3,["A","B","C"]]

print(f"Element in Nested list:{list2[3][1]}")
