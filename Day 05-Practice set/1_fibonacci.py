# 0 1 1 2 3 5 8 13 ...
def fibonacci(n):
 if(n<=1) :
  return n
 else:
  last = fibonacci(n-1)
  slast = fibonacci(n-2)
  return (last + slast)
  
print(fibonacci(6))

