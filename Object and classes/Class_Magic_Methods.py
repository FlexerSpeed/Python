# --- Magic methods in class ---

class Comment:

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.upvote += 1

    def __add__(self, other):
        return (f'{self.text} {other.text}', self.votes_qty + other.votes_qty)
