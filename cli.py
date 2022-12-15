import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)
while True:
    user_action = input("Type add, show, edit, complete or exit").lower().strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):  ## " | 'display' "   Use vertical line for OR

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            edit_text = input("Enter replacement task: ").strip() + '\n'

            todos = functions.get_todos()

            todos[number - 1] = edit_text

            functions.write_todos(todos)

        except ValueError:
            print("Enter a numeric value after edit")
        except:
            print("Other Error")

    elif user_action.startswith('complete'):
        try:
            item_remove = int(user_action[9:])
            index = item_remove - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"{todo_to_remove} has been removed.")
        except IndexError:
            print("Task Number does not exist.")
        except ValueError:
            print("Enter a numeric value after edit")
        except:
            print("Other Error")

    elif user_action.startswith('exit'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")
        print('Bye!')
        break

    else:
        print("Entered an unkonwn command")
