bill = int(input("Enter bill: "))
charge = float(input("Amount to be paid if bill exceeds 200 units:"))
if(bill<=200):
    print("No bill")
elif(bill>200):
    print("Total charge: " ,(bill-200)*charge)