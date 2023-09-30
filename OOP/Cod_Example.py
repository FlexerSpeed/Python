import sqlite3


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._db_name = 'bank_accounts.db'
        self._conn = sqlite3.connect(self._db_name)
        self._create_table()
        account = self._get_account(owner)

        if not account:
            self._insert_into_account(owner, balance)
        else:
            self.balance = account['balance']

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Topped up {amount}. Your balance is - {self.balance}'
        else:
            return "Amount should be greater than zero"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f'Withdraw {amount}. Your balance is - {self.balance}'
        else:
            return 'Invalid amount or not enough funds'

    def _create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS accounts (
            owner  KEY PRIMARY KEY,
            balance REAL NOT NULL
        )
        '''
        self._conn.execute(query)
        self._conn.commit()

    def _insert_into_account(self, owner, balance):
        query = 'INSERT INTO accounts (owner, balance) VALUES (?, ?)'
        self._conn.execute(query, (owner, balance))
        self._conn.commit()

    def _update_account(self, owner, balance):
        query = 'UPDATE accounts SET balance = ? WHERE owner = ?'
        self._conn.execute(query, (owner, balance))
        self._conn.commit()

    def _get_account(self, owner):
        query = 'SELECT * FROM accounts WHERE owner = ?'
        cursor = self._conn.cursor()
        cursor.execute(query, (owner,))
        account = cursor.fetchone()
        if account:
            return {'owner': account[0], 'balance': account[1]}
        return None


account = BankAccount("John", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
