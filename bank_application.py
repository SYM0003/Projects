from abc import ABC,abstractclassmethod
from random import randint
from sys import exit
import datetime

class Utility:

    history=[]
    @staticmethod
    def genAccount():
        ac='1'
        for i in range(11):
            ac+=str(randint(0, 9))
        return ac
    
    def addtransaction(msg,ac=0):
        Utility.history.append([msg,ac,datetime.datetime.now()])
class Account(ABC):
    bank='YOURBANK'
    def __init__(self,name,balance,min_balance):
        self.__acnum=Utility.genAccount()
        self.__name=name
        self.__balance=balance
        self.__min_balance=min_balance

    # utility methods
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
    def get_acnum(self):
        return self.__acnum
        
    
    def withdraw(self,amount):
        option=input('Enter your father name')
        count=2
        while option!=self.get_name() :
            if count==0:
                print('Your have entered wrong answer multiple times.please visit the bank')
                Utility.addtransaction('User entered wrong cradantials',self.get_acnum())
                break
            input('wrong answer,please try again')
            count-=0
        else:
            if amount>self.balance-self.min_balance:
                print('Insufficient funds')
                print(f'Your account balance is {self.__balance}')
                Utility.addtransaction('Insufficient funds',self.get_acnum())
            else:
                self.balance-=amount
                print(f'withdraw succefully')
                print(f'Remaining balance is {self.__balance}')
                Utility.addtransaction('withdraw succefully',self.get_acnum())

    def deposite(self,amount):
        self.__balance+=amount
        print(f'Deposited succefully')
        print(f'Your account balance is {self.__balance}')
        Utility.addtransaction('Deposited succefully',self.get_acnum())

    def balance(self):
        print(f'Your account balance is {self.__balance}')
        Utility.addtransaction('Balance request',self.get_acnum())

class SavingAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,0)
    
    def __str__(self):
        return f'Account holder name: {self.get_name()}\nAccount number: {self.get_acnum()}\nAccount balance: {self.get_balance()}'
class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,-1000)
    
    def __str__(self):
        return f'Account holder name: {self.get_name()}\nAccount number: {self.get_acnum()}\nAccount balance: {self.get_balance()}' 


print(f'Welcome to the online site of {Account.bank}')

print('If you want to open account,enter 1️\nif you already have account than enter 2️\nfor exit enter 0️⃣')
option=input('enter 1,2 or 0 only :')
count=2
while option not in ['1','2','0']:
    if count==0:
        print('\nYou have reached maximum attempts. Please try after some time.\n')
        Utility.addtransaction('Not able to create accouunt')
        exit()
        break
    option=input(f'Please enter correct option you only {count-1} attempt left:')
    count-=1
else:
    if option=='0':
        print(f'thankyou for reaching us')
        Utility.addtransaction('Exit account not created')
        exit()

    elif option=='2':
        print('This part is not implimented yet')
    else:
        print('Enter account type s(saving account) c(current account)')
        option=input('enter s or c: ').lower()
        count=2
        while option not in ['s','c']:
            if count==0:
                print('\nYou have reached maximum attempts. Please try after some time.\n')
                Utility.addtransaction('Not able to create accouunt')
                exit()
                break
            option=input(f'Please enter correct option you only {count-1} attempt left:')
            count-=1
        else:
            print('Thankyou for selecting option\n')
            if option=='s':
                name=input('Enter the customer name(first last): ')
                balance=eval(input('Enter intial balance that you want to Deposit(more than 100INR): '))
                count=2
                while balance<100 and count>=0:
                    balance=eval(input('Please enter amout more than 100rs!'))
                    count-=1
                if(balance>=100):
                    account=SavingAccount(name, balance)
                    print(f'\nAccount created succesfully. your details are:\n')
                    Utility.addtransaction('Account created succesfully',account.get_acnum())
                    print(account)
            else:
                name=input('Enter the Company name(first last): ')
                balance=eval(input('Enter intial balance that you want to Deposit(more than 10000INR): '))
                count=2
                while balance<1000 and count>=0:
                    balance=eval(input('Please enter amout more than 10000rs!'))
                    count-=1
                if(balance>=10000):
                    account=CurrentAccount(name, balance)
                    print(f'\nAccount created succesfully. your details are:\n')
                    Utility.addtransaction('Account created succesfully',account.get_acnum())
                    print(account)

print('Your histor:')  
print(Utility.history)