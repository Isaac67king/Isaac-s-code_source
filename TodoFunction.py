# read function
def todo_read(filepath='todos.txt'):
    with open('todos.txt', 'r') as file:
        file = file.readlines()
    return file


# write function
def todo_write(todo, filename='todos.txt'):
    with open('todos.txt', 'w') as file:
        file.writelines(todo)

