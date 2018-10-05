from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankUser:
    def __init__(self, owner):
        self.owner = owner
        self.saving = False
        self.checking = False
        self.saving_balance = None
        self.checking_balance = None

    def addAccount(self, accountType):
        if not self.saving or not self.checking:
            if accountType == AccountType.SAVINGS and not self.saving:
                self.saving = True
                self.saving_balance = 0
            elif accountType == AccountType.CHECKING and not self.checking:
                self.checking = True
                self.checking_balance = 0
            else:
                print('Only one savings/checking account per user.')
        else:
            print('Only one savings/checking account per user.')

    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS and self.saving:
            print('Current Balance:', self.saving_balance)
        elif accountType == AccountType.CHECKING and self.checking:
            print('Current Balance:', self.checking_balance)
        else:
            print('Do not have this type of account.')

    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.saving:
                if isinstance(amount, int):
                    self.saving_balance = self.saving_balance + amount
                    print('Current Balance:', self.saving_balance)
                else:
                    print("Deposit amount is illegal")
            else:
                print('Do not have this type of account.')
        elif accountType == AccountType.CHECKING:
            if self.checking:
                if isinstance(amount, int):
                    self.checking_balance = self.checking_balance + amount
                    print('Current Balance:', self.checking_balance)
                else:
                    print("Deposit amount is illegal")
            else:
                print('Do not have this type of account.')
        else:
            print('Do not have this type of account.')

    def withdraw(self, accountType, amount):
        try:
            if accountType == AccountType.SAVINGS and self.saving:
                assert self.saving_balance >= amount and amount > 0 and isinstance(amount, int)
                self.saving_balance = self.saving_balance - amount
                print('Current Balance:', self.saving_balance)
            elif accountType == AccountType.CHECKING and self.checking:
                assert self.checking_balance >= amount and amount > 0 and isinstance(amount, int)
                self.checking_balance = self.checking_balance - amount
                print('Current Balance:', self.checking_balance)
            else:
                print('Do not have this type of account.')
        except AssertionError:
            print("Withdraw amount is illegal")


def ATMSession(bankUser):
    def Interface():
        choise = int(input(
            'Enter Option:\n' + '1)Exit\n' + '2)Create Account\n' + '3)Check Balance\n' + '4)Deposit\n' + '5)Withdraw\n'))
        while choise != 1:
            if choise < 1 or choise > 5:
                print('Please enter an available option.')
            else:
                print('Enter Option:')
                print('1)Checking')
                print('2)Savings')
                accType = int(input())
                while accType not in [1, 2]:
                    accType = int(input('Please input 1 for checking or 2 for savings.'))
                if choise == 2:
                    if accType == 1:
                        bankUser.addAccount(AccountType.CHECKING)
                    else:
                        bankUser.addAccount(AccountType.SAVINGS)

                elif choise == 3:
                    if accType == 1:
                        bankUser.getBalance(AccountType.CHECKING)
                    else:
                        bankUser.getBalance(AccountType.SAVINGS)

                elif choise == 4:
                    # check whether has the certain account
                    if accType == 1:
                        if bankUser.checking:
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                            try:
                                amount = int(amount)
                            except ValueError:
                                amount = float(amount)
                            while amount < 0 or not isinstance(amount, int):
                                amount = input('Enter Integer Amount, Cannot Be Negative:')
                                try:
                                    amount = int(amount)
                                except ValueError:
                                    amount = float(amount)
                            bankUser.deposit(AccountType.CHECKING, amount)
                        else:
                            print('Do not have this type of account.')

                    else:
                        if bankUser.saving:
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                            try:
                                amount = int(amount)
                            except ValueError:
                                amount = float(amount)
                            while amount < 0 or not isinstance(amount, int):
                                amount = input('Enter Integer Amount, Cannot Be Negative:')
                                try:
                                    amount = int(amount)
                                except ValueError:
                                    amount = float(amount)
                            bankUser.deposit(AccountType.SAVINGS, amount)
                        else:
                            print('Do not have this type of account.')

                else:
                    if accType == 1:
                        if bankUser.checking:
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                            try:
                                amount = int(amount)
                            except ValueError:
                                amount = float(amount)
                            while amount < 0 or not isinstance(amount, int):
                                amount = input('Enter Integer Amount, Cannot Be Negative:')
                                try:
                                    amount = int(amount)
                                except ValueError:
                                    amount = float(amount)
                            bankUser.withdraw(AccountType.CHECKING, amount)
                        else:
                            print('Do not have this type of account.')
                    else:
                        if bankUser.saving:
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                            try:
                                amount = int(amount)
                            except ValueError:
                                amount = float(amount)
                            while amount < 0 or not isinstance(amount, int):
                                amount = input('Enter Integer Amount, Cannot Be Negative:')
                                try:
                                    amount = int(amount)
                                except ValueError:
                                    amount = float(amount)
                            bankUser.withdraw(AccountType.SAVINGS, amount)
                        else:
                            print('Do not have this type of account.')

            choise = int(input(
                'Enter Option:\n' + '1)Exit\n' + '2)Create Account\n' + '3)Check Balance\n' + '4)Deposit\n' + '5)Withdraw\n'))

    return Interface
