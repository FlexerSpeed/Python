from os import system
from ClassWork.Cat.first_cat_say import Cat

if __name__ == "__main__":
    question = None
    while question != "q":
        print("Type \"q\" to end the program")
        question = input("What does the cat say?")
        system("cls")
        if question != "q":
            cat1 = Cat(question)
            cat1.say()
            del cat1
