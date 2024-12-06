import FreeSimpleGUI as sG
import TodoFunction as tF


input_box = sG.InputText(tooltip="task", key="todo")
add_button = sG.Button("Add")
list_box = sG.Listbox(values=tF.todo_read(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sG.Button("Edit")
delete_button = sG.Button("Complete")
exit_button = sG.Button("Exit")

window = sG.Window(title="Todo App",
                   layout=[[input_box, add_button], [list_box], [edit_button, delete_button, exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = tF.todo_read()
            todo = values["todo"] + "\n"

            todos.append(todo)

            tF.todo_write(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = tF.todo_read()
            index = todos.index(todo_to_edit)

            todos[index] = new_todo
            tF.todo_write(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Complete':
            todo_to_delete = values['todos'][0]
            todos = tF.todo_read()

            todos.remove(todo_to_delete)

            tF.todo_write(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            window.close()
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sG.WIN_CLOSED:
            break

window.close()

