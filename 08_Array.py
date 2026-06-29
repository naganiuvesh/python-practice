name = ['uvesh', 'nagani']
print(f"My surname is {name[1]} and my name is {name[0]}")

from array import array

arr = array('i',[1, 2, 3, 4, 5])
print(arr[0])
print(arr[2])
print(arr[4])

print(arr)
print("Length of array is :",len(arr)) # len is use to print lenth of array

arr.append(6) # 6 is ADD in array
arr.remove(1) # 1 is Removed in array
print(arr)

arr.insert(0, 1)
print(arr)

arr.pop() # pop is used to remove last element in array that's whay 6 is Removed in array
print(arr)

print(arr)
print(arr.index(5)) # Chake for index number of element 

print(arr)
print(arr.count(5)) # How much time 5 in array

print(arr)
arr.reverse() # used to print array in reverse order
print("Reverse", arr)
arr.reverse() # it use to re-reverse 
print(arr) 

print(arr)
arr[4] = 6
print(arr)
