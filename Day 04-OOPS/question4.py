class rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
    def getdata(self):
        self.length = int(input("Enter the length:"))
        self.breadth = int(input("Enter the breadth:"))
    def area(self):
        if(self.length==self.breadth):
            print("Area of Square:",self.length*self.breadth)
        else:
           print("Area of rectangle is:",self.length*self.breadth)
    
    def perimeter(self):
        if(self.length==self.breadth):
            print("Perimeter of Square:",4*self.length)
        print ("Perimeter of rectanlge is:",2*(self.length+self.breadth))
    
    def ifsquare(self):
        if(self.length==self.breadth):
            print("This is a square")
        else:
            print("A Rectangle")

a1 = rectangle()
a1.getdata()
a1.ifsquare()
a1.area()
a1.perimeter()
