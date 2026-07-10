a = float(input("Enter the value of a: "))
calc = input("Enter the operation: ")
b = float(input("Enter the value of b: "))

  
if(calc=="+"):
 print(a+b)

elif(calc=="-"):
 print(a-b)

elif(calc=="*"):
 print(a*b)

elif(calc=="/"):
 if(b!=0):
  print(a/b)
 else:
  print("division by zero is not possible!")  

elif(calc=="%"):
 print(a%b)

elif(calc=="<="):
 print(a<=b)

elif(calc==">="):
 print(a>=b)


 

