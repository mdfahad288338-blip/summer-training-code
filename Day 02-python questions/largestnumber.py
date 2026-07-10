# 20,21,70,80,64,36

arr = [20,21,70,80,64,36]
largest = arr[0]
for i in arr:
    if(i>largest):
        largest = i
print(largest)

sum = 0
for i in arr:
   sum = sum+i
print(f"sum of all the elements in the array is:{sum}")
print(f"average of the given number is : {sum/6}")