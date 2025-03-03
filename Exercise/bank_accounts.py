class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nUser {self.name}, have {self.balance} on the account.")

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException (
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\nDeposit Accepted")
            self.get_balance()
        else:
            print(f"\nPlease try a positive amount")
            self.get_balance()
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
            try: 
                print('\n**********\n\nBeginning Transfer.. 🚀')
                self.viable_transaction(amount) 
                self.withdraw(amount)
                #se refere a outro objeto na memória e não uma cópia dele, acessa outro objeto a partir dessa estrutura
                account.deposit(amount) 
                print('\nTransfer complete! ✅\n\n**********')
            except BalanceException as error: 
                print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        #bonus 5% for this tipy of account on the fuction deposit
        self.balance += (amount * 1.05)
        print("\nDeposit Complete")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        #classe filha tiver um __init__() próprio, o __init__() da mãe NÃO será chamado automaticamente, na classe Interst... não usa super pq não precisa de init, só modifica uma função
        super().__init__(initial_amount, acct_name)
        self.fee = 5 #taxa cobrada para modificar função Banckaccount

    def withdraw(self, amount): 
        try: 
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')

#aqui temos a classe mãe do Bankaccount, interest que herda a do bank, a saving que herda interest-> banck, usa super para chamar o init da classe que herdou, interest não tem, python joga init do bank, ou seja 3 classes com 'mesmas funções' 2 com msm init, mais que modificam 2 funções de depositar e de retirar