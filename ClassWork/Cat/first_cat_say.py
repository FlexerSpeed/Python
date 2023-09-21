class Cat:
    def __init__(self, words):
        self.words = words

    def say(self):
        speech_bubble = "_" * (len(self.words) + 4)
        print("\t"+speech_bubble)
        print("\t"+f"< {self.words} >")
        print("\t"+"-" * len(speech_bubble))
        print("         /")
        print("        /")
        print("       /")
        print("      /")
        print("     /")
        print(" /\\_/\\")
        print("( o.o )")
        print(" > ^ <")


if __name__ == "__main__":
    user_input = input("What does the cat say? ")
    cat = Cat(user_input)
    cat.say()
