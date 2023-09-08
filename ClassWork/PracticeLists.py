todo_list = []

while True:
    persons_task = input(
        'Enter the task what you need to-do. Press <enter> when done: ')
    if persons_task:
        todo_list.append(persons_task)
    else:
        break

print('Your To-Do List:\n', ('_' * 20))

for i, task in enumerate(todo_list, start=1):
    print(f'{i}: {task}')
