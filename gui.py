from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in  a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# having two squarebrackets is because we  want both elements in the same
# row. For separate lines, each element will have its own inner list box
window.read()
window.close()
