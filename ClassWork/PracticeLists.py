todo_list1 = []

while True:
    persons_task = input(
        'Enter a task for your to-do list. Press <enter> when done: ')
    if persons_task:
        todo_list1.append(persons_task)
    else:
        break

print('Your To-Do List:\n', ('_' * 20))
for i, task in enumerate(todo_list1, start=1):
    print(f'{i}: {task}')
