def account(user_account):
    initial_balance = 2000

    def deposit(amount):
        nonlocal initial_balance
        initial_balance += amount
        print(f"ACCEPT: Now you have ${initial_balance}")

    def withdraw(amount):
        nonlocal initial_balance
        initial_balance = initial_balance - amount
        if initial_balance < amount:
            print("DENIED: there aren't enough money")
        else:
            print(f"ACCEPT:Now you have ${initial_balance}")

    def get_balance():
        nonlocal initial_balance
        print(f"This is the quantity in you ACCOUNT BANK: {initial_balance}")

    return deposit, get_balance, withdraw

deposit_zacarias, get_balance_zacarias, withdraw_zacarias = account('zacarias')

deposit_zacarias(500)
get_balance_zacarias()
withdraw_zacarias(100)
get_balance_zacarias()



