import functions
import PySimpleGUI as sg
import time
import os

# Creating a todos.txt file if it does not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in  a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
# having two square brackets is because we  want both elements in the same
# row. For separate rows, each element will have its own inner list box
while True:
    event, values = window.read() # Loop runs every 200 milliseconds
    window["clock"].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            if values['todo'] == '':
                sg.popup("Please enter a todo before clicking Add", font=['Helvetica', 10])
            else:
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item first", font=("Helvetica", 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select item first", font=("Helvetica", 20))

        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case sg.WIN_CLOSED:
            break
window.close()
