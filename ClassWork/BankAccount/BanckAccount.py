class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_dep(self):
        print('Your balance is: $', self.balance)

    def deposit(self, add_money):
        self.balance += add_money
        print('Deposit Accepted. Your balance is: $', self.balance)

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print('Withdrawal Accepted. Your balance is: $', self.balance)
        else:
            print('Funds Unavailable!')


owner_name = input('Enter owner name: ')
initial_balance = float(input('Enter initial balance: '))
acct1 = Account(owner_name, initial_balance)

while True:
    print('\n1. Show Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Quit')

    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        acct1.show_dep()
    elif choice == '2':
        amount = float(input('Enter the amount to deposit: '))
        acct1.deposit(amount)
    elif choice == '3':
        amount = float(input('Enter the amount to withdraw: '))
        acct1.withdraw(amount)
    elif choice == '4':
        print('Thank you for using the account!')
        break
    else:
        print('Invalid choice. Please choose 1, 2, 3, or 4.')
