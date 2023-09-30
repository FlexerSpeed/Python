# --- Methods ---
# Методы представялют собой функции, которые определены внутри классов и могут быть вызваны
# на обьектах этого класса

class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


# --- Bound Methods (Привязанные методы) ---
# Cвязанны с конкретным обьктом класса
# (Когда вызываем привязанный метод он автоматически получает доступ к данным и атрибутам этого обьекта)
# метод является привязанным, усли у него первый параметр self

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):  # Является привязанным методом
        print(f'{self.name} is barking!')


my_dog = Dog('Gus')
my_dog.bark()  # bark вызывается на обьекте my_dog который экзепляр класса Dog


# --- Статические методы (Static method) ---
# Метод который не привязан ни к обьектам класса, ни к самому классу
# Статические методы могут быть вызванны на классе, а не на экземплярах классса
# Для определения статического метода используется декоратор @staticmethod
# Не имеет параметра self

class MathUtils:
    @staticmethod  # Декоратор
    def add(x, y):
        return x + y


result = MathUtils.add(2, 6)
print(result)
