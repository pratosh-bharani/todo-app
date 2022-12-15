FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the list
    of items in the text file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Write todos items in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__": ## adding this statement prevents the below code from executing
    # when called in another file like main_untilDay15.py
    # check day 14 code experiments on udemy 40 day python course
    print("Hello from functions")