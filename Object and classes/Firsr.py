# Классы это шаблоны для обьектов
# Из одного класса можно создавать экземпляры обьектов
# Экземпляры могут иметь собственные атрибуты
# Экземпляры наследуют все атрибуты классов

class Car:
    def move(self):  # self это указание на определённый экземпляр класса Car
        print('Car is moving')

    def stop(self):  # Функция будет вызываться для конкретного экземплярва класса
        print('Car stopped')  # Наследуется всеми экземплярами класса


my_car = Car()  # my_car - экземпляр класса Car. Car является функцией конструктором
my_car.move()  # Обращение к методам наследованным от класса Car
# При этом my_car выступает аргументом в методе move. Так как в классе Car прописано Self

# Магический метод __init__. Это ключевая функция конструктор
# Собственные атрибуты экземпляров определяются с помощью функции __init__


class Comment:
    def __init__(self, text):  # Является функцией конструктором для класса
        self.text = text
        self.votes_qty = 0

    def upvote(self):         # Является методом для класса
        self.votes_qty += 1


firs_comment = Comment('First comment')
"""
Пошаговое обьяснение проиходящего:
1 - firs_comment = Comment('First comment') Пайтон сздаёт новый обьект в памяти
2 - firs_comment передаентся в функцию init класса Comment как параметр self
3 - ('First comment') передаётся как значение следующего параметра text
4 - Внутри функции init для созданного обьекта firs_comment Пайтон добавляет два атрибута (text, votes_qty) и присваивает им указанные значения
5 - В итоге мы можем вызывать методы класса Comment для экземпляра firs_comment
"""

my_comment = Comment('My comment')

print(my_comment.__dict__)
print(my_comment.text)
my_comment.upvote()
print(my_comment.votes_qty)


# --- Practical Task ---
class Image:
    def __init__(self, resolution, title, extention):
        self.resolution = resolution
        self.title = title
        self.extention = extention

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def rename(self, new_name):
        self.title = new_name


new_image = Image('1920x1080', 'My Dog', 'jpg')

new_image.resize('1500x900')
new_image.rename('My lovely dog')

print(new_image.resolution)
print(new_image.title)

# --- Task Two ---


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_dep(self):
        print('Your balance is: $', self.balance)

    def deposit(self, add_mony):
        self.balance += add_mony
        print('Deposit Accepted. Your balance is: $', self.balance)

    def withdraw(self, withdraw):
        if (self.balance >= withdraw):
            self.balance -= withdraw
            print('Withdrawal Accepted. Your balance is: $', self.balance)
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)
acct1.show_dep()
