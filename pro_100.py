class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("BUBBLE_NOTE = 100")
        print("BUBBLE_coin = 200")
        print("BUBBLE_GC = 300")

    def withdrawl1(self,BUBBLE_NOTE):
        new_amount = 100 - BUBBLE_NOTE
        print("You have withdrawn amount "+str(BUBBLE_NOTE) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,BUBBLE_coin):
        new_amount = 200 - BUBBLE_coin
        print("You have withdrawn amount "+str(BUBBLE_coin) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,BUBBLE_GC):
        new_amount = 300 - BUBBLE_GC
        print("You have withdrawn amount "+str(BUBBLE_GC) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to BUBBLE'S Bank! Bhuwan welcome's You to Bank!!")
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. BUBBLE_NOTE")
        print("2. BUBBLE_coin")
        print("3. BUBBLE_GC")
        choose = int(input("1. Add BUBBLE_NOTE  2. Add BUBBLE_coin 3. Add BUBBLE_GC: "))
        if (choose == 1):
           BUBBLE_NOTE = int(input("Enter the amount:- "))
           new_user.withdrawl1(BUBBLE_NOTE)
        if (choose == 2):
           BUBBLE_coin= int(input("Enter the amount:- "))
           new_user.withdrawl2(BUBBLE_coin)    
        if (choose == 3):
           BUBBLE_GC = int(input("Enter the amount:- "))
           new_user.withdrawl3(BUBBLE_GC)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()