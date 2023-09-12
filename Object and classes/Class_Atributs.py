# --- Class Attribetes ---
# Это перменныеБ которые принадлежат самому классу, а не его экземплярамю
# Чтобы обьявить атрибут нужно обьявит переменную внутри класса, в верхней части класса

class Comment:
    total_comments = 0  # Создание атрибута

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1  # Используем его в функции класса


firs_comment = Comment('First comment')
print(Comment.total_comments)  # Обращение к атрибуту класса
