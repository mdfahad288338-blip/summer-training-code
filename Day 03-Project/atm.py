#select language
#cash withdraw
#balance 
#change password
#help
pin = 1234
balance = 123000
print("""Welcome to "Fahad's" biggest atm of India""")
lang = input("Select language english or hindi: ")
if(lang=='english'):
    print("1.Cash Withdraw\n2.Balance\n3.Change password\n4.Help\n ")
    option=int(input("Option:"))
    if(option==2):
        a = int(input("Enter pin:"))
        if(a==pin):
            print("Your balance is:",balance)
        else:
            print("Not found!")
    elif(option==1):
        z = int(input("Enter amount:"))
        c = int(input("Enter the pin: "))
        if(c==1234):
            balance = balance-z
            print("left amount: ",balance)
    elif(option==3):
        p = int(input("Enter previous pin: "))
        if(p==pin):
            pin1=int(input("Enter new pin: "))
        else:
            print("Wrong pin")
    elif(option==4):
        print("help not fount sorrie!!")

else:
   if(lang=='hindi'):
    print("नकद निकासी\nबैलेंस\nपिन बदलें\nसहायता\n")
    option=int(input("Option:"))
    if(option==2):
        a = int(input("पिन दर्ज करें: "))
        if(a == pin):
            print("आपका बैलेंस है:", balance)
        else:
            print("गलत पिन!")

    elif(option==1):
        z = int(input("राशि दर्ज करें: "))
        c = int(input("पिन दर्ज करें: "))
        if(c == 1234):
            balance = balance - z
            print("शेष राशि:", balance)

    elif(option==3):
        p = int(input("पुराना पिन दर्ज करें: "))
        if(p == pin):
            pin1 = int(input("नया पिन दर्ज करें: "))
            pin = pin1
            print("पिन सफलतापूर्वक बदल दिया गया।")
        else:
            print("गलत पिन!")

    elif(option==4):
        print("sahayta not found sorrie!!")    




